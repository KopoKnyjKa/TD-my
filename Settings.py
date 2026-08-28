import pygame
GREEN = (68,102,42)
BROWN = (188,152,126)
BLACK = (0,0,0)
BLUE = (70,130,180)

FPS = 60
WIDTH = 500
HEIGHT = 500
road_width = 44
def get_distance(start,end):
    start = pygame.math.Vector2(start)
    end = pygame.math.Vector2(end)
    return start.distance_to(end)

NAME = 'TD_start'