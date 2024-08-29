import numpy as np
import requests, PIL
from PIL import Image, ImageDraw

# pillow______________________
image = Image.open('pic.jpg')
draw = ImageDraw.Draw(image)
w, h = image.size
for x in range(w):
    for y in range(h):
        if x % 2 == 0 and y % 2 == 0:
            draw.point((x, y), (200, 100, 200))
resized_img = image.resize((500, 500))
resized_img.save('resized_image.png')
# ____________________________
# requests____________________
print('requsets: ')
r = requests.get('https://requests.readthedocs.io/en/latest/')
txt = r.text
print(txt[0:50])
# _____________________________
# numpy_______________________
print('________________')
print('numpy: ')
a = np.array(
    [np.arange(1, 101, 10), np.arange(2, 101, 10), np.arange(3, 101, 10), np.arange(4, 101, 10), np.arange(5, 101, 10)])

x = np.hsplit(a, 2)
print(x[0] + x[1])
