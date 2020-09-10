import requests
from django.contrib.auth import get_user_model
from apps.colorin.models import InstagramPhoto, InstagramProfile
from apps.colorin.parsing.images import save_images
from django.core import files
import random
import string
from apps.colorin.palette.get import get_palette
from apps.colorin.palette.match import get_similar_of_all_img_colors
from proxy_requests import ProxyRequests
from apps.colorin.parsing.proxy import proxies as prox


def update_profile(request):
    print("Profile already exists, start update process")

    url = "https://www.instagram.com/" + request.user.username + "/?__a=1"




    r = requests.get(url, headers={'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"})

    instagram_json = r.json()


    inst_user = instagram_json["graphql"]["user"]
    inst_profile_pic = inst_user["profile_pic_url_hd"]
    inst_full_name = inst_user["full_name"]
    inst_biography = inst_user["biography"]
    inst_profile_pic_url = inst_profile_pic

    inst_list_of_photo = inst_user["edge_owner_to_timeline_media"]["edges"]

    inst_photo = []
    for item in range(10):
        try:
            inst_photo.append(inst_list_of_photo[item]["node"]["display_url"])
        except IndexError:
            pass

    inst_profile = InstagramProfile.objects.get(user_id=request.user.id)
    value_of_inst_full_name = inst_profile.inst_full_name
    value_of_inst_biography = inst_profile.inst_biography
    value_of_inst_profile_pic_url = inst_profile.inst_profile_pic_url

    if value_of_inst_full_name != inst_full_name:
        inst_profile.inst_full_name = inst_full_name
        print("Update - Full name NEW")
    else:
        print("Update - Full name the same")

    if value_of_inst_biography != inst_biography:
        inst_profile.inst_biography = inst_biography
        print("Update - Bio NEW")
    else:
        print("Update - Bio the same")

    if value_of_inst_profile_pic_url != inst_profile_pic_url:
        inst_profile.inst_profile_pic_url = inst_profile_pic_url
        print("Update - Ava NEW")

        lf = save_images(inst_profile_pic_url)
        file_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8)) + '.jpg'

        palette = get_palette(lf, 2)
        inst_theme_color = palette[0]
        inst_profile.inst_theme_color = inst_theme_color

        inst_profile.inst_profile_pic.save(file_name, files.File(lf))
    else:
        print("Update - Ava the same")

    inst_profile.save()


    number_of_colors = 6

    for photo_url in inst_photo:

        if not InstagramPhoto.objects.filter(user_id=request.user.id, photo_url=photo_url).exists():
            print("Update - photo don't exists")
            lf = save_images(photo_url)
            file_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8)) + '.jpg'

            palette = get_palette(lf, number_of_colors)
            dominant = palette[0]
            similar = get_similar_of_all_img_colors(palette)

            inst_img = InstagramPhoto(user_id=request.user.id,
                                      photo_url=photo_url,
                                      palette=palette,
                                      dominant=dominant,
                                      similar=similar,)

            inst_img.photo.save(file_name, files.File(lf))
            inst_img.save()
            print("Update - new photo from new url saved")
        else:
            print("Update - photo the same")

    inst_photo_queryset = InstagramPhoto.objects.filter(user_id=request.user.id).all()
    for item in inst_photo_queryset:
        if item.photo_url not in inst_photo:
            item.delete()
            print("Update - old photo deleted")


def create_profile(request):
    print("Profile DO NOT exists")

    url = "https://www.instagram.com/" + request.user.username + "/?__a=1"

    cookies = dict(
        urlgen='{\"46.53.243.32\": 42772\054 \"46.53.246.243\": 42772\054 \"46.53.243.255\": 42772}:1kFi8I:rwngNqAwZcgWGK41JBCeAiAVXVo")',
        csrftoken='KDWwc6eG8hENKwo1fXFkB66Eu6Raa9lp',
        shbts="1599427996\0544773271606\0541630963996:01f7eb9d024dff2aa1ed6bb90c5f772c92e5ee2f045dc27918773afd2e473e294fd53be1",
        ig_did='E7BBC664-7EAF-40DD-B381-0729AF98F138',
        rur="FRC\0544773271606\0541631115511:01f7787b1ca482d6510bbf64b089e3065a0e3ab1f35313ff6c93735f440aa270b06788cb",
        shbid="8142\0544773271606\0541630963996:01f7459734a8b26f5faa8ba87ab42faafaefe9a0920e6b17b8ad2b604d5931063cf5bfa4",
        mcd='3',
        mid='W02wugALAAGZdS00qvpTLOWHC1JL'
        )

    r = requests.get(url, cookies=cookies, headers={
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"})
    instagram_json = r.json()

    inst_user = instagram_json["graphql"]["user"]
    inst_profile_pic = inst_user["profile_pic_url_hd"]
    inst_full_name = inst_user["full_name"]
    inst_biography = inst_user["biography"]
    inst_profile_pic_url = inst_profile_pic

    inst_list_of_photo = inst_user["edge_owner_to_timeline_media"]["edges"]

    inst_photo = []
    for item in range(10):
        try:
            inst_photo.append(inst_list_of_photo[item]["node"]["display_url"])
        except IndexError:
            pass

    lf = save_images(inst_profile_pic_url)
    file_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8)) + '.jpg'

    palette = get_palette(lf, 2)
    inst_theme_color = palette[0]

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

        palette = get_palette(lf, number_of_colors)
        dominant = palette[0]
        similar = get_similar_of_all_img_colors(palette)

        inst_img = InstagramPhoto(user_id=request.user.id,
                                  photo_url=url,
                                  palette=palette,
                                  dominant=dominant,
                                  similar=similar,)

        inst_img.photo.save(file_name, files.File(lf))
        inst_img.save()
        print("Photo from IG saved (first iteration)")
