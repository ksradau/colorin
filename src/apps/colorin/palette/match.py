from django.contrib.auth import get_user_model
from apps.colorin.models import InstagramPhoto, InstagramProfile


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


def get_similar_of_all_profile(img_similar):
    _all_colors = []
    for  in img_similar:
        _all_colors += color_array
    return _all_colors

for img in test_uploaded_list:
    match_counter = 0
    for palette in img:
        if palette in _all:
            match_counter += 1
            print("~~~ It's a MATCH !!!")
        else:
            print("~~~ Oh no")
    print("~~~ Num of matches in img:")
    print(match_counter)