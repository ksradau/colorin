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
    T = 20 + 1
    tolerance_list = []
    r, g, b = color[0], color[1], color[2]
    for rn in range(r - T, r + T):
        for gn in range(g - T, g + T):
            for bn in range(b - T, b + T):
                tolerance_list.append((rn, gn, bn,))
    return tolerance_list


test_list_of_inst_colors = get_palette('examples\ex1.jpg', 6)

palette_first_test_uploaded = get_palette('examples\ex2.jpg', 6)
palette_second_test_uploaded = get_palette('examples\ex3.jpg', 6)

test_uploaded_list = palette_first_test_uploaded + palette_second_test_uploaded

similar_array_for_inst_palette = get_similar_array((150, 40, 90))

print(similar_array_for_inst_palette)
