def autocrop_alpha(img):
    pixdata = img.load()

    x_start = -1
    x = 0
    while x < img.size[0] and x_start == -1:
        for y in range(img.size[1]):
            if pixdata[x, y][-1] != 0:
                x_start = x
                break
        x += 1
    left = x_start

    x_end = -1
    x = img.size[0] - 1
    while x > 1 and x_end == -1:
        for y in range(img.size[1]):
            if pixdata[x, y][-1] != 0:
                x_end = x
                break
        x -= 1
    right = x_end

    y_start = -1
    y = 0
    while y < img.size[1] and y_start == -1:
        for x in range(img.size[0]):
            if pixdata[x, y][-1] != 0:
                y_start = y
                break
        y += 1

    top = y_start

    y_end = -1
    y = img.size[1] - 1
    while y > 1 and y_end == -1:
        for x in range(img.size[0]):
            if pixdata[x, y][-1] != 0:
                y_end = y
                break
        y -= 1

    bottom = y_end

    img = img.crop((left, top, right + 1, bottom + 1))

    return img

