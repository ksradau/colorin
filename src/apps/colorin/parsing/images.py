import requests
import tempfile

from django.core import files
from django.contrib.auth import get_user_model
from apps.colorin.models import InstagramPhoto, InstagramProfile

User = get_user_model()


def save_images(image_url):

    request = requests.get(image_url, stream=True)

    lf = tempfile.NamedTemporaryFile()

    for block in request.iter_content(1024 * 8):

        if not block:
            break

        lf.write(block)
    
    return lf

