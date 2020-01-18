import math
import random
import pygame
from pygame import mixer
import pygame.freetype
from pygame.sprite import Sprite
from pygame.rect import Rect
from enum import Enum

BLUE = (106, 159, 181)
WHITE = (255, 255, 255)

n = 1
while n<(n+2):
    def create_surface_with_text(text, font_size, text_rgb, bg_rgb):
        """ Returns surface with text written on """
        font = pygame.freetype.SysFont("Courier", font_size, bold=True)
        surface, _ = font.render(text=text, fgcolor=text_rgb, bgcolor=bg_rgb)
        return surface.convert_alpha()


    class UIElement(Sprite):
        """ An user interface element that can be added to a surface """

        def __init__(self, center_position, text, font_size, bg_rgb, text_rgb, action=None):
            """
            Args:
                center_position - tuple (x, y)
                text - string of text to write
                font_size - int
                bg_rgb (background colour) - tuple (r, g, b)
                text_rgb (text colour) - tuple (r, g, b)
                action - the gamestate change associated with this button
            """
            self.mouse_over = False

            default_image = create_surface_with_text(
                text=text, font_size=font_size, text_rgb=text_rgb, bg_rgb=bg_rgb
            )

            highlighted_image = create_surface_with_text(
                text=text, font_size=font_size * 1.2, text_rgb=text_rgb, bg_rgb=bg_rgb
            )

            self.images = [default_image, highlighted_image]

            self.rects = [
                default_image.get_rect(center=center_position),
                highlighted_image.get_rect(center=center_position),
            ]

            self.action = action

            super().__init__()

        @property
        def image(self):
            return self.images[1] if self.mouse_over else self.images[0]

        @property
        def rect(self):
            return self.rects[1] if self.mouse_over else self.rects[0]

        def update(self, mouse_pos, mouse_up):
            """ Updates the mouse_over variable and returns the button's
                action value when clicked.
            """
            if self.rect.collidepoint(mouse_pos):
                self.mouse_over = True
                if mouse_up:
                    return self.action
            else:
                self.mouse_over = False

        def draw(self, surface):
            """ Draws element onto a surface """
            surface.blit(self.image, self.rect)


    def main():
        pygame.init()

        screen = pygame.display.set_mode((800, 600))
        game_state = GameState.TITLE

        while True:
            if game_state == GameState.TITLE:
                game_state = title_screen(screen)

            if game_state == GameState.NEWGAME:
                game_state = play_level(screen)

            if game_state == GameState.QUIT:
                pygame.quit()
                return


    def title_screen(screen):
        start_btn = UIElement(
            center_position=(400, 500),
            font_size=30,
            bg_rgb=BLUE,
            text_rgb=WHITE,
            text="Quit",
            action=GameState.NEWGAME,
        )
        quit_btn = UIElement(
            center_position=(400, 400),
            font_size=30,
            bg_rgb=BLUE,
            text_rgb=WHITE,
            text="Start",
            action=GameState.QUIT,
        )

        buttons = [start_btn, quit_btn]

        while True:
            mouse_up = False
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    mouse_up = True
            screen.fill(BLUE)

            for button in buttons:
                ui_action = button.update(pygame.mouse.get_pos(), mouse_up)
                if ui_action is not None:
                    return ui_action
                button.draw(screen)

            pygame.display.flip()

    def play_level(screen):
        pygame.quit()
        

        while True:
            mouse_up = False
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    mouse_up = True
            screen.fill(BLUE)

            ui_action = return_btn.update(pygame.mouse.get_pos(), mouse_up)
            if ui_action is not None:
                return ui_action
            return_btn.draw(screen)

            pygame.display.flip()


    class GameState(Enum):
        QUIT = -1
        TITLE = 0
        NEWGAME = 1


    if __name__ == "__main__":
        main()


    background = pygame.image.load('background.png')

    pygame.init()

    screen = pygame.display.set_mode((800, 600))

    mixer.music.load("background.wav")
    mixer.music.play(-1)


    pygame.display.set_caption("Space Invader")
    icon = pygame.image.load('ufo.png')
    pygame.display.set_icon(icon)


    playerImg = pygame.image.load('player.png')
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
        enemyImg.append(pygame.image.load('enemy.png'))
        enemyX.append(random.randint(0, 736))
        enemyY.append(random.randint(50, 150))
        enemyX_change.append(4)
        enemyY_change.append(40)



    bulletImg = pygame.image.load('bullet.png')
    bulletX = 0
    bulletY = 480
    bulletX_change = 0
    bulletY_change = 10
    bullet_state = "ready"



    score_value = 0
    font = pygame.font.Font('freesansbold.ttf', 32)

    textX = 10
    testY = 10


    over_font = pygame.font.Font('freesansbold.ttf', 64)


    def show_score(x, y):
        score = font.render("Score : " + str(score_value), True, (255, 255, 255))
        screen.blit(score, (x, y))


    def game_over_text():
        over_text = over_font.render("GAME OVER", True, (255, 255, 255))
        screen.blit(over_text, (200, 250))
        pygame.quit()
        return


    def player(x, y):
        screen.blit(playerImg, (x, y))


    def enemy(x, y, i):
        screen.blit(enemyImg[i], (x, y))


    def fire_bullet(x, y):
        global bullet_state
        bullet_state = "fire"
        screen.blit(bulletImg, (x + 16, y + 10))


    def isCollision(enemyX, enemyY, bulletX, bulletY):
        distance = math.sqrt(math.pow(enemyX - bulletX, 2) + (math.pow(enemyY - bulletY, 2)))
        if distance < 27:
            return True
        else:
            return False



    running = True
    while running:

        
        screen.fill((0, 0, 0))
        
        screen.blit(background, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    playerX_change = -5
                if event.key == pygame.K_RIGHT:
                    playerX_change = 5
                if event.key == pygame.K_SPACE:
                    if bullet_state is "ready":
                        bulletSound = mixer.Sound("laser.wav")
                        bulletSound.play()
                        
                        bulletX = playerX
                        fire_bullet(bulletX, bulletY)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    playerX_change = 0


        playerX += playerX_change
        if playerX <= 0:
            playerX = 0
        elif playerX >= 736:
            playerX = 736

        
        for i in range(num_of_enemies):

            
            if enemyY[i] > 440:
                for j in range(num_of_enemies):
                    enemyY[j] = 2000
                game_over_text()
                break

            enemyX[i] += enemyX_change[i]
            if enemyX[i] <= 0:
                enemyX_change[i] = 4
                enemyY[i] += enemyY_change[i]
            elif enemyX[i] >= 736:
                enemyX_change[i] = -4
                enemyY[i] += enemyY_change[i]

           
            collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
            if collision:
                explosionSound = mixer.Sound("explosion.wav")
                explosionSound.play()
                bulletY = 480
                bullet_state = "ready"
                score_value += 1
                enemyX[i] = random.randint(0, 736)
                enemyY[i] = random.randint(50, 150)

            enemy(enemyX[i], enemyY[i], i)

        
        if bulletY <= 0:
            bulletY = 480
            bullet_state = "ready"

        if bullet_state is "fire":
            fire_bullet(bulletX, bulletY)
            bulletY -= bulletY_change
        player(playerX, playerY)
        show_score(textX, testY)
        pygame.display.update()

        n = n + 1
    
