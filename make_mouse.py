from sympy import Point, Line, Ellipse

def make_mouse():
    fill_color = "#d8d8d8"
    stroke_color = "#939393"
    click_color = "#ed6a6a"
    stroke_width = 2
    
    svg_height = 50
    precision = 1
    
    origin_x = (svg_height * 0.333) + (stroke_width / 2)
    origin_x = round(origin_x, precision)
    
    origin_y = (svg_height / 2) + (stroke_width / 2)
    origin_y = round(origin_y, precision)
    
    radius_x = round(svg_height * 0.333, precision)
    radius_y = round(svg_height / 2, precision)
    
    ellipse = Ellipse(center=(origin_x, origin_y), hradius=radius_x, vradius=radius_y)
    
    h_ratio = 0.333
    
    p1 = Point(0, svg_height * h_ratio)
    p2 = Point(svg_height, svg_height * h_ratio)
    line = Line(p1, p2)
    
    h_line_x1 = round(eval(str(ellipse.intersection(line)[0].x)), precision)
    h_line_x2 = round(eval(str(ellipse.intersection(line)[1].x)), precision)
    h_width = round(h_line_x2 - h_line_x1, precision)
    
    wheel_ratio = 0.165
    
    wheel_origin_x = origin_x + (stroke_width / 2)
    wheel_origin_y = round(svg_height * wheel_ratio, precision)
    wheel_radius_y = round(svg_height / 10, precision)
    wheel_radius_x = round(svg_height / 20, precision)
    
    red_width = round(wheel_origin_x - (stroke_width / 2), precision)
    red_height = round(svg_height * h_ratio, precision)
    
    svg = [
        '<svg width="100px" height="100px" xmlns="http://www.w3.org/2000/svg">',
        '    <g transform="translate(10, 10)">',
        '    <ellipse cx="' + str(origin_x) + '" cy="' + str(origin_y) + '" rx="' + str(radius_x) + '" ry="' + str(radius_y) + '" fill="' + fill_color + '" stroke="' + stroke_color + '" stroke-width="' + str(stroke_width) + '"/>',
        '    <rect x="' + str(h_line_x1) + '" y="' + str(round(svg_height * h_ratio, precision)) + '" width="' + str(h_width) + '" height="' + str(stroke_width) + '" fill="' + stroke_color + '"/>',
        '    <rect x="' + str(origin_x) + '" y="' + str(round(stroke_width / 2, precision)) + '" width="' + str(stroke_width) + '" height="' + str(round(svg_height * h_ratio, precision)) + '" fill="' + stroke_color + '"/>',
        '    <clipPath id="clickMB">',
        '        <ellipse cx="' + str(origin_x) + '" cy="' + str(origin_y) + '" rx="' + str(radius_x - stroke_width / 2) + '" ry="' + str(radius_y - stroke_width / 2) + '" fill="#000000"/>',
        '    </clipPath>',
        #'    <rect width="' + str(red_width) + '" height="' + str(red_height) + '" fill="' + click_color + '" clip-path="url(#clickMB)"/>',
        '    <rect x="' + str(red_width + stroke_width) + '" width="' + str(red_width) + '" height="' + str(red_height) + '" fill="' + click_color + '" clip-path="url(#clickMB)"/>',
        '    <ellipse cx="' + str(wheel_origin_x) + '" cy="' + str(wheel_origin_y) + '" rx="' + str(wheel_radius_x) + '" ry="' + str(wheel_radius_y) + '" fill="' + stroke_color + '" stroke="' + stroke_color + '" stroke-width="' + str(stroke_width) + '"/>',
        '    </g>',
        '</svg>'
    ]
    
    return '\n'.join(svg)

svg = make_mouse()
with open('mouse.svg', 'w') as f:
    f.write(svg)
