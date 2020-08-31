from PIL import Image
import requests
from apps.colorin.palette.get import get_palette
import tempfile


def xxx():
    url = "https://s3.amazonaws.com/colorin-bucket/KGM0BCX9.jpg"
    request = requests.get(url,
                           headers={
                               'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"},
                           stream=True)
    lf = tempfile.NamedTemporaryFile(delete=False, suffix='.jpg')
    lf.write(request.content)
    palette = get_palette(lf, 6)
    print(palette)

    for color in palette:
        image = Image.new("RGB", (100, 100), color)
        image.show()


xxx()

