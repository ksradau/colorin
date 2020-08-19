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
    r, g, b = color[0], color[1], color[2]
    for rn, gn, bn in (range(r - T, r + T), range(g - T, g + T), range(b - T, b + T)):
        if 

test_list_of_inst_colors = get_palette('examples/ex1.jpg', 10)

palette_first_test_uploaded = get_palette('examples/ex2.jpg', 10)
palette_second_test_uploaded = get_palette('examples/ex3.jpg', 10)

test_uploaded_list = palette_first_test_uploaded + palette_second_test_uploaded