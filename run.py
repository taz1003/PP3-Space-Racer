import random

def instructions():
    """
    Shows the player instructions about the rules and obstacles of the game.
    """
    print("It's the year 5056.\nYou race against an alien, in an attempt to save humanity, to see who reaches space 25 first!")
    print("You take turns & roll 1-6, the number corresponding the spaces you move.")
    print("But beaware! There are space obstacles on some spaces that hinders your progress.")
    print("The obstacles & their hindrances are:")
    print("Asteroid Impact = -1 \nGamma Ray Blast = -3 \nSupernova Pull = -5 \nNeutron Star Collision = Start over!")

def start():
    """
    Gives the player a choice to start the game or not
    """
    choice = input("Do you wish start the race? (y/n) ").lower()
    
    if choice== "n":
        print("You let the alien take over humanity!")
        quit()
    elif choice == "y":
        print("You chose to race for humanity's sake!")
    else:
        print("Invalid choice. Let's try again.")
        start()
        

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
        elif self.position > 25:
            self.position = 25
    
    def reset(self):
        self.position = 0


def check_obstacles(spaceship, board):
    """
    Checks for the obstacles throughout the board.
    If found, they affect the spaceship.
    """
    space = board[space.position - 1]

    if space== "start_over":
        print(f"{spaceship.name} is with a Neutron Star Collision! Start Over!")
        spaceship.reset()
    elif space == "move_back_5":
        print(f"{spaceship.name} is hit with Supernova Pull! Move back 5 spaces")
        spaceship.move(-5)
    elif space == "move_back_3":
        print(f"{spaceship.name} is hit with Gamma Ray Blast! Move back 3 spaces")
        spaceship.move(-3)
    elif space == "move_back_1":
        print(f"{spaceship.name} is hit with Asteroid Impact! Move back 1 spaces")
        spaceship.move(-1)
    
    print(f"{spaceship.name} is at position {spaceship.position}")


def step_counter(spaceship, board):
    """
    Rolls a random number between 1 - 6, moves the spaceship and checks for 
    obstacles.
    """
    steps = random.randint(1, 6)
    print(f"{spaceship.name} rolled a {steps}")
    spaceship.move(steps)
    check_obstacles(spaceship, board)

def check_winner(player, alien):
    """
    Checks for the side that reaches the max length of the board first.
    Returns the winner.
    """
    if player.position >= 25:
        return player.name
    elif alien.position >= 25:
        return alien.name
    else:
        return None

def main():
    instructions()
    start()
    print("Best of luck Racer!")
    create_board()
    

main()
