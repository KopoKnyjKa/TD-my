import Settings
import pygame

path = [(100,0), (100,400), (300,400), (300,150), (500,150)]

def draw_map(surface):
    surface.fill(Settings.GREEN)
    pygame.draw.lines(surface,Settings.BROWN,False,path,Settings.road_width)
    for point in path:
        point=(point[0]+1,point[1]+1)
        pygame.draw.circle(surface,Settings.BROWN,point,Settings.road_width//2,Settings.road_width//2)