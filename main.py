import logging
from typing import Literal, Union
from networktables import NetworkTables
from constants import *
from auto_chooser import *
from text_engine import *
from polygon import Polygon

import pygame

pygame.init()

gameDisplay = pygame.display.set_mode(
    (display_width, display_height))

pygame.display.set_caption('Treble Display')
clock = pygame.time.Clock()

background_color = white

auto_chooser_grid = getAutoChooserGrid(gameDisplay)

polygons = [
    Polygon(chassis_polygon_one, chassis_color, gameDisplay,
            scale=pixels_per_inch, pivot=arm_pivot), 
    Polygon(chassis_polygon_two, chassis_color, gameDisplay,
            scale=pixels_per_inch), 
    Polygon(chassis_polygon_three, chassis_color, gameDisplay,
            scale=pixels_per_inch), 
    
    Polygon(intake_polygon_one, active_intake_color, gameDisplay,
            scale=pixels_per_inch), 
    Polygon(intake_polygon_two, active_intake_color, gameDisplay,
            scale=pixels_per_inch), 
    
    Polygon(outtake_polygon_one, outtake_color, gameDisplay, 
            scale=pixels_per_inch, pivot=text_location), 
    Polygon(outtake_polygon_two, outtake_color, gameDisplay, 
            scale=pixels_per_inch), 
    Polygon(outtake_polygon_three, outtake_color, gameDisplay, 
            scale=pixels_per_inch), 
    
    Polygon(conveyor_polygon_one, active_conveyor_color, gameDisplay,
            scale=pixels_per_inch), 
    Polygon(conveyor_polygon_two, active_conveyor_color, gameDisplay,
            scale=pixels_per_inch), 
    
    Polygon(flywheel_polygon_one, active_flywheel_color, gameDisplay,
            scale=pixels_per_inch), 
    Polygon(flywheel_polygon_two, active_flywheel_color, gameDisplay,
            scale=pixels_per_inch),
]


def draw_polygon_alpha(color, points):
    lx, ly = zip(*points)
    min_x, min_y, max_x, max_y = min(lx), min(ly), max(lx), max(ly)
    target_rect = pygame.Rect(min_x, min_y, max_x - min_x, max_y - min_y)
    shape_surf = pygame.Surface(target_rect.size, pygame.SRCALPHA)
    pygame.draw.polygon(shape_surf, color, [
                        (x - min_x, y - min_y) for x, y in points])
    gameDisplay.blit(shape_surf, target_rect)


def drawPolygons(pos, current_angle, target_angle, intake_active, conveyor_active, flywheel_active, text_engine): # assuming angle is in degrees
    
    for i in range(5):
        polygons[i].rotateTo(0)
        polygons[i].setPos(pos)
        polygons[i].update_hitbox()

    for i in range(5, 12):
        polygons[i].rotateTo(current_angle)
        polygons[i].setPos(polygons[0].pivotPoint)
        polygons[i].update_hitbox()

    polygons[5].rotateTo(target_angle)
    polygons[5].update_hitbox()
    
    draw_polygon_alpha(outtake_target_color, polygons[5].hitbox)
    
    polygons[5].rotateTo(current_angle)
    polygons[i].update_hitbox()
    
    for i in range(len(polygons)):
        if (i == 3 or i == 4):
            if intake_active:
                draw_polygon_alpha(polygons[i].color, polygons[i].hitbox)
        elif (i == 8 or i == 9):
            if conveyor_active:
                draw_polygon_alpha(polygons[i].color, polygons[i].hitbox)
        elif (i == 10 or i == 11):
            if flywheel_active:
                draw_polygon_alpha(polygons[i].color, polygons[i].hitbox)
        else:
            polygons[i].draw()
            
    text_engine.type("991", font, polygons[5].pivotPoint, 0.2, 0.2, white, 2, space_between_letters=8, angle=current_angle + text_angle)


def mouse_pos_to_inches(mousePos):
    return (
        (mousePos[0] - polygons[0].pivotPoint[0]) / pixels_per_inch,
        ((gameDisplay.get_height() - mousePos[1]) - polygons[0].pivotPoint[1]) / pixels_per_inch
    )


TE = Text_Engine(gameDisplay)

logging.basicConfig(level=logging.DEBUG)

NetworkTables.initialize(server=robot_ip)  # RoboRio
smartDashboard = NetworkTables.getTable("SmartDashboard")

for i in auto_chooser_grid:
    for j in i:
        j.setPos((0, 0))

mousedownlast = False
mouseclicked = False

indices = [0, 0, 0]

run = True

