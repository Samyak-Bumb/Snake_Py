# Created/Wriiten By Samyak Bumb

from cmath import rect
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
        # Move Rightwards (No Key Event Required)
        self.direction = Vector2(1, 0)
        self.new_block = False

    def draw_snake(self):
        for block in self.body:
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)

            block_rect = pygame.Rect(
                x_pos, y_pos, cell_size, cell_size)
            pygame.draw.rect(
                screen, Rectangle_clra, block_rect)

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

    def add_block(self):
        self.new_block = True

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
        # Fruit Setup
        self.fruit.draw_fruit()
        # Snake Setup
        self.snake.draw_snake()
        # Grass Setup
        self.draw_grass()

    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            # Reposition the Fruit (After Eating Changing the Position of Apple)
            self.fruit.randomiz()
            # Add Another Block to the Snake (Extending Snake after Eating Apple)
            self.snake.add_block()

    def check_fail(self):
        # Check if Snake is Outside of the Screen
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
            self.game_over()
        # Check if Snake hits himself
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

    def game_over(self):
        pygame.quit()
        sys.exit()

    def draw_grass(self):
        grass_clr = (162, 209, 73)

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

    # Basic Setup


pygame.init()

pygame.display.set_caption("Snake Game By Samyak Bumb")

# Variables
cell_size = 34
cell_number = 19
Rectangle_clr = 231, 71, 29  # Box Color
Rectangle_clra = 71, 188, 236  # Snake Color
apple = pygame.image.load('assets/img/apple.png')


# Screen Size
screen = pygame.display.set_mode(
    (cell_number * cell_size, cell_number * cell_size))
clock = pygame.time.Clock()

# Objects
main_game = MAIN()

SCREEN_UPDATE = pygame.USEREVENT
# This event will Triggerd after every 150 ms (Speed of Snake)
pygame.time.set_timer(SCREEN_UPDATE, 150)

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

# Thanks to "Clear Code"
