import sys
from PIL import Image

images = []
imagesPaths = ["Public/cat1.png", "Public/cat2.png", "Public/cat3.png", "Public/cat4.png"]

for image in imagesPaths:
    image = Image.open(image);
    images.append(image)

images[0].save(
    "Public/cat.gif", save_all=True, append_images=images[1:], duration=200, loop=0
)
