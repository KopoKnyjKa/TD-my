import pygame
import Settings
def can_build(pos,path):
    for count in range(len(path)-1):
        if path[count][0]==path[count+1][0]:
            if path[count][0]-15-Settings.road_width//2<pos[0]<path[count][0]+15+Settings.road_width//2 and \
                (path[count][1]-15<pos[1]<path[count+1][1]+15 or path[count+1][1]-15<pos[1]<path[count][1]+15):
                return False
        elif path[count][1]==path[count+1][1]:
            if path[count][1]-15-Settings.road_width//2<pos[1]<path[count][1]+15+Settings.road_width//2 and \
                (path[count][0]-15<pos[0]<path[count+1][0]+15 or path[count+1][0]-15<pos[0]<path[count][0]+15):
                return False
    return True
rad_vision = False
class Tower:
    def __init__(self,cursor):
        self.coord = pygame.Vector2(cursor)
        self.size = 15
        self.rad_size = 100
        self.target = None
        self.bullets = []
        self.reload = 0
    def draw(self, surface):
        pygame.draw.circle(surface,Settings.BLUE, self.coord,self.size,self.size)
        if rad_vision:
            pygame.draw.circle(surface, Settings.BLACK, self.coord, self.rad_size, 2)
    def update(self,enemies,surface):
        self.check_target(enemies)
        self.take_aim(surface)
        self.shoot()
        if self.reload > 0:
            self.reload -= 1
    def check_target(self,enemies):
        if not self.target:
            self.get_target(enemies)
        elif self.target.dead:
            self.get_target(enemies)
        elif Settings.get_distance(self.target.coord,self.coord)>self.rad_size:
            self.get_target(enemies)
    def get_target(self,enemies):
        potential_target = [[enemy.queue, enemy] for enemy in enemies if (Settings.get_distance(enemy.coord,self.coord))<= self.rad_size]
        if potential_target:
            self.target = min(potential_target)[1]
            print('new target', self.target)
        else: self.target = None
    def take_aim(self,surface):
        if self.target:
            pygame.draw.line(surface,Settings.BLACK,self.coord,self.target.coord,1)
    def shoot(self):
        if self.target:
            if self.reload == 0:
                self.bullets.append(Bullet(self.coord,self.target.coord))
                self.reload = 15

class Bullet:
    def __init__(self,tower_coord,target_coord):
        self.coord = tower_coord.copy()
        self.speed = 2
        self.size = 3
        self.direction = (target_coord - self.coord).normalize()
        self.dead = False
        self.damage = 20
    def draw(self,surface):
        pygame.draw.circle(surface,Settings.BLACK,self.coord,self.size,self.size)
    def update(self,tower_coord,rad_size):
        self.move(tower_coord,rad_size)
    def move(self,tower_coord,rad_size):
        self.coord += self.direction * self.speed
        if Settings.get_distance(self.coord,tower_coord)>rad_size:
            self.dead = True