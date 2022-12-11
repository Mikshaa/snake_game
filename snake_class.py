import time as tm
import random
import turtle as t

print('test')

class Snake:
    
    def __init__(self, color, color_hd, shape, x, y, long):
        self.snake = []
        self.long = long
        for i in range(long):
            tip = t.Turtle()
            tip.shape(shape)
            tip.color(color)
            tip.penup()
            tip.setpos(-i*20+x, 0+y)
            self.snake.append(tip)
        self.snake[0].color(color_hd)
        self.head = self.snake[0]

        
    def move(self):
        hd = self.snake[0].heading()
        for i in self.snake:
            last_hd = i.heading()
            i.forward(20)
            i.setheading(hd)
            hd = last_hd
            if i.xcor()>=300:
                i.setx(-300)
            if i.ycor() >= 300:
                i.sety(-300)
            if i.xcor()<-300:
                i.setx(300)
            if i.ycor() < -300:
                i.sety(300)

                
    def turn(self, x):
        self.snake[0].setheading(x)

        
    def dtp(self):
        for i in range(1, len(self.snake)):
            if self.snake[0].distance(self.snake[i])<10:
                return False
        return True

    
    def more(self, color, shape):
        tip = t.Turtle()
        tip.shape(shape)
        tip.color(color)
        tip.penup()
        tip.setpos(self.snake[-1].pos())
        tip.backward(20)
        self.snake.append(tip)

    def check_food(self, food):
        if self.snake[0].distance(food.food)<20:
            return True
        return False


class Food:
    
    def __init__(self, color, shape):
        self.food = t.Turtle()
        self.food.shape(shape)
        self.food.color(color)
        self.food.penup()

        
    def food_pos(self):
        self.food.setpos(random.randrange(-250,250), random.randrange(-250,250))

class Field:

    def __init__(self):
        self.ts = t.Screen()
        self.ts.title('Змейка')
        self.ts.bgcolor('pink')
        self.ts.setup(width=600, height=600)
        self.ts.tracer(0)
        #self.snake = Snake('black', 'white', 'turtle', 0, 0, 5)
        #self.food = Food('green', 'circle')

        
    def listen_p(self, snake):
        self.obj = snake
        self.ts.listen()
        self.ts.onkeypress(self.goleft , "Left")
        self.ts.onkeypress(self.goright, "Right")
        self.ts.onkeypress(self.goup, "Up")
        self.ts.onkeypress(self.godown, "Down")

    def goleft(self):
        for i in self.obj:
            i.turn(180)

    def goup(self):
        for i in self.obj:
            i.turn(90)

    def goright(self):
        for i in self.obj:
            i.turn(0)

    def godown(self):
        for i in self.obj:
            i.turn(270)

    def reload(self):
        self.ts.update()

    def end_game(self):
        end_text = t.Turtle()
        end_text.hideturtle()
        end_text.color('red')
        end_text.penup()
        end_text.goto(-100,200)
        end_text.write('Game Over', font=('Arial', 40))
        
"""  
    def play(self):
        self.food.food_pos()
        while self.snake.dtp():
            
            self.snake.move()
            if self.snake.snake[0].distance(self.food.food)<20:
                self.food.food_pos()
                self.snake.more('black', 'turtle')
            self.ts.update()
            tm.sleep(0.2)
        else:
            print('lose')

        """
        








