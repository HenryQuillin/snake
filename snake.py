'''
Henry Quillin 
Snake Game using Turtle 
11/22/2020
'''

import turtle
import random 

up = False
down = False
left = False
right = False
keep_playing = True 
apple = turtle.Turtle()
snake_body = []

# Create screen
window = turtle.Screen()
window.title("Snake game")
window.bgcolor("blue")
width = 500
height = 500
window.setup(width= width, height= height)

# draw snake head 
head = turtle.Turtle()
head.shape("square")
head.color("#FF00FF")
head.penup()
head.goto(0, 0)
head.direction = 'stop'

# Draw apple 
def draw_apple(): 
    global apple
    apple.shape("circle")
    apple.color("red")
    apple.penup()
    ran_x = random.randrange(- 240 , 240 , 10 ) 
    ran_y = random.randrange(- 240 , 240 , 10 ) 
    apple.setpos(ran_x , ran_y)
    apple.speed(0)
    grow_snake()
    #code to add to snake body 

def grow_snake():
    new_segment = turtle.Turtle()
    new_segment.speed = 0
    new_segment.shape = 'square'
    new_segment.color("#FF00FF")
    new_segment.penup()
    snake_body.append(new_segment)

def head_up():
    head.direction = 'up'

def head_down():
    head.direction = 'down'

def head_left():
    head.direction = 'left'


def head_right():
    head.direction = 'right'

def close():
    exit()

def close_text():
    close = turtle.Turtle()
    close.hideturtle()
    close.write( "Wall hit" , align = "center" , font =( "Courier" , 24 , "normal" ))

# Keyboard bindings
window.listen()
window.onkeypress(head_up , "w" )
window.onkeypress(head_left , "a" )
window.onkeypress(head_down , "s" )
window.onkeypress(head_right , "d" )
window.onkeypress(close , "Escape" )

def check_boundaries(): 
    global keep_playing
    if head.ycor() <= - 245 or head.ycor() >= 245:
        keep_playing = False
        close_text()
    if head.xcor() <= - 245 or head.xcor() >= 245:
        keep_playing = False
        close_text()


def eat_apple(apple): 
    if (head.distance(apple) < 20):
        draw_apple()
    
draw_apple()
def gameplay():
    global keep_playing 
    while keep_playing == True:
        check_boundaries()
        eat_apple(apple)
        window.update()
        global up, down, left, right
        if head.direction == 'up':
            head.sety(head.ycor() + 20)
        if head.direction == 'down':
            head.sety(head.ycor() - 20)
        if head.direction == 'left':
            head.setx(head.xcor() - 20)
        if head.direction == 'right':
            head.setx(head.xcor() + 20)
        # move end segment of snake body 
        for index in range(len(snake_body) - 1,0,-1):
            x = snake_body[index - 1].xcor()
            y = snake_body[index - 1].ycor()
            snake_body[index].goto(x,y)
        if len(snake_body) > 0:
            x = head.xcor
            y = head.ycor
            print(type(x))
            snake_body[0].goto(x,y)


gameplay()
turtle.done()

