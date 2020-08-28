from django.contrib.auth import get_user_model
from apps.colorin.models import InstagramPhoto, UploadedPhoto, EmojiPic
import requests


def match(request):
    inst_photo_queryset = InstagramPhoto.objects.filter(user_id=request.user.id).all()
    all_colors_array = []
    for item in inst_photo_queryset:
        similar_list = eval(item.similar)
        all_colors_array += similar_list

    uploaded_photo_queryset = UploadedPhoto.objects.filter(user_id=request.user.id).all()
    for img in uploaded_photo_queryset:
        match_counter = 0
        palette = eval(img.palette)
        for color in palette:
            if color in all_colors_array:
                match_counter += 1
                print("~~~ It's a MATCH !!!")
            else:
                print("~~~ Oh no")
        print("~~~ Num of matches in img:")
        print(match_counter)
        if match_counter > 4:
            img.is_match = True
            print("is_match field TRUE")
        else:
            img.is_match = False
            print("is_match field FALSE")
        img.save()

    emoji_match(request)


def get_similar_of_all_img_colors(palette):
    _all = []
    for color in palette:
        color_array = get_similar_of_one_color(color)
        _all += color_array
    return _all


def get_similar_of_one_color(color):
    T = 15
    tolerance_list = []
    r, g, b = color[0], color[1], color[2]
    for rn in range(r - T, r + T):
        for gn in range(g - T, g + T):
            for bn in range(b - T, b + T):
                if rn > 255:
                    rn = 255
                if gn > 255:
                    gn = 255
                if bn > 255:
                    bn = 255
                tolerance_list.append((abs(rn), abs(gn), abs(bn),))
    return set(tolerance_list)


def emoji_match(request):
    emoji_pic_queryset = UploadedPhoto.objects.filter(user_id=request.user.id).all()
    for pic in emoji_pic_queryset:
        match_counter = 0
        palette = eval(pic.similar)
        for color in palette:
            if color in all_colors_array:
                match_counter += 1

        if match_counter > 4:
            pic.is_match = True
        else:
            pic.is_match = False
        pic.save()
