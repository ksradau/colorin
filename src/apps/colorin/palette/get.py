from colorthief import ColorThief


def get_palette(photo_url, number_of_colors):
    color_thief = ColorThief(photo_url)
    palette = color_thief.get_palette(color_count=number_of_colors, quality=10)
    return palette
