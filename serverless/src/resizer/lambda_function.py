import os
from io import BytesIO
from typing import NamedTuple

import boto3
import requests
from PIL import Image

S3 = boto3.client("s3")

API_URL = os.getenv("API_URL")
assert API_URL

TOKEN = os.getenv("TOKEN")
assert TOKEN


class S3File(NamedTuple):
    bucket: str
    key: str


def lambda_handler(event, context):
    assert context

    files = get_files(event)
    for s3_file in files:
        resize(s3_file)
        patch(s3_file)


def get_files(event: dict):
    for record in event["Records"]:
        s3 = record["s3"]
        bucket = s3["bucket"]["name"]
        key = s3["object"]["key"]

        print(f"processing: {bucket} | {key}")

        if "thumbnail" in key:
            print("skip thumbnail")
            continue

        yield S3File(
            bucket=bucket, key=key,
        )


def resize(s3_file: S3File):
    size = (128, 128)
    original = download_image(s3_file)
    location, image_file = s3_file.key.split("/")
    image_file_parts = image_file.split(".")
    image_file_name = ".".join(image_file_parts[:-1])
    image_file_ext = image_file_parts[-1]
    image_format = image_file_ext.upper()
    if image_format == "JPG":
        image_format = "JPEG"
    image = Image.open(original)
    image.thumbnail(size, Image.ANTIALIAS)
    resized = BytesIO()
    image.save(resized, image_format)
    resized.seek(0)
    new_key = f"{location}/{image_file_name}__thumbnail.{image_file_ext}"
    S3.upload_fileobj(
        resized,
        s3_file.bucket,
        new_key,
        ExtraArgs={
            "ACL": "public-read",
            "ContentType": f"image/{image_format.lower()}",
        },
    )
    print(f"uploaded to: {s3_file.bucket} | {new_key}")


def download_image(s3_file: S3File):
    image = BytesIO()
    S3.download_fileobj(s3_file.bucket, s3_file.key, image)
    print(f"downloaded: {s3_file}: {image.tell()} bytes")
    image.seek(0)
    return image


def patch(s3_file: S3File):
    location, image_file = s3_file.key.split("/")
    image_file_parts = image_file.split(".")
    image_file_name = ".".join(image_file_parts[:-1])
    image_file_ext = image_file_parts[-1]
    thumb_name = f"{image_file_name}__thumbnail.{image_file_ext}"

    resp = requests.get(f"{API_URL}/", headers={"AUTHORIZATION": f"Token {TOKEN}"})
    payload = resp.json()
    obj = next(filter(lambda elm: image_file_name in elm["original"], payload))
    resp = requests.patch(
        f"{API_URL}/{obj['uuid']}/",
        json={"thumbnail": thumb_name},
        headers={"AUTHORIZATION": f"Token {TOKEN}"},
    )
    print(f"XXX patch resp: {resp}")