import math
import random
import pygame
from pygame import mixer

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

background = pygame.image.load("background.png")

mixer.music.load("background.wav")
mixer.music.play(-1)

pygame.display.set_caption("Space Invasion")

icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

playerImg = pygame.image.load("player.png")
playerX = 370
playerY = 480
playerX_change = 0

enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load("enemy.png"))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(4)
    enemyY_change.append(40)

BulletImg = pygame.image.load("bullet.png")
BulletX = 0
BulletY = 480
BulletX_change = 0
BulletY_change = 10
Bullet_state = "ready"

Score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

TestX = 10
TextY = 10

over_font = pygame.font.Font('freesansbold.ttf', 64)

def show_score(x, y):
    score = font.render("Score:" + str(score_value), True, (255, 255, 255))
    screen.blit(over_text(200, 250))

def player(x, y):
    screen.blit(playerImg,(x, y))

def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))
