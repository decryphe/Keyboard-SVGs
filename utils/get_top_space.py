import os
from PIL import Image, ImageDraw, ImageFont
from .get_string_size import get_string_size

def get_top_space(string, font_size):
    """
    Because "]" marks the top line,
    get the top distance between the string and the top of "]"
    """

    font_path = os.path.join(os.path.dirname(__file__), 'courierbd.ttf')
    font = ImageFont.truetype(font_path, font_size)

    standard_width, null = get_string_size("M", font_size)
    null, standard_height = get_string_size("[", font_size)

    size = font.getsize(string + ']')

    img = Image.new("RGBA", size)

    draw = ImageDraw.Draw(img)
    x = 0
    y = 0
    color = (0, 0, 0, 255)
    draw.text((x, y), string, fill=color, font=font)

    diff_y = img.size[1] - standard_height

    pixdata = img.load()

    y_start = -1
    y = diff_y
    while y < img.size[1] and y_start == -1:
        for x in range(img.size[0] - standard_width):
            if pixdata[x, y][-1] != 0:
                y_start = y
                break
        y += 1
    return y_start - diff_y