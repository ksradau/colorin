from colorthief import ColorThief
from PIL import Image

color_thief = ColorThief("examples\ex1.jpg")

dominant_color = color_thief.get_color(quality=1)
print(dominant_color)
palette = color_thief.get_palette(color_count=10)
print(palette)


img_big = (300, 300)
img_small = (150, 150)

img_dominant = Image.new("RGB", img_big, dominant_color)
img_dominant.show()

for i in palette:
    img = Image.new("RGB", img_small, i)
    img.show()
