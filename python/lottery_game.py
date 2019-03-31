## LOTTERY GAME!! ##

import random

score = 0
name = input("Who is playing? ")
current_round = 0
num1 = 0
num2 = 0
num3 = 0

# Play 5 rounds of the game
## 
for current_round in range(5):
## 


# Start a new round
## 
print("Results for current round " + str(current_round))
## 


# Check if the player won the game and adjust score
## 
if num1 == num2 == num3:
    print("You won! 5 added to score.")
    score += 5
else:
    print("You lost. 1 removed from score".)
    score -= 1
## 


# Randomly select lottery numbers
## 
num1 = random.randInt(1, 9)
num2 = random.randInt(1, 9)
num3 = random.randInt(1, 9)
## 

# Print out the player's score
## 
print("Current score is " + str(score))
## 
