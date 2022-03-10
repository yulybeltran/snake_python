from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

#Creación del tablero de el juego
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("red")
screen.title("Programáte snake game")

screen.tracer(0)

game_is_on = True

#Creo a la serpiente - Instanciar el objeto serpiente
snake = Snake()

#Creamos el objeto comida
food = Food()

#Creamos el objeto tablero
scoreboard = ScoreBoard()

#Metodo escucha de las teclas
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    #Detecatar colision de comida
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()
   
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280 :
        game_is_on = False
        scoreboard.game_over()

    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()