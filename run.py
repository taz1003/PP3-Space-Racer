import random

def instructions():
    """
    Shows the player instructions about the rules and obstacles of the game.
    """
    print("It's the year 5056. You race against the AI to see who reaches space 25 first!")
    print("You take turns & roll 1-6, the number corresponding the spaces you move.")
    print("But beaware! There are space obstacles on some spaces that hinders your progress.")
    print("The obstacles & their hindrances are:")
    print("Asteroid Impact = -1 \nGamma ray Blast = -3 \nSupernova Pull = -5 \nNeutron Star Collision = Start over!")
    print("Best of luck Racer!")


def create_board():
    """
    Creates a board for the race that contains a list of 25 spaces 
    with None value, except for some spaces that have disaster effects to
    hinder progress in the race.
    """
    board = [None] * 25
    board[4] = "move_back_1"
    board[7] = "move_back_3"
    board[8] = "move_back_5"
    board[12] = "move_back_1"
    board[15] = "move_back_5"
    board[18] = "move_back_3"
    board[20] = "move_back_1"
    board[23] = "start_over"
    return board


class spaceship:
    """
    Creates an instance Spaceship that adjusts itself as per the steps
    and its position won't go below 0
    """
    def __init__(self, name):
        self.name = name
        self.position = 0
    
    def move(self, steps):
        self.position += steps
        if self.position < 0:
            self.position = 0
    
    def reset(self):
        self.position = 0


def


def main():
    instructions()
    create_board()

main()
