import time
from turtle import Screen
import snake, scoreboard, food


def start_game():
    screen_func = Screen()
    screen_func.setup(width=600, height=600)
    screen_func.bgcolor("black")
    screen_func.title("Snake Game ")
    screen_func.tracer(0)

    snake_func = snake.SnakeGame()
    food_func = food.Food()
    scoreboard_num = scoreboard.ScoreBoard()

    screen_func.listen()
    screen_func.onkey(snake_func.up, "Up")
    screen_func.onkey(snake_func.down, "Down")
    screen_func.onkey(snake_func.left, "Left")
    screen_func.onkey(snake_func.right, "Right")

    segments = snake_func.segments

    game_is_on = True

    while game_is_on:
        screen_func.update()
        time.sleep(0.1)
        snake_func.move()

        if snake_func.head.distance(food_func) < 15:
            food_func.refresh()
            snake_func.extend()
            scoreboard_num.increase_score()

        if snake_func.head.xcor() > 290 or snake_func.head.xcor() < -290 or snake_func.head.ycor() > 290 or snake_func.head.ycor() < -290:
            game_is_on = False
            scoreboard_num.game_over()

        for segment in segments[1:]:

            if snake_func.head.distance(segment) < 10:
                game_is_on = False
                scoreboard_num.game_over()

    screen_func.exitonclick()


start_game()
