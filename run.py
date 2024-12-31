import random

def instructions():
    """
    Shows the player instructions about the rules and obstacles of the game.
    """
    print("It's the year 5056.\nYou race against the aliens, in an attempt to save humanity, to see who reaches space 25 first!")
    print("You take turns & roll 1-6, the number corresponding the spaces you move.")
    print("But beaware! There are space obstacles on some spaces that hinder your progress.")
    print("The obstacles & their hindrances are:")
    print("Asteroid Impact = Go back 1 space \nGamma Ray Blast = Go back 3 spaces \nBlackhole Pull = Go back 5 spaces \nNeutron Star Collision = Start over!")

def start():
    """
    Gives the player a choice to start the game or not
    """
    choice = input("Do you wish start the race? Type 'y' to start & 'n' to quit: ").lower()
    
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
    board = [None] * 26
    board[4] = "move_back_1"
    board[7] = "move_back_3"
    board[8] = "move_back_5"
    board[12] = "move_back_1"
    board[15] = "move_back_5"
    board[18] = "move_back_3"
    board[20] = "move_back_5"
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


def ask_to_continue():
    """
    Asks for yes or no input for game continuation. Anything else typed will
    raise a ValueError.
    """
    while True:
        try:
            response = input("Continue the race? (y/n): ").lower()
            if response == "n":
                return False
            elif response == "y":
                return True
            else:
                raise ValueError("Invalid input. Please type 'y' or 'n'.")
        except ValueError as e:
            print(e)


def check_obstacles(spaceship, board):
    """
    Checks for the obstacles throughout the board.
    If found, they affect the spaceship.
    """
    # Set maximum position value to the max length of the board which
    # accounts for the zero-based indexing of the board list.
    if spaceship.position > len(board) - 1:
        spaceship.position = len(board) - 1
    
    #Set values for spaces
    if spaceship.position - 1 < len(board):
        space = board[spaceship.position -1]
    else:
        space = None

    if space == "start_over":
        print(f"!! {spaceship.name} is hit with Neutron Star Collision! Start Over!")
        spaceship.reset()
    elif space == "move_back_5":
        print(f"!! {spaceship.name} is hit with Blackhole Pull! Move back 5 spaces")
        spaceship.move(-5)
    elif space == "move_back_3":
        print(f"!!{spaceship.name} is hit with Gamma Ray Blast! Move back 3 spaces")
        spaceship.move(-3)
    elif space == "move_back_1":
        print(f"!! {spaceship.name} is hit with Asteroid Impact! Move back 1 spaces")
        spaceship.move(-1)
    
    print(f"{spaceship.name} is at space {spaceship.position}")


def step_counter(spaceship, board):
    """
    Rolls a random number between 1 - 6, moves the spaceship and checks for 
    obstacles.
    """
    steps = random.randint(1, 6)
    print(f"-- {spaceship.name} rolled a {steps} --")
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


def handle_turn(player, alien, board):
    """
    Handles the turn based functionality between the player and the
    alien(computer) and returns the winner.
    """
    while True:

        print(f"==> {player.name} is at space {player.position} VS {alien.name} is at space {alien.position} <==")
        print("Player's turn: ") 
        if ask_to_continue() == False:
            print("You forsake humanity!")
            quit()
        
        step_counter(player, board)
        winner = check_winner(player, alien)
        if winner:
            return winner
        
        print("Alien's turn: ")
        step_counter(alien, board)
        winner = check_winner(player, alien)
        if winner:
            return winner


def main():
    """
    Runs all the game functions.
    """
    instructions()
    start()
    print("Best of luck Racer!")

    board = create_board()
    player = spaceship("Player")
    alien = spaceship("Alien")

    winner = handle_turn(player, alien, board)
    if winner:
        print(f"{winner} wins the space race!")
      
main()