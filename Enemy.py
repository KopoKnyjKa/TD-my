import pygame
import Settings
import Map
class Enemy:
    def __init__(self,enemies_queue):
        self.coord = pygame.Vector2(Map.path[0])
        self.speed = 0.5
        self.direction = None
        self.size = 10
        self.cur_goal = 1
        self.dead = False
        self.queue = enemies_queue
        self.hp = 1000
        self.spawn_time = 0
    def draw(self,surface):
            pygame.draw.circle(surface, Settings.BLACK, self.coord, self.size, self.size)
    def update(self):
        self.check_hp()
        self.check_goal()
        self.move()
    def check_hp(self):
        if self.hp <= 0 :
            self.dead = True
    def check_goal(self):
        if self.coord[0] == Map.path[self.cur_goal][0] and self.coord[1] == Map.path[self.cur_goal][1]:
            if self.cur_goal==len(Map.path)-1:
                if not self.dead:
                    print('BOOOOM')
                self.dead=True
            if self.cur_goal<len(Map.path)-1:
                self.cur_goal+=1
                self.get_direction()
        if not self.direction:
            self.get_direction()
    def get_direction(self):
            self.direction = pygame.math.Vector2(Map.path[self.cur_goal][0] - self.coord[0],Map.path[self.cur_goal][1] - self.coord[1]).normalize()
    def move(self):
        self.coord += self.direction * self.speed
    def take_damage(self,damage):
        self.hp -= damage

