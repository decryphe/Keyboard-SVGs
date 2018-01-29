import os
from PIL import Image, ImageDraw, ImageFont


def get_string_size(string, fontsize):
    font_path = os.path.join(os.path.dirname(__file__), 'courierbd.ttf')
    font = ImageFont.truetype(font_path, fontsize)

    size = font.getsize(string)

    #img_path = os.path.join(os.path.expanduser('~'), 'img.png')

    img = Image.new("RGBA", size)

    size = [size[0], 0]

    draw = ImageDraw.Draw(img)
    x = 0
    y = 0
    color = (0, 0, 0, 255)
    draw.text((x, y), string, fill=color, font=font)

    pixdata = img.load()

    # WIDTH #
    x_start = -1
    x = 0
    while x < img.size[0] and x_start == -1:
        for y in range(img.size[1]):
            if pixdata[x, y][-1] != 0:
                x_start = x
                break
        x += 1

    x_end = -1
    x = img.size[0] - 1
    while x > 1 and x_end == -1:
        for y in range(img.size[1]):
            if pixdata[x, y][-1] != 0:
                x_end = x
                break
        x -= 1

    #size[0] = x_end - x_start

    # HEIGHT #
    y_start = -1
    y = 0
    while y < img.size[1] and y_start == -1:
        for x in range(img.size[0]):
            if pixdata[x, y][-1] != 0:
                y_start = y
                break
        y += 1

    y_end = -1
    y = img.size[1] - 1
    while y > 1 and y_end == -1:
        for x in range(img.size[0]):
            if pixdata[x, y][-1] != 0:
                y_end = y
                break
        y -= 1

    size[1] = y_end - y_start

    return size