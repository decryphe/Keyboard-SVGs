import os
from PIL import Image, ImageDraw, ImageFont

from utils import autocrop_alpha

words = {
    "A": "A",
    "B": "B",
    "C": "C",
    "D": "D",
    "E": "E",
    "F": "F",
    "G": "G",
    "H": "H",
    "I": "I",
    "J": "J",
    "K": "K",
    "L": "L",
    "M": "M",
    "N": "N",
    "O": "O",
    "P": "P",
    "Q": "Q",
    "R": "R",
    "S": "S",
    "T": "T",
    "U": "U",
    "V": "V",
    "W": "W",
    "X": "X",
    "Y": "Y",
    "Z": "Z",
    "SHIFT": "Shift",
    "CTRL": "Ctrl",
    "ALT": "Alt",
    "ZERO": "0",
    "ONE": "1",
    "TWO": "2",
    "THREE": "3",
    "FOUR": "4",
    "FIVE": "5",
    "SIX": "6",
    "SEVEN": "7",
    "EIGHT": "8",
    "NINE": "9",
    "LEFT_CTRL": "l Ctrl",
    "LEFT_ALT": "l Alt",
    "LEFT_SHIFT": "l Shift",
    "RIGHT_ALT": "r Alt",
    "RIGHT_SHIFT": "r Shift",
    "RIGHT_CTRL": "r Ctrl",
    "OSKEY": "OS Key",
    "ESC": "Esc",
    "TAB": "Tab",
    "RET": "Return",
    "SPACE": "Spacebar",
    "LINE_FEED": "Enter", # Not too sure about this one...
    "BACK_SPACE": "Backspace",
    "DEL": "Del",
    "SEMI_COLON": ";",
    "PERIOD": ".",
    "COMMA": ",",
    "QUOTE": '"',
    "ACCENT_GRAVE": "`",
    "MINUS": "-",
    "SLASH": "/",
    "BACK_SLASH": "\\",
    "EQUAL": "=",
    "PLUS": "+",
    "MINUS": "-",
    "LEFT_BRACKET": "[",
    "RIGHT_BRACKET": "]",
    "LEFT_ARROW": "Left",
    "DOWN_ARROW": "Down",
    "RIGHT_ARROW": "Right",
    "UP_ARROW": "Up",
    "NUMPAD_1": "Numpad 1",
    "NUMPAD_2": "Numpad 2",
    "NUMPAD_3": "Numpad 3",
    "NUMPAD_4": "Numpad 4",
    "NUMPAD_5": "Numpad 5",
    "NUMPAD_6": "Numpad 6",
    "NUMPAD_7": "Numpad 7",
    "NUMPAD_8": "Numpad 8",
    "NUMPAD_9": "Numpad 9",
    "NUMPAD_PERIOD": "Numpad .",
    "NUMPAD_SLASH": "Numpad /",
    "NUMPAD_ASTERIX": "Numpad *",
    "NUMPAD_MINUS": "Numpad -",
    "NUMPAD_PLUS": "Numpad +",
    "NUMPAD_ENTER": "Numpad Enter",
    "F1": "F1",
    "F2": "F2",
    "F3": "F3",
    "F4": "F4",
    "F5": "F5",
    "F6": "F6",
    "F7": "F7",
    "F8": "F8",
    "F9": "F9",
    "F10": "F10",
    "F11": "F11",
    "F12": "F12",
    "F13": "F13",
    "F14": "F14",
    "F15": "F15",
    "F16": "F16",
    "F17": "F17",
    "F18": "F18",
    "F19": "F19",
    #"Pause", "||", Do something else here
    "INSERT": "Insert",
    "HOME": "Home",
    "PAGE_UP": "PgUp",
    "PAGE_DOWN": "PgDown",
    "END": "End",
    "LEFTMOUSE": "LMB",
    "RIGHTMOUSE": "RMB",
    "MIDDLEMOUSE": "MMB",
    "ACTIONMOUSE": "LMB",
    "SELECTMOUSE": "RMB",
}

font_path = 'courierbd.ttf'
font_size = 18
font = ImageFont.truetype(font_path, font_size)

padding = 3
stroke_width = 1
shadow_width = 3

for key in words.keys():

    size = font.getsize(words[key])

    img = Image.new("RGBA", size)

    draw = ImageDraw.Draw(img)
    x = 0
    y = 0
    color = "#4d4d4d"
    draw.text((x, y), words[key], fill=color, font=font)

    img = autocrop_alpha(img)

    width = font_size
    if len(words[key]) > 1:
        width = img.size[0] + (padding * 2)
    height = font_size

    bg = Image.new("RGB", (width + padding * 2, height + padding * 2), "#d8d8d8")
    loc_x = int((bg.size[0] - img.size[0]) / 2) + int((shadow_width) / 2)
    loc_y = int((bg.size[1] - img.size[1]) / 2)

    bg.paste(img, (loc_x, loc_y), mask=img.split()[3])

    img_width = stroke_width + bg.size[0] + shadow_width
    img_height = stroke_width + bg.size[1] + shadow_width

    shadow = Image.new("RGB", (img_width, img_height), "#939393")
    shadow.paste(bg, (stroke_width, stroke_width))

    shadow.save(os.path.join(os.getcwd(), 'images', key + '.png'))
