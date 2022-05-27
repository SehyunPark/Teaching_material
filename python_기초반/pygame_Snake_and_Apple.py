import pygame  # pygame 가져오기
from pygame.locals import *  # 상수들 가져오기
import time  # 뱀 속도 설정 위해 가져오기
import random  # 사과 램덤 배치를 위해 가져오기

SIZE = 40  # 블록 사이즈 40


class Apple:
    def __init__(self, parent_screen):
        self.apple = pygame.image.load('apple.jpg').convert()  # 사과 그림 가져오기
        self.parent_screen = parent_screen  # 스크린 설정
        self.x = SIZE * 3  # 첫 위치
        self.y = SIZE * 3  # 첫 위치

    def draw(self):
        self.parent_screen.blit(self.apple, (self.x, self.y))  # 사과 그리기
        pygame.display.flip()  # 사과 올리기

    def move(self):
        self.x = random.randint(1, 24) * SIZE  # 랜덤한 위치에 사과 배치
        self.y = random.randint(1, 19) * SIZE  # 랜덤함 위치에 사과 배치


class Snake:
    def __init__(self, parent_screen, length):
        self.length = length  # 뱀 길이
        self.parent_screen = parent_screen  # 스크린 설정
        self.block = pygame.image.load('block.jpg').convert()  # 블록 그림 가져오기

        self.x = [SIZE] * length
        self.y = [SIZE] * length
        self.direction = 'down'  # 첫 방향

    def increase_length(self):
        self.length += 1
        self.x.append(-1)  # 새로운 블록 추가
        self.y.append(-1)  # 새로운 블록 추가

    def draw(self):
        for i in range(self.length):
            self.parent_screen.blit(self.block, (self.x[i], self.y[i]))  # 블록 그리기
        pygame.display.flip()  # 스크린에 띄우기

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
            self.y[i] = self.y[i - 1]  # 앞 선 블록 위치에 그 다음 블록 위치시키기

        if self.direction == 'left':
            self.x[0] -= SIZE  # 블록 크기만큼 이동
        if self.direction == 'right':
            self.x[0] += SIZE
        if self.direction == 'up':
            self.y[0] -= SIZE
        if self.direction == 'down':
            self.y[0] += SIZE

        self.draw()  # 방향을 바꿨으면 꼭 그려서 화면에 나타내기


class Game:
    def __init__(self):
        pygame.init()  # 게임 생성
        pygame.display.set_caption("Snake and Apple Game!")

        pygame.mixer.init()  # 소리 설정

        self.play_background_music()  # 배경 음악 재생
        self.surface = pygame.display.set_mode((1000, 800))  # 게임 창 사이즈 조절

        self.snake = Snake(self.surface, 1)  # 길이 1인 뱀 생성
        self.snake.draw()  # 뱀 그리기

        self.apple = Apple(self.surface)  # 사과 생성
        self.apple.draw()  # 사과 그리기

    @staticmethod
    def play_sound(sound):
        sound = pygame.mixer.Sound(f"{sound}.mp3")  # mp3 경로
        pygame.mixer.Sound.play(sound)

    def show_background(self):
        bg = pygame.image.load('background.jpg')   # jpg 경로
        self.surface.blit(bg, (0, 0))  # 배경은 (0,0)부터 시작

    def play(self):
        self.show_background()
        self.snake.walk()
        self.apple.draw()
        self.display_score()
        pygame.display.flip()

        # 사과 먹기
        if self.is_collision(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y):
            self.play_sound("ding")
            self.snake.increase_length()
            self.apple.move()

        # 뱀 머리가 몸과 충돌
        for i in range(3, self.snake.length):  # 세번째 블록부터 몸과 충돌 발생
            if self.is_collision(self.snake.x[0], self.snake.y[0], self.snake.x[i],
                                 self.snake.y[i]):
                self.play_sound("crash")
                raise "Collision Occurred!"

    @staticmethod
    def play_background_music():
        pygame.mixer.music.load("music.mp3")
        pygame.mixer.music.play()

    def display_score(self):
        font = pygame.font.SysFont('arial', 30)
        score = font.render(f"Score: {self.snake.length}", True, (255, 255, 255))
        self.surface.blit(score, (800, 10))

    @staticmethod
    def is_collision(x1, y1, x2, y2):
        if (x1 >= x2) and (x2 + SIZE > x1):
            if (y1 >= y2) and (y2 + SIZE) > y1:
                return True

        return False

    def show_game_over(self):
        self.show_background()
        font = pygame.font.SysFont('arial', 30)
        line1 = font.render(f"Game is over! Your score is {self.snake.length}", True, (255, 255, 255))
        self.surface.blit(line1, (200, 300))
        line2 = font.render("To play again press Enter. To exit press Escape!", True, (255, 255, 255))
        self.surface.blit(line2, (200, 350))

        pygame.display.flip()

        pygame.mixer.music.pause()

    def reset(self):
        self.snake = Snake(self.surface, 1)  # 길이가 1인 뱀 다시 생성
        self.apple = Apple(self.surface)  # 사과도 다시 생성

    def run(self):
        # 게임 진행 룹

        running = True
        pause = False

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    # local에서 가져온 KEYDOWN 키 입력 상수
                    if event.key == K_ESCAPE:
                        running = False

                    if event.key == K_RETURN:
                        pygame.mixer.music.unpause()
                        pause = False

                    if not pause:
                        # 방향키 위 아래 왼 오른쪽
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
            time.sleep(.2)  # 뱀 속력 조절


if __name__ == '__main__':
    game = Game()
    game.run()
