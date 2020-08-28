import requests
from apps.colorin.parsing.emoji_dict import emoji_dict
from apps.colorin.palette.get import get_palette
import random
from time import sleep
import tempfile


def get_similar_of_one_color(color):
    T = 10
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


def parse_emoji():
    with open("output.txt", "w") as txt:
        for emoji_name in emoji_dict.keys():
            url = "https://vk.com/images/emoji/" + emoji_name + ".png"
            request = requests.get(url,
                                   headers={'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"},
                                   stream=True)
            sleep(random.randint(1, 9))
            lf = tempfile.NamedTemporaryFile(delete=False, suffix='.png')
            lf.write(request.content)
            palette = get_palette(lf, 2)
            similar_array = get_similar_of_one_color(palette[0])
            emoji_dict[emoji_name] = similar_array

            txt.write(str(emoji_name) + '\n')
            txt.write(str(similar_array) + '\n')

            print(similar_array)

        txt.write(emoji_dict)

    print(emoji_dict)


def add_emoji(request):
    pass
