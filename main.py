# Created/Written By Samyak Bumb

import pygame
import sys
import random

from pygame.math import Vector2


# Fruit Function (Apple)

class FRUIT:
    def __init__(self):
        # If th Snake Eats Apple Change the Position of Apple
        self.randomiz()

    def draw_fruit(self):
        # Drawing a Rectangle
        fruit_rect = pygame.Rect(
            int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)

        # Fruit Graphics
        screen.blit(apple, fruit_rect)

        # pygame.draw.rect(screen, Rectangle_clr, fruit_rect)

    def randomiz(self):
        # Random integer to move it from 1 Place to another (Changing Position of Fruit)
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        # Creating an X & Y Position
        self.pos = Vector2(self.x, self.y)


# Snake Function

class SNAKE:
    def __init__(self):
        self.body = [
            Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)
        ]
        # Removed
        # Move Rightwards (No Key Event Required)
        # self.direction = Vector2(1, 0)
        # Added
        self.direction = Vector2(0, 0)
        # To stop infinte blocks after eating apple
        self.new_block = False

        self.head_up = pygame.image.load(
            "assets/img/head_up.png").convert_alpha()
        self.head_down = pygame.image.load(
            "assets/img/head_down.png").convert_alpha()
        self.head_right = pygame.image.load(
            "assets/img/head_right.png").convert_alpha()
        self.head_left = pygame.image.load(
            "assets/img/head_left.png").convert_alpha()

        self.tail_up = pygame.image.load(
            "assets/img/tail_up.png").convert_alpha()
        self.tail_down = pygame.image.load(
            "assets/img/tail_down.png").convert_alpha()
        self.tail_right = pygame.image.load(
            "assets/img/tail_right.png").convert_alpha()
        self.tail_left = pygame.image.load(
            "assets/img/tail_left.png").convert_alpha()

        self.body_vertical = pygame.image.load(
            "assets/img/body_vertical.png").convert_alpha()
        self.body_horizontal = pygame.image.load(
            "assets/img/body_horizontal.png").convert_alpha()

        self.body_tr = pygame.image.load(
            "assets/img/body_tr.png").convert_alpha()
        self.body_tl = pygame.image.load(
            "assets/img/body_tl.png").convert_alpha()
        self.body_br = pygame.image.load(
            "assets/img/body_br.png").convert_alpha()
        self.body_bl = pygame.image.load(
            "assets/img/body_bl.png").convert_alpha()
        self.crunch = pygame.mixer.Sound(
            "assets/Sound/crunch.wav")

    def draw_snake(self):
        self.update_face_graphics()
        self.update_tail_graphics()

        for index, block in enumerate(self.body):
            # 1. We will still need a Rect for the Positioning
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)

            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
            # 2.What Dirction is the face Heading
            if index == 0:
                # Make it "head" if it is "head_right"
                screen.blit(self.head, block_rect)
            elif index == len(self.body) - 1:
                screen.blit(self.tail, block_rect)
            else:
                # Removed
                # pygame.draw.rect(screen, (255, 255, 255), block_rect)
                # Added
                previous_block = self.body[index + 1] - block
                next_block = self.body[index - 1] - block

                if previous_block.x == next_block.x:
                    screen.blit(self.body_vertical, block_rect)
                elif previous_block.y == next_block.y:
                    screen.blit(self.body_horizontal, block_rect)
                else:
                    if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
                        screen.blit(self.body_tl, block_rect)
                    elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
                        screen.blit(self.body_bl, block_rect)
                    elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
                        screen.blit(self.body_tr, block_rect)
                    elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
                        screen.blit(self.body_br, block_rect)

        # 3. Snake head Dirction is not updating
    def update_face_graphics(self):
        head_relation = self.body[1] - self.body[0]
        if head_relation == Vector2(1, 0):
            self.head = self.head_left

        elif head_relation == Vector2(-1, 0):
            self.head = self.head_right

        elif head_relation == Vector2(0, 1):
            self.head = self.head_up

        elif head_relation == Vector2(0, -1):
            self.head = self.head_down

    def update_tail_graphics(self):
        tail_relation = self.body[-2] - self.body[-1]
        if tail_relation == Vector2(1, 0):
            self.tail = self.tail_left

        elif tail_relation == Vector2(-1, 0):
            self.tail = self.tail_right

        elif tail_relation == Vector2(0, 1):
            self.tail = self.tail_up

        elif tail_relation == Vector2(0, -1):
            self.tail = self.tail_down

        # for block in self.body:
        #     x_pos = int(block.x * cell_size)
        #     y_pos = int(block.y * cell_size)

        #     block_rect = pygame.Rect(
        #         x_pos, y_pos, cell_size, cell_size)
        #     pygame.draw.rect(
        #         screen, Rectangle_clra, block_rect)

    def move_snake(self):
        if self.new_block == True:
            # Moving the Snake (Taking All the Element Execpt Last":1")
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0]+self.direction)
            self.body = body_copy[:]
            # Solving The Problem of Infinte Blocks (Extending Snake)
            self.new_block = False
        else:
            # Moving the Snake (Taking All the Element Execpt Last":1")
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0]+self.direction)
            self.body = body_copy[:]

    def reset(self):
        self.body = [
            Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)
        ]
        self.direction = Vector2(1, 0)

    def adding_block(self):
        self.new_block = True

    def reset(self):
        self.body = [
            Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)
        ]
        # To stop the Snake (Stop it from same direction after game_over)
        self.direction = Vector2(0, 0)

    def crunch_eating(self):
        self.crunch.play()


# Adding Main Logic to Game (Connecting)

