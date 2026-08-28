import pygame
import Enemy
import Settings
import Map
import Tower
pygame.init()
pygame.display.set_caption(Settings.NAME)
surface = pygame.display.set_mode((Settings.WIDTH,Settings.HEIGHT))
clock = pygame.time.Clock()

enemies = []
enemies_queue = 0
towers =[]
bullets = []
def check_collisions(bullet_coord,enemy_coord,bullet_size,enemy_size):
    return Settings.get_distance(bullet_coord, enemy_coord) <= bullet_size + enemy_size

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.unicode == 't':
                enemies_queue += 1
                enemies.append(Enemy.Enemy(enemies_queue))
            if event.unicode == 'q':
                Tower.rad_vision = not Tower.rad_vision
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if Tower.can_build(event.pos,Map.path):
                    towers.append(Tower.Tower(event.pos))
    Map.draw_map(surface)
    enemies = [enemy for enemy in enemies if not enemy.dead]
    for enemy in enemies:
        enemy.update()
        enemy.draw(surface)
    for tower in towers:
        tower.update(enemies, surface)
        tower.draw(surface)
        for bullet in tower.bullets:
            bullet.update(tower.coord, tower.rad_size)
            bullet.draw(surface)
            for enemy in enemies:
                if check_collisions(bullet.coord,enemy.coord,bullet.size,enemy.size):
                    bullet.dead = True
                    enemy.take_damage(bullet.damage)
        tower.bullets = [bullet for bullet in tower.bullets if not bullet.dead]





    pygame.display.flip()
    clock.tick(Settings.FPS)
pygame.quit()








print('Over')