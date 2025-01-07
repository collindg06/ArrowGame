# This program simulates the client side of a client/server connection using udp that allows the user to play a game of archery against the computer. 

# Imports
import random
from socket import * 

# Choose server / '127.0.0.1'
serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)

def getWind():

    # Set the wind power and directions randomly
    windPower = random.randint(1, 10)
    windDirectional = random.randint(-10, 10)
    if (windDirectional < 0 ):
        windWay = "south"
    else:
        windWay = "north"

    return windPower, windDirectional, windWay

def userInput(windPower, windDirectional, windWay):

    # Give user the wind power        
    print("There is " + str(windPower) + " mph wind power and it is blowing " + str(abs(windDirectional)) + " mph " + windWay )

    # Input validation
    invalidation = 1
    while(invalidation == 1):
        # Get user input
        power = input("How much power do you want to give? ")
        direction = input("Do you want to aim to the north or south? ")
        aim = input("How far to that side do you want to aim it? ")
        invalidation = 2

        if (direction != "north" and direction != "south"):
            print("Please try again.\n")
            invalidation = 1
        elif (not power.isnumeric()):
            print("Please try again.\n")
            invalidation = 1
        elif (not aim.isnumeric()):
            print("Please try again.\n")
            invalidation = 1
        else:
            aim = int(aim)
            power = int(power)
            print("Open the turtle graphics window once it opens.")
            print("\n")
        
    return power, direction, aim

def applyInput(power, direction, aim, windPower, windDirectional):
    
    # User shooting input being set based on conditions
    isneg = False
    if (direction == "south"):
        aim = aim * -1
        isneg = True

    if (power != 0):        
        power = power * windPower

    aim = (aim) + (windDirectional)

    if (aim >= 0):
        isneg = False
    else:
        isneg = True
        
    return aim , power, isneg

def sendToServer(aim , power, isneg, windPower):
    
    # Send variables to server
    clientSocket.sendto(repr(power).encode(), (serverName, serverPort))
    clientSocket.sendto(repr(aim).encode(), (serverName, serverPort))
    clientSocket.sendto(repr(windPower).encode(), (serverName, serverPort))
    clientSocket.sendto(repr(isneg).encode(), (serverName, serverPort))

def receiveVariables():

    # Receive variables back from server
    score, serverAddress = clientSocket.recvfrom(2048)
    cpuScore, serverAddress = clientSocket.recvfrom(2048)

    # Decode variables
    score = score.decode()
    cpuScore = cpuScore.decode()

    # Convert variables to interger
    score = int(score)
    cpuScore = int(cpuScore)

    return score, cpuScore

def determineWinner(score, cpuScore):

    # Show user what the opponent scored
    print("You scored " + str(score) + "!")
    print("Your opponent scored " + str(cpuScore) + "!")

    # Determine who wins and show user
    if (cpuScore > score):
        print("You Lose")
    elif (score > cpuScore):
        print("You Win")
    elif(score == cpuScore):            
        print("Tie Game")

# Main program
if __name__ == '__main__':

    # Explain and start game
    print("Archery \nRules: You will face an opponent. \nInput the power and direction to shoot based off the wind patterns.")
    print("With no wind a perfect shot is 540 power 1 north\n")

    windPower, windDirectional, windWay = getWind()
    power, direction, aim = userInput(windPower, windDirectional, windWay)
    aim , power, isneg = applyInput(power, direction, aim, windPower, windDirectional)
    sendToServer(aim , power, isneg, windPower)
    score, cpuScore = receiveVariables()
    determineWinner(score, cpuScore)

    clientSocket.close()