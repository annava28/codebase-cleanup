from random import choice
from app.utils import determine_winner

valid_selections = ["rock", "paper", "scissors"] # only have to update in one place

#
# USER SELECTION
#

u = input("Please choose one of 'Rock', 'Paper', or 'Scissors': ").lower()
print("USER CHOICE:", u)
if u not in valid_selections:
    print("OOPS, TRY AGAIN")
    exit()

#
# COMPUTER SELECTION
#

c = choice(valid_selections)
print("COMPUTER CHOICE:", c)

#
# WINNER DETERMINATION
#

winner = determine_winner(u,c)
if winner == u:
    print("YOU WON")
elif winner == c:
    print("COMPUTER WON")
else:
    print("TIE")

