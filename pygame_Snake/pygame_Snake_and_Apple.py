import pygame
from pygame.locals import *
import time
import random

SIZE = 40  # block size 40


# OOP necessary (to be a good programmer)

class Apple:
    def __init__(self, parent_screen):
        self.apple = pygame.image.load('C:/Users/harry/OneDrive/Desktop/apple.jpg').convert()  # apple
        self.parent_screen = parent_screen
        self.x = SIZE * 3  # to align with an apple and snake
        self.y = SIZE * 3

    def draw(self):
        self.parent_screen.blit(self.apple, (self.x, self.y))  # draw an image
        pygame.display.flip()  # uploading the results in your screen (MUST)

    def move(self):  # apple should be located in SIZE unit (random location)
        self.x = random.randint(1, 24) * SIZE  # 25 = 1000/(apple unit)
        self.y = random.randint(1, 19) * SIZE  # 20 = 800/(apple unit)


class Snake:
    def __init__(self, parent_screen, length):
        self.length = length  # snake length
        self.parent_screen = parent_screen
        self.block = pygame.image.load('C:/Users/harry/OneDrive/Desktop/block.jpg').convert()  # block

        self.x = [SIZE] * length
        self.y = [SIZE] * length
        self.direction = 'down'  # first default direction

    def increase_length(self):
        self.length += 1
        self.x.append(-1)  # append new x
        self.y.append(-1)  # append new y

    def draw(self):
        for i in range(self.length):
            self.parent_screen.blit(self.block, (self.x[i], self.y[i]))  # draw blocks
        pygame.display.flip()  # uploading the results in your screen (MUST)

    def move_left(self):
        self.direction = 'left'

    def move_right(self):
        self.direction = 'right'

    def move_up(self):
        self.direction = 'up'

    def move_down(self):
        self.direction = 'down'

    def walk(self):

        for i in range(self.length - 1, 0, -1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]  # put the blocks in previous location

        if self.direction == 'left':
            self.x[0] -= SIZE  # move SIZE
        if self.direction == 'right':
            self.x[0] += SIZE
        if self.direction == 'up':
            self.y[0] -= SIZE
        if self.direction == 'down':
            self.y[0] += SIZE

        self.draw()  # after changing the direction, draw()


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Snake and Apple Game!")

        pygame.mixer.init()

        self.play_background_music()
        self.surface = pygame.display.set_mode((1000, 800))  # initializing game window & window size
        self.snake = Snake(self.surface, 1)  # drawing a snake (starting with a length of 1)
        self.snake.draw()
        self.apple = Apple(self.surface)
        self.apple.draw()

    def play_sound(self, sound):
        sound = pygame.mixer.Sound(f"C:/Users/harry/OneDrive/Desktop/{sound}.mp3")
        pygame.mixer.Sound.play(sound)

    def render_background(self):
        bg = pygame.image.load('C:/Users/harry/OneDrive/Desktop/background.jpg')
        self.surface.blit(bg, (0, 0))  # location starting from (0, 0)

    def play(self):
        self.render_background()
        self.snake.walk()
        self.apple.draw()
        self.display_score()
        pygame.display.flip()

        # snake colliding with apple
        if self.is_collision(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y):
            self.play_sound("ding")
            self.snake.increase_length()
            self.apple.move()

        # snake colliding itself
        for i in range(3, self.snake.length):  # snake can collide with starting from the 3rd block
            if self.is_collision(self.snake.x[0], self.snake.y[0], self.snake.x[i],
                                 self.snake.y[i]):  # head colliding with itself (remaining blocks)
                self.play_sound("crash")
                raise "Collision Occurred!"

    def play_background_music(self):
        pygame.mixer.music.load("C:/Users/harry/OneDrive/Desktop/music.mp3")
        # sound - short time & music - long time
        pygame.mixer.music.play()

    def display_score(self):
        font = pygame.font.SysFont('arial', 30)
        score = font.render(f"Score: {self.snake.length}", True, (255, 255, 255))
        self.surface.blit(score, (800, 10))

    def is_collision(self, x1, y1, x2, y2):
        if (x1 >= x2) and (x2 + SIZE > x1):
            if (y1 >= y2) and (y2 + SIZE) > y1:
                return True

        return False

    def show_game_over(self):
        self.render_background()
        font = pygame.font.SysFont('arial', 30)
        line1 = font.render(f"Game is over! Your score is {self.snake.length}", True, (255, 255, 255))
        self.surface.blit(line1, (200, 300))
        line2 = font.render("To play again press Enter. To exit press Escape!", True, (255, 255, 255))
        self.surface.blit(line2, (200, 350))

        pygame.display.flip()

        pygame.mixer.music.pause()

    def reset(self):  # resetting the game - initializing a snake & an apple
        self.snake = Snake(self.surface, 1)  # drawing a snake (starting with a length of 1)
        self.apple = Apple(self.surface)

    def run(self):
        # event loop (necessary)

        running = True
        pause = False

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    # KEY DOWN - from local
                    if event.key == K_ESCAPE:
                        running = False

                    if event.key == K_RETURN:
                        pygame.mixer.music.unpause()
                        pause = False

                    if not pause:
                        # up, down, left, right key - block moving (x & y coordinates changed)
                        if event.key == K_UP:
                            self.snake.move_up()

                        if event.key == K_DOWN:
                            self.snake.move_down()

                        if event.key == K_LEFT:
                            self.snake.move_left()

                        if event.key == K_RIGHT:
                            self.snake.move_right()

                elif event.type == QUIT:
                    running = False
            try:
                if not pause:
                    self.play()
            except Exception as e:
                self.show_game_over()
                pause = True
                self.reset()
            time.sleep(.2)  # after 0.2 seconds, it moves on its own


if __name__ == '__main__':
    game = Game()
    game.run()
