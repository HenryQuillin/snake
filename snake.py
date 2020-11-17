import turtle
import random 

up = False
down = False
left = False
right = False
keep_playing = True 
apple = turtle.Turtle()

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

# Draw apple 
def draw_apple(): 
    global apple
    apple.shape("circle")
    apple.color("red")
    apple.penup()
    ran_x = random.randrange(- 240 , 240 , 10 ) 
    ran_y = random.randrange(- 240 , 240 , 10 ) 
    apple.setpos(ran_x , ran_y)

def head_up():
    global up, down, left, right
    up = True
    down = False
    left = False
    right = False 

def head_down():
    global up, down, left, right
    up = False
    down = True
    left = False
    right = False 

def head_left():
    global up, down, left, right
    up = False
    down = False
    left = True
    right = False 


def head_right():
    global up, down, left, right
    up = False
    down = False
    left = False
    right = True 

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
    if ((apple.ycor() <= head.ycor()+ 10 and apple.ycor() >= head.ycor()- 10 ) and (apple.xcor() <= head.xcor()+ 10 and apple.xcor() >= head.xcor()- 10 )):
        draw_apple()
    
draw_apple()
def gameplay():
    global keep_playing 
    while keep_playing == True:
        global up, down, left, right
        if up == True:
            y = head.ycor()
            y += 5
            head.sety(y)
        if down == True:
            y = head.ycor()
            y -= 5
            head.sety(y)
        if left == True:
            x = head.xcor()
            x -= 5
            head.setx(x)
        if right == True:
            x = head.xcor()
            x += 5
            head.setx(x)
        check_boundaries()
        eat_apple(apple)
        window.update()
gameplay()
turtle.done()

