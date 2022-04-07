




def to_usd(my_price):
    return f"${my_price:,.2f}"


from random import choice

def determine_winner(user_choice, computer_choice):
    """
    This function considers both the user's choice and the computer's
    randomly generated choice, to determine the winner in a game
    of Rock, Paper, Scissors. 
    Invoking the function: determine_winner(--variable for user's choice--, --variable for computer choice--)
    The inputs should be strings of either "rock", "paper", or "scissors". 

    Sample:

    user = "rock" 
    computer = "scissors"

    determine_winner(user,computer)

    Output: USER WON!     
    """

    #return "paper"
    winners = {
        "rock": {
            "rock": None,
            "paper": "paper",
            "scissors": "rock",
        },
        "paper": {
            "rock": "paper",
            "paper": None,
            "scissors": "scissors",
        },
        "scissors": {
            "rock": "rock",
            "paper": "scissors",
            "scissors": None,
        }
    }
    winning_choice = winners[user_choice][computer_choice]
    return winning_choice
    #return "OOPS"