class MAIN:
    def __init__(self):
        # Adding FRUIT class in "MAIN"
        self.fruit = FRUIT()
        # Adding SNAKE class in "MAIN"
        self.snake = SNAKE()

    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()

    def draw_element(self):
        # If get eny Problem take that elemnt to the top

        # Grass Setup
        self.draw_grass()
        # Score Setup
        self.show_score()
        # Fruit Setup
        self.fruit.draw_fruit()
        # Snake Setup
        self.snake.draw_snake()

    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            # Reposition the Fruit (After Eating Changing the Position of Apple)
            self.fruit.randomiz()
            # Add Another Block to the Snake (Extending Snake after Eating Apple)
            self.snake.adding_block()
            # Crunch sound after eating apple
            self.snake.crunch_eating()

        # Final tweaks (There are some chances that the fruit will land on the body of snake to fix it this code is used EZ)
        for block in self.snake.body[1:]:
            if block == self.fruit.pos:
                self.fruit.randomiz()

    def check_fail(self):
        # Check if Snake is Outside of the Screen
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
            self.game_over()
        # Check if Snake hits himself
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

    def game_over(self):
        self.snake.reset()

    def draw_grass(self):
        for row in range(cell_number):
            if row % 2 == 0:
                for col in range(cell_number):
                    if col % 2 == 0:
                        grass_rect = pygame.Rect(
                            col * cell_size, row * cell_size, cell_size, cell_size)

                        pygame.draw.rect(
                            screen, grass_clr, grass_rect)
            else:
                for col in range(cell_number):
                    if col % 2 != 0:
                        grass_rect = pygame.Rect(
                            col * cell_size, row * cell_size, cell_size, cell_size)

                        pygame.draw.rect(
                            screen, grass_clr, grass_rect)

    def show_score(self):
        # Counting
        scor_txt = str(len(self.snake.body) - 3)
        score_surface = fnt.render(scor_txt, True, (0, 0, 0))
        # Positioning
        # Left = Increase, Right = Decrese
        score_x = int(cell_size * cell_number - 15)
        # Top = Increase, Bottom = Decrese
        score_y = int(cell_size * cell_number - 630)
        score_rect = score_surface.get_rect(center=(score_x, score_y))
        apple_rect = apple.get_rect(midright=(
            score_rect.left, score_rect.centery))
        bg_rect = pygame.Rect(
            apple_rect.left, apple_rect.top, apple_rect.width + apple_rect.width + 6, apple_rect.height)  # x, y, w, h Respectively

        pygame.draw.rect(screen, grass_clr, bg_rect)  # Bg of apple+txt
        screen.blit(score_surface, score_rect)
        screen.blit(apple, apple_rect)
        # Border  # WARNING: DON'T Increse
        pygame.draw.rect(screen, (0, 0, 0), bg_rect, 1)

    # Basic Setup


# Sound Speed & Dealy
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()

pygame.display.set_caption("Snake Game By Samyak Bumb")

# Variables
cell_size = 34
cell_number = 19
# Rectangle_clr = 231, 71, 29  # Box Color
# Rectangle_clra = 71, 188, 236  # Snake Color
grass_clr = (162, 209, 73)
apple = pygame.image.load("assets/img/apple.png")
fnt = pygame.font.Font("assets/fnt/PoetsenOne.ttf", 25)


# Screen Size
screen = pygame.display.set_mode(
    (cell_number * cell_size, cell_number * cell_size))
clock = pygame.time.Clock()

# Objects
main_game = MAIN()

SCREEN_UPDATE = pygame.USEREVENT
# This event will Triggerd after every 150 ms (Speed of Snake)
pygame.time.set_timer(SCREEN_UPDATE, 200)

################################################

# Screen Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Move Snake Condition
        if event.type:
            main_game.update()

        # != means "Not Equal"
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                # This condtion is added cuz it should not go Reverse
                if main_game.snake.direction.y != 1:
                    # Move Upwards
                    main_game.snake.direction = Vector2(0, -1)
            if event.key == pygame.K_w:
                # This condtion is added cuz it should not go Reverse
                if main_game.snake.direction.y != 1:
                    # Move on Press "w" Upwards
                    main_game.snake.direction = Vector2(0, -1)
            if event.key == pygame.K_DOWN:
                # This condtion is added cuz it should not go Reverse
                if main_game.snake.direction.y != -1:
                    # Move Downwards
                    main_game.snake.direction = Vector2(0, 1)
            if event.key == pygame.K_s:
                # This condtion is added cuz it should not go Reverse
                if main_game.snake.direction.y != -1:
                    # Move on Press "s" Downwards
                    main_game.snake.direction = Vector2(0, 1)
            if event.key == pygame.K_LEFT:
                # This condtion is added cuz it should not go Reverse
                if main_game.snake.direction.x != 1:
                    # Move Leftwards
                    main_game.snake.direction = Vector2(-1, 0)
            if event.key == pygame.K_a:
                # This condtion is added cuz it should not go Reverse
                if main_game.snake.direction.x != 1:
                    # Move on Press "a" Leftwards
                    main_game.snake.direction = Vector2(-1, 0)
            if event.key == pygame.K_RIGHT:
                # This condtion is added cuz it should not go Reverse
                if main_game.snake.direction.x != -1:
                    # Move Rightwards
                    main_game.snake.direction = Vector2(1, 0)
            if event.key == pygame.K_d:
                # This condtion is added cuz it should not go Reverse
                if main_game.snake.direction.x != -1:
                    # Move on Press "d" Rightwards
                    main_game.snake.direction = Vector2(1, 0)

        # Board (Inside of Window)
        screen.fill((170, 215, 81))  # Board Color
        # Execpt 2 Line of Code in 1 Line (Clean Code)
        main_game.draw_element()

    # FPS & Continue Display
    pygame.display.update()
    clock.tick(59)

# Thanks to "Clear Code" YouTube Channel for this Awesome Tutorial
