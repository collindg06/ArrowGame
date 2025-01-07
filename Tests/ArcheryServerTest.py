# This program is a test for the program that simulates the server side of a client/server connection using udp that allows the user to play a game of archery against the computer. 

# Imports
import turtle
import random
from socket import * 

# Configure server
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print('The server is ready to receive')


def receiveVariables():

   # Get variables from the client
   power, clientAddress = serverSocket.recvfrom(2048)
   aim, clientAddress = serverSocket.recvfrom(2048)
   windPower, clientAddress = serverSocket.recvfrom(2048)
   isneg, clientAddress = serverSocket.recvfrom(2048)

   # Decode variables
   power = power.decode()
   aim = aim.decode()
   windPower = windPower.decode()
   isneg = isneg.decode()

   # Convert decoded variables to integers and boolean
   power = int(power)
   aim = int(aim)
   windPower = int(windPower)
   isneg = bool(isneg)

   return power, aim, windPower, isneg, clientAddress

def displayTarget():

   # Draw target
   window = turtle.Screen()
   turtle.TurtleScreen._RUNNING=True
   target = turtle.Turtle()
   turtle.bgcolor('deepskyblue') 

   target.penup()
   target.forward(150)
   target.pendown()

   target.color('blue','blue')
   target.begin_fill()
   target.circle(50)
   target.end_fill()

   target.penup()
   target.goto(target.xcor(), target.ycor() + 40)
   target.pendown()
   target.color('yellow','yellow')
   target.begin_fill()
   target.circle(10)
   target.end_fill()
   target.forward(15)
   target.hideturtle()
   target.pensize(5)
   target.penup()
   target.goto(target.xcor()+ 5, target.ycor() -36)
   target.pendown()
   target.color('brown','brown')
   target.goto(target.xcor(), target.ycor() -30)
   target.penup()
   target.goto(target.xcor() - 40, target.ycor())
   target.pendown()
   target.goto(target.xcor(), target.ycor() +30)

def shootArrow(power, aim, isneg):

   # Show arrow being shot
   arrow = turtle.Turtle()
   arrow.penup()
   arrow.goto(arrow.xcor()-400, arrow.ycor() + 40 )
   arrow.pendown()
   arrow.color ('green')
   arrow.pensize (2)
   arrow.shape ('arrow')
   arrow.setheading(aim)
   arrow.forward(power)
   arrow.speed(.05)

   # Remove arrow trail
   clearTrail = turtle.Turtle()
   clearTrail.penup()
   clearTrail.goto(clearTrail.xcor()-400, clearTrail.ycor() + 40 )
   clearTrail.pendown()
   clearTrail.color ('deepskyblue')
   clearTrail.pensize (4)
   clearTrail.shape ('arrow')
   clearTrail.setheading(aim)

   if (power <600):
      clearTrail.forward((power-100))
   else:
      clearTrail.forward((480))

   clearTrail.speed(.05)



def determineScores(power, aim):

   # See what score user gets and display it
   if ((aim ==  2) and (537 <= power <= 543)):
      score =  10
      turtle.TK.messagebox.showinfo("Message", "You scored 10!")
   elif ((aim ==  0) and (537 <= power <= 543)):
      score = 10
      turtle.TK.messagebox.showinfo("Message", "You scored 10!")

   elif ((aim == 1 ) and (529<= power <= 550)):
      score =  10
      turtle.TK.messagebox.showinfo("Message", "You scored 10!")

   elif ((aim == 2) and (544<= power <= 590)):
      score =  5
      turtle.TK.messagebox.showinfo("Message", "You scored 5!")

   elif ((aim == 2) and (490 <= power <= 536)):
      score = 5
      turtle.TK.messagebox.showinfo("Message", "You scored 5!")

   elif ((aim == 0) and (544<= power <= 590)):
      score = 5
      turtle.TK.messagebox.showinfo("Message", "You scored 5!")

   elif ((aim == 0) and (490 <= power <= 536)):
      score =  5
      turtle.TK.messagebox.showinfo("Message", "You scored 5!")

   elif ((aim == 6 ) and (525 <= power <= 550)):
      score = 5
      turtle.TK.messagebox.showinfo("Message", "You scored 5!")

   elif ((aim == -4 ) and (525 <= power <= 550)):
      score =  5
      turtle.TK.messagebox.showinfo("Message", "You scored 5!")

   elif ((aim == 4 ) and (500 <= power <= 580)):
      score =  5
      turtle.TK.messagebox.showinfo("Message", "You scored 5!")

   elif ((aim == -2 ) and (500 <= power <= 580)):
      score =  5
      turtle.TK.messagebox.showinfo("Message", "You scored 5!")

   elif ((aim == -1 ) and (495 <= power <= 585)):
      score = 5
      turtle.TK.messagebox.showinfo("Message", "You scored 5!")

   elif ((aim == 3 ) and (495 <= power <= 585)):
      score =  5
      turtle.TK.messagebox.showinfo("Message", "You scored 5!")

   elif ((aim == 5 ) and (510 <= power <= 565)):
      score = 5
      turtle.TK.messagebox.showinfo("Message", "You scored 5!")

   elif ((aim == -3 ) and (510 <= power <= 565)):
      score = 5
      turtle.TK.messagebox.showinfo("Message", "You scored 5!")

   elif ((aim == 1 ) and (490 <= power <= 528)):
      score = 5
      turtle.TK.messagebox.showinfo("Message", "You scored 5!")

   elif ((aim == 1 ) and (551 <= power <= 590)):
      score =  5
      turtle.TK.messagebox.showinfo("Message", "You scored 5!")
   else:
      turtle.TK.messagebox.showinfo("Message", "You missed. You scored 0!")
      score = 0

   # Randomize CPU score
   numbers = [0,5,10]
   cpuScore = random.choice(numbers)

   return score, cpuScore

def sendToClient(score, cpuScore, clientAddress):

   # Send variables back to client
   serverSocket.sendto(repr(score).encode(), clientAddress)
   serverSocket.sendto(repr(cpuScore).encode(), clientAddress)


# Main program
if __name__ == '__main__':

   while True:

      power, aim, windPower, isneg, clientAddress = receiveVariables()
      displayTarget()
      shootArrow(power, aim, isneg)
      score, cpuScore = determineScores(power, aim)
      turtle.done()

      sendToClient(score, cpuScore, clientAddress)