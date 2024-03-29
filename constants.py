display_width = 1440
display_height = 531

selector_width = 720
selector_height = 340

internal_border = 15

main_border = 20
top_border = 50

pixels_per_inch = (display_width - selector_width) * 0.018

robot_ip = "10.9.91.2"

categories = ["place",  "path name"]

chassis_polygon_one: list[tuple[float, float]] = [  # in inches
    (0, 4), 
    (0.866025, 2.5), 
    (3.1, 2.5), 
    (3.1, 1.866641), 
    (6.491089, 0.2125), 
    (7.023756, 0.2125), 
    (8.625836, 1.993474), 
    (8.930114, 2.5), 
    (11.647576, 2.5), 
    (11.344466, 1.975), 
    (12.484733, 0), 
    (14.765267, 0), 
    (15.905534, 1.975), 
    (15.602424, 2.5), 
    (19, 2.5), 
    (19, 1.5), 
    (30.368708, 1.5), 
    (31.234733, 0), 
    (33.515267, 0), 
    (34.381292, 1.5), 
    (37.133975, 1.5), 
    (38, 3), 
    (38, 5), 
    (37.133975, 6.5), 
    (35, 6.5), 
    (35, 24.039724), 
    (34, 24.039724), 
    (34, 6.5), 
    (19, 6.5), 
    (19, 7.5), 
    (11.991552, 7.5), 
    (11.991552, 8.576433), 
    (8.819839, 10.481730), 
    (7, 11.039724), 
    (3, 11.039724), 
    (3, 7.5), 
    (0.866025, 7.5), 
    (0, 6)
]

chassis_polygon_two: list[tuple[float, float]] = [
    (30.125, 16.039724), 
    (30.125, 18.039724), 
    (29.125, 18.039724), 
    (29.125, 16.039724)
]

chassis_polygon_three: list[tuple[float, float]] = [
    (9, 25.039724), 
    (9, 26.039724), 
    (7, 26.039724), 
    (7, 25.039724)
]

intake_polygon_one: list[tuple[float, float]] = [
    (3.702177, 2.657290), 
    (3.802427, 2.255391), 
    (4.157500, 2.042093), 
    (4.559399, 2.142343), 
    (8.878367, 9.332049), 
    (8.778117, 9.733948), 
    (8.423044, 9.947246), 
    (8.021145, 9.846996)
]

intake_polygon_two: list[tuple[float, float]] = [
    (6.137657, 1.079937), 
    (6.237907, 0.678038), 
    (6.592980, 0.464740), 
    (6.994879, 0.564990), 
    (11.364312, 7.838703), 
    (11.264062, 8.240602), 
    (10.908988, 8.453900), 
    (10.507089, 8.353650)
]

arm_pivot: tuple[float, float] = (15.25, 23.039724)

outtake_polygon_one: list[tuple[float, float]] = [
    (-11.558452, 1.587424), 
    (-11.558452, -5.069038), 
    (-11.210389, -7.094411), 
    (10.171953, -6.259489), 
    (10.709282, -6.796817), 
    (12.159029, -6.796817), 
    (13.184155, -5.771691), 
    (13.184155, -4.515886), 
    (14.468337, -2.586893), 
    (15.506940, -2.408408), 
    (17.969281, 3.545375), 
    (16.551320, 6.616052), 
    (7.208200, 5.010425), 
    (6.025941, 3.335317), 
    (-6.497155, 0.912774), 
    (-8.534283, 0.562691), 
    (-10.110228, 2.177097)
]

outtake_polygon_two: list[tuple[float, float]] = [
    (-9.123314, -0.561303), 
    (-9.407722, -0.845711), 
    (-9.407722, -1.247924), 
    (-9.123314, -1.532332), 
    (2.384817, -1.532332), 
    (2.669224, -1.247924), 
    (2.669224, -0.845711), 
    (2.384817, -0.561303)
]

outtake_polygon_three: list[tuple[float, float]] = [
    (-9.123314, -3.561303), 
    (-9.407722, -3.845711), 
    (-9.407722, -4.247924), 
    (-9.123314, -4.532332), 
    (2.384817, -4.532332), 
    (2.669224, -4.247924), 
    (2.669224, -3.845711), 
    (2.384817, -3.561303)
]

conveyor_polygon_one: list[tuple[float, float]] = [
    (-9.149202, -0.498803), 
    (-9.470222, -0.819822), 
    (-9.470222, -1.273813), 
    (-9.149202, -1.594832), 
    (2.410705, -1.594832), 
    (2.731724, -1.273813), 
    (2.731724, -0.819822),  
    (2.410705, -0.498803)
]

conveyor_polygon_two: list[tuple[float, float]] = [
    (-9.149202, -3.498803), 
    (-9.470222, -3.819822), 
    (-9.470222, -4.273813), 
    (-9.149202, -4.594832), 
    (2.410705, -4.594832), 
    (2.731724, -4.273813), 
    (2.731724, -3.819822),  
    (2.410705, -3.498803)
]

flywheel_polygon_one: list[tuple[float, float]] = [
    (4.713957, 0.703183), 
    (3.981724, -0.029051), 
    (3.981724, -1.064584), 
    (4.713957, -1.796817), 
    (12.159029, -1.796817), 
    (13.184155, -0.771691), 
    (13.184155, 0.678056), 
    (12.159029, 1.703183), 
    (10.709282, 1.703183), 
    (9.709282, 0.703183)
]

flywheel_polygon_two: list[tuple[float, float]] = [
    (4.713957, -3.296817), 
    (3.981724, -4.029051), 
    (3.981724, -5.064584), 
    (4.713957, -5.796817), 
    (9.709282, -5.796817), 
    (10.709282, -6.796817), 
    (12.159029, -6.796817), 
    (13.184155, -5.771691), 
    (13.184155, -4.321944), 
    (12.159029, -3.296817)
]

text_location: tuple[float, float] = (12.126048, 3.191588)

text_angle: float = 9.751102

black = (0, 0, 0)
white = (234, 234, 234)
gray = (128, 128, 128)
darker_gray = (85, 85, 85)
lighter_gray = (170, 170, 170)

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

clear_darker_gray = (85, 85, 85, 128)
clear_lighter_gray = (170, 170, 170, 128)

clear_red = (255, 0, 0, 170)
clear_green = (0, 255, 0, 170)
clear_blue = (0, 0, 255, 170)

orange = (255, 128, 0)
yellow = (255, 255, 0)
lime = (128, 255, 0)
purple = (255, 0, 255)

clear_orange = (255, 128, 0, 170)

chassis_color = darker_gray
outtake_color = lighter_gray

active_intake_color = clear_blue
active_conveyor_color = clear_orange
active_flywheel_color = clear_red
outtake_target_color = clear_lighter_gray