while run:
    
    mouseclicked = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseclicked = not mousedownlast
            mousedownlast = True
        if event.type == pygame.MOUSEBUTTONUP:
            mouseclicked = False
            mousedownlast = False

    gameDisplay.fill(background_color)
    
    # double arm
    
    pygame.draw.rect(gameDisplay, green, (selector_width, int(
        display_height * 0.9), display_width, display_height))
    
    current_angle = smartDashboard.getNumber("Current Angle", 991)
    
    if current_angle == 991:
        if pygame.mouse.get_pos()[0] > selector_width:
            mouse_pos = mouse_pos_to_inches(pygame.mouse.get_pos())
            if math.sqrt(mouse_pos[0] * mouse_pos[0] + mouse_pos[1] * mouse_pos[1]) > 2.5468175:
                current_angle = (math.atan2(mouse_pos_to_inches(pygame.mouse.get_pos())[1], mouse_pos_to_inches(pygame.mouse.get_pos())[0]) + 
                                math.asin(2.5468175 / math.sqrt(mouse_pos[0] * mouse_pos[0] + mouse_pos[1] * mouse_pos[1]))) * 180.0 / math.pi
            else:
                current_angle = 59.006106
        else:
            current_angle = 59.006106
    
    target_angle = smartDashboard.getNumber("Target 1st Angle", -9.751102)
    
    intake_state = smartDashboard.getString("intake state", "disconnected")
    conveyor_state = smartDashboard.getString("conveyor state", "disconnected")
    flywheel_stake = smartDashboard.getString("flywheel state", "disconnected")
    
    drawPolygons(
        (selector_width + (display_width - selector_width - 38 * pixels_per_inch) * 0.5, display_height * 0.1),
        current_angle, 
        target_angle, 
        intake_state != "off", 
        conveyor_state != "off", 
        flywheel_stake != "off", 
        TE
    )

    if (intake_state != "disconnected"):
        TE.type("current angle is " + str(round(current_angle, 1)), font, (selector_width + int((display_width - selector_width) * 0.5), int(
            display_height * 7.0 / 8.0)), 0.01 * display_height / 16.0, 0.01 * display_height / 16.0, black, 2, space_between_letters=display_height / 96.0)
        
        TE.type("target angle is " + str(round(target_angle, 1)), font, (selector_width + int((display_width - selector_width) * 0.5), int(
            display_height * 4.0 / 5.0)), 0.01 * display_height / 16.0, 0.01 * display_height / 16.0, black, 2, space_between_letters=display_height / 96.0)

    else:  # no reading from smartdashboard
        TE.type("could not connect to robot", font, (selector_width + int((display_width - selector_width) * 0.5), int(
            display_height * 7.0 / 8.0)), 0.01 * display_height / 16.0, 0.01 * display_height / 16.0, black, 2, space_between_letters=display_height / 96.0)
    
    # auto selector
    original_indices = indices.copy()

    for i in range(1, len(auto_chooser_grid)):
        for j in range(len(auto_chooser_grid[i])):
            if (mouseclicked):
                if ((auto_chooser_grid[i][j].hitbox[0][0] < pygame.mouse.get_pos()[0]) == (pygame.mouse.get_pos()[0] < auto_chooser_grid[i][j].hitbox[2][0])):
                    if ((auto_chooser_grid[i][j].hitbox[0][1] < pygame.mouse.get_pos()[1]) == (pygame.mouse.get_pos()[1] < auto_chooser_grid[i][j].hitbox[2][1])):
                        indices[i - 1] = j
    
    # no overrides yet :)

    for i in range(len(auto_chooser_grid)):
        if (i != 0):
            title_x = 0
            if i == 1:
                title_x = first_title_x
            if i == 2:
                title_x = second_title_x
            if i == 3:
                title_x = third_title_x
            TE.type(categories[i - 1], font, (title_x, title_height), 0.25, 0.25, white, 2, space_between_letters=6)
            
        for j in range(len(auto_chooser_grid[i])):
            temp = auto_chooser_grid[i][j].color
            if (i != 0 and indices[i - 1] != j):
                auto_chooser_grid[i][j].color = gray
            
            auto_chooser_grid[i][j].draw()
            auto_chooser_grid[i][j].color = temp
            if (i != 0):
                TE.type(auto_chooser_grid[i][j].name, font, (auto_chooser_grid[i]
                        [j].pivotPoint[0], auto_chooser_grid[i][j].pivotPoint[1] - 12.5), 
                        0.25, 0.25, black, 2, space_between_letters=6)

    TE.type("team 991", font, (277, 453), 1.2, 1.2,
            black, 6, space_between_letters=12)
    TE.type("knew it was treble", font, (520, 406), 0.4,
            0.4, black, 2, space_between_letters=6)
    
    smartDashboard.putNumberArray("Auto Data", indices)
    # print(indices)

    pygame.display.update()
    clock.tick(10)

pygame.quit()
