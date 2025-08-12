from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from board import Board
import time

screen = Screen()
screen.setup(width=680, height=680)
screen.bgcolor("PaleGreen")
screen.title("Snake Game")
screen.tracer(0)

Board()

snake = Snake()
food = Food()
scorebrd = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

def game_loop():
    screen.update()
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scorebrd.increase_score()

    if abs(snake.head.xcor()) > 310 or abs(snake.head.ycor()) > 310:
        scorebrd.reset_scoreboard()
        snake.reset()
        food.refresh()

    for part in snake.all_bodypart[1:]:
        if snake.head.distance(part) < 10:
            scorebrd.reset_scoreboard()
            snake.reset()
            food.refresh()

    screen.ontimer(game_loop, 80)

def quit_game():
    screen.bye()

screen.onkey(quit_game, "q")

game_loop()
screen.mainloop()