import requests
from apps.colorin.parsing.emoji_list import emoji_list
from apps.colorin.palette.get import get_palette
from apps.colorin.models import EmojiPic
import random
from time import sleep
import tempfile


def add_emoji(request):
    for emoji_name in emoji_list:
        url = "https://vk.com/images/emoji/" + emoji_name + ".png"
        request = requests.get(url,
                               headers={'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"},
                               stream=True)
        sleep(random.randint(1, 9))
        lf = tempfile.NamedTemporaryFile(delete=False, suffix='.png')
        lf.write(request.content)
        palette = get_palette(lf, 4)
        emoji = EmojiPic(emoji_name=emoji_name,
                         palette=palette,)

        emoji.save()
    print("All emoji added successfully ~")
