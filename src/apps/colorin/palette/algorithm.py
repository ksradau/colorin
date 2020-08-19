from colorthief import ColorThief
from math import sqrt


def get_palette(photo_url, number_of_colors):
    color_thief = ColorThief(photo_url)
    palette = color_thief.get_palette(color_count=number_of_colors, quality=10)
    return palette


def is_similar(rgb1, rgb2):
    rm = 0.5 * (rgb1[0] + rgb2[0])
    d = sum((2 + rm, 4, 3 - rm) * (rgb1 - rgb2) ** 2) ** 0.5
    if d < 20:
        return True
    return False


def get_similar_array(color):
    T = 20
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


test_list_of_inst_colors = get_palette('examples\ex1.jpg', 6)

palette_first_test_uploaded = get_palette('examples\ex2.jpg', 6)
palette_second_test_uploaded = get_palette('examples\ex3.jpg', 6)

test_uploaded_list = [palette_first_test_uploaded, palette_second_test_uploaded]

_all = []
for color in test_list_of_inst_colors:
    similar_array_for_inst_palette = get_similar_array(color)
    _all.append(similar_array_for_inst_palette)

print(_all)

match_counter = 0
for img in test_uploaded_list:
    for palette in img:
        for color in palette:
            if color in _all:
                match_counter += 1
                print("~~~ It's a MATCH !!!")
            else:
                print("~~~ Oh no")
    print("~~~ Num of matches:")
    print(match_counter)
