from colorthief import ColorThief


def get_palette(photo_url, number_of_colors):
    color_thief = ColorThief(photo_url)
    palette = color_thief.get_palette(color_count=number_of_colors, quality=10)
    return palette

    
def get_dominant(photo_url):
    color_thief = ColorThief(photo_url)
    dominant_color = color_thief.get_color(quality=10)
    return dominant_color

"""
number = 6
photo_url = "https://instagram.fmsq3-1.fna.fbcdn.net/v/t51.2885-19/s320x320/45451042_720332371686056_8754489512257650688_n.jpg?_nc_ht=instagram.fmsq3-1.fna.fbcdn.net&_nc_ohc=FcwoxpkoDJIAX9CP6gk&oh=5eb09a60cf2b370458fe7adf3b73f635&oe=5F5F010D"
palette = get_palette(photo_url, number)
dominant = get_dominant(photo_url)
print(palette)
print(dominant)
"""