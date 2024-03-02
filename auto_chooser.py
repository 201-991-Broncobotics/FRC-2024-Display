import math
from constants import *
from polygon import Polygon
from pygame import Surface

''' Categories: 

station: red, blue (2)
place: amp, middle, notamp
number: 1, 2, 3, 4

-> 4 total columns
'''

button_width = (selector_width - 2 * main_border - 3 * internal_border) / 4.0
double_height = (selector_height - main_border - top_border - internal_border) / 2.0
triple_height = (selector_height - main_border - top_border - 2 * internal_border) / 3.0

title_height = (selector_height - top_border / 2.0) - 12.5

first_title_x = main_border + button_width / 2.0
second_title_x = main_border + internal_border + button_width * 3.0 / 2.0
third_title_x = main_border + internal_border * 5.0 / 2.0 + button_width * 3.0

def getAutoChooserGrid(gameDisplay: Surface):
    return [[
        Polygon(
            [[0, 0],
             [selector_width, 0],
             [selector_width, selector_height],
             [0, selector_height]],
            black,
            gameDisplay
        )
    ], [
        Polygon(
            [[main_border, main_border + internal_border + double_height], 
             [main_border + button_width, main_border + internal_border + double_height], 
             [main_border + button_width, main_border + internal_border + double_height * 2], 
             [main_border, main_border + internal_border + double_height * 2]],
            blue,
            gameDisplay,
            pivot=(main_border + button_width / 2.0, main_border + internal_border + double_height * 3.0 / 2.0), 
            name="blue"
        ), 
        Polygon(
            [[main_border, main_border], 
             [main_border + button_width, main_border], 
             [main_border + button_width, main_border + double_height], 
             [main_border, main_border + double_height]],
            red,
            gameDisplay, 
            pivot=(main_border + button_width / 2.0, main_border + double_height / 2.0), 
            name="red"
        )
    ], [
        Polygon(
            [[main_border + internal_border + button_width, main_border + internal_border * 2 + triple_height * 2], 
             [main_border + internal_border + button_width * 2, main_border + internal_border * 2 + triple_height * 2], 
             [main_border + internal_border + button_width * 2, main_border + internal_border * 2 + triple_height * 3], 
             [main_border + internal_border + button_width, main_border + internal_border * 2 + triple_height * 3]],
            orange,
            gameDisplay,
            pivot=(main_border + internal_border + button_width + button_width / 2.0, main_border + internal_border * 2 + triple_height * 5.0 / 2.0), 
            name="amp"
        ), 
        Polygon(
            [[main_border + internal_border + button_width, main_border + internal_border + triple_height], 
             [main_border + internal_border + button_width * 2, main_border + internal_border + triple_height], 
             [main_border + internal_border + button_width * 2, main_border + internal_border + triple_height * 2], 
             [main_border + internal_border + button_width, main_border + internal_border + triple_height * 2]],
            green,
            gameDisplay, 
            pivot=(main_border + internal_border + button_width + button_width / 2.0, main_border + internal_border + triple_height * 3.0 / 2.0), 
            name="middle"
        ), 
        Polygon(
            [[main_border + internal_border + button_width, main_border], 
             [main_border + internal_border + button_width * 2, main_border], 
             [main_border + internal_border + button_width * 2, main_border + triple_height], 
             [main_border + internal_border + button_width, main_border + triple_height]],
            yellow,
            gameDisplay,
            pivot=(main_border + internal_border + button_width + button_width / 2.0, main_border + triple_height / 2.0), 
            name="not amp"
        )
    ], [
        Polygon(
            [[main_border + internal_border * 2 + button_width * 2, main_border + internal_border + double_height], 
             [main_border + internal_border * 2 + button_width * 3, main_border + internal_border + double_height], 
             [main_border + internal_border * 2 + button_width * 3, main_border + internal_border + double_height * 2], 
             [main_border + internal_border * 2 + button_width * 2, main_border + internal_border + double_height * 2]],
            purple,
            gameDisplay,
            pivot=(main_border + internal_border * 2 + button_width * 2 + button_width / 2.0, main_border + internal_border + double_height * 3.0 / 2.0), 
            name="one"
        ),
        Polygon(
            [[main_border + internal_border * 2 + button_width * 2, main_border], 
             [main_border + internal_border * 2 + button_width * 3, main_border], 
             [main_border + internal_border * 2 + button_width * 3, main_border + double_height], 
             [main_border + internal_border * 2 + button_width * 2, main_border + double_height]],
            purple,
            gameDisplay, 
            pivot=(main_border + internal_border * 2 + button_width * 2 + button_width / 2.0, main_border + double_height / 2.0), 
            name="two"
        ),
        Polygon(
            [[main_border + internal_border * 3 + button_width * 3, main_border + internal_border + double_height], 
             [main_border + internal_border * 3 + button_width * 4, main_border + internal_border + double_height], 
             [main_border + internal_border * 3 + button_width * 4, main_border + internal_border + double_height * 2], 
             [main_border + internal_border * 3 + button_width * 3, main_border + internal_border + double_height * 2]],
            purple,
            gameDisplay,
            pivot=(main_border + internal_border * 3 + button_width * 3 + button_width / 2.0, main_border + internal_border + double_height * 3.0 / 2.0), 
            name="three"
        ), 
        Polygon(
            [[main_border + internal_border * 3 + button_width * 3, main_border], 
             [main_border + internal_border * 3 + button_width * 4, main_border], 
             [main_border + internal_border * 3 + button_width * 4, main_border + double_height], 
             [main_border + internal_border * 3 + button_width * 3, main_border + double_height]],
            purple,
            gameDisplay, 
            pivot=(main_border + internal_border * 3 + button_width * 3 + button_width / 2.0, main_border + double_height / 2.0), 
            name="four"
        )
    ]]

