from turtle import Turtle,Screen

# tim = Turtle()
# tim.pencolor()

# def forward():
#   tim.fd(10)

# def back():
#   tim.bk(10)

# def clock():
#   move = 10
#   tim.left(move)
#   move += 10

# def anticlock():
#   move = 10
#   tim.right(move)
#   move += 10

# def clear():
#   tim.clear()
#   tim.penup()
#   tim.home()
#   tim.pendown()
from random import randint
screen = Screen()
screen.setup(width=500,height=400)
screen.listen()

bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter color: ")

def random_move(turtle):
  turtle.forward(randint(0,10))

def who_wins(bet,winner):
  if bet == winner:
    print(f"Your bet was correct the winner is the {winner} turtle")
  else:
    print(f"you guess was {bet} turtle the winner is the {winner} turtle you looooose! ")

def create_turtles(bet):
  colors = ["red","orange","yellow","green","blue","indigo","violet"]
  color = ["red","orange","yellow","green","blue","indigo","violet"]
  x = -230
  y = -100
  winner = ""
  end_of_race = False

  for i in range(len(colors)-1):
    colors[i] = Turtle(shape ="turtle")
    colors[i].penup()
    colors[i].goto(x=x,y=y)
    colors[i].color(color[i])
    y += 30

  while not end_of_race:
    for i in range(len(colors) -1):
      if colors[i].xcor() > 230:
        end_of_race = True
        winner = colors[i].pencolor()
        print(winner)
      else:
        random_move(colors[i])
  who_wins(bet=bet,winner=winner)
  
  # for turtle in colors:
  #   # f"{colors[turtle]}_turtle" = Turtle()
  #   colors[turtle] = Turtle()
  #   colors[turtle].color(colors[turtle])
  #   print("")

create_turtles(bet)


screen.exitonclick()