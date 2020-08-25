import requests
from apps.colorin.parsing.emoji_dict import emoji_dict
from apps.colorin.palette.get import get_palette
from apps.colorin.palette.match import get_similar_of_all_img_colors

for emoji_name in emoji_dict.keys():
    url = "https://vk.com/images/emoji/" + emoji_name + ".png"
    request = requests.get(url,
                           headers={'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"},
                           stream=True)

    lf = tempfile.NamedTemporaryFile(delete=False, suffix='.png')
    f.write(request.content)
    palette = get_palette(lf, 2)
    similar_array = get_similar_of_all_img_colors(palette)
    emoji_dict[emoji_name] = similar_array

print(emoji_dict)