# here and below is collision logic

def point_above_line(point, line): # definition of "above": y above line, or if vertical, then x value greater
    # point format: (x, y)
    # line format: [(x1, y1), (x2, y2)]
    if line[0][0] == line[1][0]:
        return point[0] > line[0][0]
    elif point[0] == line[0][0]:
        return point[1] > line[0][1]
    elif point[0] > line[0][0]:
        return (point[1]-line[0][1])/(point[0]-line[0][0]) > (line[1][1]-line[0][1])/(line[1][0]-line[0][0])
    else:
        return (point[1]-line[0][1])/(point[0]-line[0][0]) < (line[1][1]-line[0][1])/(line[1][0]-line[0][0])

def point_on_line(point, line):
    if abs(line[1][0]-line[0][0]) == 0:
        return abs(line[0][0] - point[0]) < 0.01
    elif abs(point[0]-line[0][0]) == 0:
        return False
    else:
        return (point[1]-line[0][1])/(point[0]-line[0][0]) == (line[1][1]-line[0][1])/(line[1][0]-line[0][0])

def intersect(line_1, line_2):
    if (max(line_1[0][0], line_1[1][0]) < min(line_2[0][0], line_2[1][0])) or (min(line_1[0][0], line_1[1][0]) > max(line_2[0][0], line_2[1][0])) or (max(line_1[0][1], line_1[1][1]) < min(line_2[0][1], line_2[1][1])) or (min(line_1[0][1], line_1[1][1]) > max(line_2[0][1], line_2[1][1])):
        return False  # legit zero chance they intersect

    temp_1 = line_1[1][0]
    temp_2 = line_2[1][0]
    if line_1[0][0] == line_1[1][0]:
        temp_1 += 0.01
    if line_2[0][0] == line_2[1][0]:
        temp_2 += 0.01
    lein_1 = [line_1[0], (temp_1, line_1[1][1])]
    lein_2 = [line_2[0], (temp_2, line_2[1][1])]

    if point_on_line(lein_1[0], lein_2) or point_on_line(lein_1[1], lein_2) or point_on_line(lein_2[0], lein_1) or point_on_line(lein_2[1], lein_1):
        return False  # if any of the points are on the line
    else:
        return (point_above_line(lein_1[0], lein_2) != point_above_line(lein_1[1], lein_2)) and (point_above_line(lein_2[0], lein_1) != point_above_line(lein_2[1], lein_1))

# we want the inside-ness to be the same for every line
def point_inside_polygon(point, polygon, accuracy=6):
    # solution - very scuffed - kinda LOLLY - but should work
    min_x = 10000000
    min_y = 10000000
    max_x = -10000000
    max_y = -10000000
    for i in polygon:
        min_x = min(min_x, i[0])
        max_x = max(max_x, i[0])
        min_y = min(min_y, i[1])
        max_y = max(max_y, i[1])
    length = math.sqrt((max_x-min_x)*(max_x-min_x)+(max_y-min_y)*(max_y-min_y))

    for i in range(accuracy):  # go over "accuracy" radial lines
        temp = 0

        # add 1 if intersects line, 0.5 for each endpoint it touches
        for j in range(len(polygon)):
            radial_line = [point, (point[0] + length*math.cos(2*math.pi/accuracy * i),
                                   point[1] + length*math.sin(2*math.pi/accuracy * i))]
            if point_on_line(polygon[j], radial_line):
                temp += 1
            if point_on_line(polygon[(j+1) % len(polygon)], radial_line):
                temp += 1
            if intersect(radial_line,
                         [polygon[j], polygon[(j+1) % len(polygon)]]):
                temp += 2
            # see if the radial line intersects any of the hitbox lines

        if temp % 4 != 2:
            return False
    return True