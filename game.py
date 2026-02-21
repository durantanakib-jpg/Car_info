import pygame
import random

pygame.init()

screen_width = 500
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

player_img = pygame.image.load(r"C:\Users\duran\Downloads\audi-rs6-avant-performance-15-removebg-preview.png")
player_img = pygame.transform.scale(player_img, (90, 180))
player_img = pygame.transform.rotate(player_img, 90)

enemy_img = pygame.image.load(r"C:\Users\duran\Downloads\Screenshot 2025-11-14 191511-Photoroom.png")
enemy_img = pygame.transform.scale(enemy_img, (90, 180))

player_x = screen_width // 2 - 45
player_y = screen_height - 220
player_speed = 6

enemies = []
enemy_speed = 5
spawn_timer = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < screen_width - 90:
        player_x += player_speed

    spawn_timer += 1
    if spawn_timer > 50:
        spawn_timer = 0
        ex = random.randint(0, screen_width - 90)
        ey = -200
        enemies.append([ex, ey])

    for e in enemies:
        e[1] += enemy_speed

    enemies = [e for e in enemies if e[1] < screen_height + 200]

    player_rect = pygame.Rect(player_x, player_y, 90, 180)
    for e in enemies:
        enemy_rect = pygame.Rect(e[0], e[1], 90, 180)
        if player_rect.colliderect(enemy_rect):
            running = False

    screen.fill((50, 50, 50))
    for e in enemies:
        screen.blit(enemy_img, (e[0], e[1]))
    screen.blit(player_img, (player_x, player_y))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
