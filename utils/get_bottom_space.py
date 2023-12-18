import os
from PIL import Image, ImageDraw, ImageFont
from .get_string_size import get_string_size

def get_bottom_space(string, font_size):
    """
    Because the bottom of "A" marks the 0 line, get the distance
    between the bottom of the string and the bottom of "A"
    """

    font_path = os.path.join(os.path.dirname(__file__), 'courierbd.ttf')
    font = ImageFont.truetype(font_path, font_size)

    standard_width, null = get_string_size("M", font_size)
    null, standard_height = get_string_size("[", font_size)

    size = font.getsize(string + 'A')

    img = Image.new("RGBA", size)

    draw = ImageDraw.Draw(img)
    x = 0
    y = 0
    color = (0, 0, 0, 255)
    draw.text((x, y), string + "A", fill=color, font=font)

    img.save('temp.png')

    diff_y = img.size[1] - standard_height

    pixdata = img.load()

    y_start = -1
    y = img.size[1] - 1
    while y > diff_y and y_start == -1:
        for x in range(img.size[0] - standard_width, img.size[0]):
            if pixdata[x, y][-1] != 0:
                y_start = y
                break
        y -= 1
    return img.size[1] - y_start - 1