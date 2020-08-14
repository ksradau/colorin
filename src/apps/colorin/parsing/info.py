import requests
from django.contrib.auth import get_user_model
from apps.colorin.models import InstagramPhoto, InstagramProfile
from apps.colorin.parsing.images import save_images
from django.core import files
import random
import string


def get_info(request):
    url = "https://www.instagram.com/" + request.user.username + "/?__a=1"

    r = requests.get(url, headers={
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"})
    instagram_json = r.json()

    inst_user = instagram_json["graphql"]["user"]
    inst_profile_pic = inst_user["profile_pic_url_hd"]
    inst_full_name = inst_user["full_name"]
    inst_biography = inst_user["biography"]
        
    lf = save_images(inst_profile_pic)
    file_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8)) + '.jpg'

    inst_profile = InstagramProfile(user_id=request.user.id, inst_full_name=inst_full_name,
                                    inst_biography=inst_biography)
    inst_profile.inst_profile_pic.save(file_name, files.File(lf))
    inst_profile.save()

    inst_list_of_photo = inst_user["edge_owner_to_timeline_media"]["edges"]

    inst_photo = [inst_list_of_photo[item]["node"]["display_url"] for item in range(10)]

    if InstagramPhoto.objects.filter(user_id=request.user.id).exists():
        InstagramPhoto.objects.filter(user_id=request.user.id).delete()

    for photo_url in inst_photo:
        lf = save_images(photo_url)
        file_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8)) + '.jpg'

        inst_img = InstagramPhoto(user_id=request.user.id)
        inst_img.photo.save(file_name, files.File(lf))
        inst_img.save()
