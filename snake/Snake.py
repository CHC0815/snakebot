from typing import Literal, Tuple

import numpy as np

SnakeMoves = Literal[1, 2, 3, 4]
SnakeHead = 3
SnakeBody = 2
Food = 1


class Snake:
    def __init__(self):
        self.rows = 10
        self.cols = 10
        self.board = np.zeros((self.cols, self.rows), dtype=int)
        self.change = [0, 0]
        self.snake_body = [[5, 5]]
        self.add_food()

    def update_change(self, action):
        if action == 1:  # up
            self.change = [0, -1]
        elif action == 2:  # down
            self.change = [0, 1]
        elif action == 3:  # left
            self.change = [-1, 0]
        elif action == 4:  # right
            self.change = [1, 0]
        else:
            raise ValueError("Invalid action")

    def collides_with_boundaries(self) -> bool:
        return (
            self.snake_body[-1][0] < 0
            or self.snake_body[-1][0] >= self.cols
            or self.snake_body[-1][1] < 0
            or self.snake_body[-1][1] >= self.rows
        )

    def add_food(self):
        food = np.random.randint(0, self.rows), np.random.randint(0, self.cols)
        while self.board[food[0], food[1]] == 1:
            food = np.random.randint(0, self.rows), np.random.randint(0, self.cols)
        self.board[food[0], food[1]] = 1

    def collides_with_food(self) -> bool:
        return self.board[self.snake_body[-1][0], self.snake_body[-1][1]] == Food

    def collides_with_self(self) -> bool:
        return (
            self.board[self.snake_body[-1][0], self.snake_body[-1][1]] == SnakeBody
            or self.board[self.snake_body[-1][0], self.snake_body[-1][1]] == SnakeHead
        )

    def update_snake(self):
        self.snake_body.append(
            [
                self.snake_body[-1][0] + self.change[0],
                self.snake_body[-1][1] + self.change[1],
            ]
        )

    def add_snake(self):
        for part in self.snake_body:
            self.board[part[0], part[1]] = SnakeBody
        self.board[self.snake_body[-1][0], self.snake_body[-1][1]] = SnakeHead

    def remove_snake(self):
        for part in self.snake_body:
            self.board[part[0], part[1]] = 0

    def step(self, action: SnakeMoves) -> bool:
        self.update_change(action)
        self.update_snake()
        if self.collides_with_self():
            return False
        if self.collides_with_boundaries():
            return False
        food = self.collides_with_food()
        self.remove_snake()
        if food:
            self.add_food()
        else:
            self.snake_body.pop(0)
        self.add_snake()
        return True

    def render(self):
        print("-" * 20)
        for row in range(self.rows):
            for col in range(self.cols):
                print(self.board[col, row], end=" ")
            print()
