import math

block1_mass = 1
block2_mass = 100

block1_size = 50
block2_size = block1_size*(1+math.log10(block2_mass/block1_mass)/8)

block_y = 200
border_align = 15

line_size = 10

grey = (90, 90, 90)
black = (0, 0, 0)
line_color = (30, 30, 30)
white = (255, 255, 255)

FPS = 0
screen_height = 400
screen_weight = 900
