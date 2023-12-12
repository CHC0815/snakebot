from typing import get_args

from snake.Snake import Snake, SnakeMoves


def map_action(action: str):
    if action == "w":
        return 1
    elif action == "s":
        return 2
    elif action == "a":
        return 3
    elif action == "d":
        return 4
    else:
        raise ValueError("Invalid action")


def main():
    snake = Snake()
    running = True
    while running:
        action = input()
        if action == "q":
            running = False
            break
        a = map_action(action[0])
        running = snake.step(a)  # type: ignore
        snake.render()


if __name__ == "__main__":
    main()
