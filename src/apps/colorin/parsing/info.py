import requests
from django.contrib.auth import get_user_model
from apps.colorin.models import InstagramPhoto, InstagramProfile
from apps.colorin.parsing.images import save_images
from django.core import files
import random
import string
from apps.colorin.palette.get import get_palette, get_dominant


def get_info(request):
    url = "https://www.instagram.com/" + request.user.username + "/?__a=1"

    r = requests.get(url, headers={
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"})
    instagram_json = r.json()

    inst_user = instagram_json["graphql"]["user"]
    inst_profile_pic = inst_user["profile_pic_url_hd"]
    inst_full_name = inst_user["full_name"]
    inst_biography = inst_user["biography"]
    inst_profile_pic_url = inst_profile_pic

    inst_list_of_photo = inst_user["edge_owner_to_timeline_media"]["edges"]
    inst_photo = [inst_list_of_photo[item]["node"]["display_url"] for item in range(10)]

    if InstagramProfile.objects.filter(user_id=request.user.id).exists():
        print("Profile already exists")

        inst_profile = InstagramProfile.objects.get(user_id=request.user.id)
        value_of_inst_full_name = inst_profile.inst_full_name
        value_of_inst_biography = inst_profile.inst_biography
        value_of_inst_profile_pic_url = inst_profile.inst_profile_pic_url

        if value_of_inst_full_name != inst_full_name:
            inst_profile.inst_full_name = inst_full_name

        if value_of_inst_biography != inst_biography:
            inst_profile.inst_biography = inst_biography

        if value_of_inst_profile_pic_url != inst_profile_pic_url:
            inst_profile.inst_profile_pic_url = inst_profile_pic_url

            lf = save_images(inst_profile_pic_url)
            file_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8)) + '.jpg'

            inst_profile.inst_theme_color = get_dominant(lf)

            inst_profile.inst_profile_pic.save(file_name, files.File(lf))

        inst_profile.save()
        print("Profile changes saved")


        number_of_colors = 6

        for photo_url in inst_photo:

            if not InstagramPhoto.objects.filter(user_id=request.user.id, photo_url=photo_url).exists():
                print("Update - photo dont exists")
                lf = save_images(photo_url)
                file_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8)) + '.jpg'

                inst_img = InstagramPhoto(user_id=request.user.id,
                                          photo_url=photo_url,
                                          palette=get_palette(lf, number_of_colors),
                                          dominant=get_dominant(lf))
                inst_img.photo.save(file_name, files.File(lf))
                inst_img.save()
                print("Update - new photo from new url saved")

        inst_photo_queryset = InstagramPhoto.objects.filter(user_id=request.user.id).all()
        for item in inst_photo_queryset:
            if item.photo_url not in inst_photo:
                item.delete()
                print("Update - old photo deleted")

        return True

    elif not InstagramProfile.objects.filter(user_id=request.user.id).exists():

        print("Profile DO NOT exists")
        lf = save_images(inst_profile_pic)
        file_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8)) + '.jpg'

        inst_theme_color = get_dominant(lf)

        inst_profile = InstagramProfile(user_id=request.user.id, inst_full_name=inst_full_name,
                                        inst_biography=inst_biography, inst_theme_color=inst_theme_color,
                                        inst_profile_pic_url=inst_profile_pic_url)
        inst_profile.inst_profile_pic.save(file_name, files.File(lf))
        inst_profile.save()
        print("Profile was created")

        number_of_colors = 6
        print("Num of photo from request")
        print(len(inst_photo))

        for url in inst_photo:
            lf = save_images(url)
            file_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8)) + '.jpg'

            inst_img = InstagramPhoto(user_id=request.user.id,
                                      photo_url=url,
                                      palette=get_palette(lf, number_of_colors),
                                      dominant=get_dominant(lf))
            inst_img.photo.save(file_name, files.File(lf))
            inst_img.save()
            print("Photo from IG saved (first iteration)")
        return True