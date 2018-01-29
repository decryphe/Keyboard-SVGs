from .get_string_size import get_string_size
from .get_top_space import get_top_space
from .get_bottom_space import get_bottom_space

def make_svg(string, font_size):

    standard_width, null = get_string_size("M", font_size)
    null, standard_height = get_string_size("[", font_size)

    text_width, text_height = get_string_size(string, font_size)

    bottom_space = get_bottom_space(string, font_size)
    top_space = get_top_space(string, font_size)

    padding = 5
    precision = 1

    stroke_width = round(font_size / 40, precision)
    shadow_width = round(font_size / 10, precision)

    offset_x = 0
    rect_width = text_width + (padding * 2)
    if rect_width < standard_height + (padding * 2):
        rect_width = standard_height + (padding * 2)
    rect_height = standard_height + (padding * 2)

    svg_width = rect_width + shadow_width
    svg_height = rect_height + shadow_width

    x = (rect_width + shadow_width) - ((rect_width + shadow_width) / 2) - (text_width / 2) + (shadow_width / 4)
    x = round(x, precision)
    y = svg_height - bottom_space - (svg_height / 2) + (text_height / 2) + top_space - stroke_width
    y = round(y, precision)

    if int(x) == x:
        x = int(x)
    if int(y) == y:
        y = int(y)

    svg = [
        '<svg xmlns="http://www.w3.org/2000/svg">',
        '    <rect width="' + str(svg_width) + 'px" height="' + str(svg_height) + 'px" fill="#939393"/>',
        '    <rect width="' + str(rect_width) + 'px" height="' + str(rect_height) + 'px" fill="#d8d8d8" stroke="#939393" stroke-width="' + str(stroke_width) + 'px"/>',
        '    <text fill="#4d4d4d" x="' + str(x) + 'px" y="' + str(y) + 'px" font-size="' + str(font_size) + 'px" font-family="Courier" font-weight="bold">' + string + '</text>',
        '</svg>'
    ]

    return '\n'.join(svg)


