



from random import choice

#
# USER SELECTION
#

options = ["rock", "paper", "scissors"]


u = input("Please choose one of 'Rock', 'Paper', or 'Scissors': ").lower()
print("USER CHOICE:", u)
if u not in options :
    print("OOPS, TRY AGAIN")
    exit()

#
# COMPUTER SELECTION
#

c = choice(options)
print("COMPUTER CHOICE:", c)

#
# DETERMINATION OF WINNER
#

if u == "rock":
    if c == "rock":
        print("It's a tie!")
    if c == "paper":
        print("The computer wins")
    if c == "scissors":
        print("You win!")

if u == "paper":
    if c == "rock":
        print("You win!")
    if c == "paper":
        print("It's a tie!")
    if c == "scissors":
        print("The computer wins")

if u == "scissors":
    if c == "rock":
        print("The computer wins")
    if c == "paper":
        print("You win!")
    if c == "scissors":
        print("It's a tie!")