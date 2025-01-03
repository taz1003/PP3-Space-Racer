import random


def instructions():
    """
    Shows the player instructions about the rules and obstacles of the game.
    """
    print("💥 It's the year 5056.\nYou race against the aliens,")
    print("in an attempt to save humanity,")
    print("to see who reaches from space 1 to space 30 first.")
    print("---------------------------------------------------")
    print("You take turns & roll 1-6 as in the spaces you move.")
    print("But beaware! There are obstacles on some")
    print("spaces that hinder your progress.")
    print("---------------------------------------------------")
    print("The obstacles are:")
    print("Asteroid Impact = Go back 1 space")
    print("Gamma Ray Blast = Go back 3 spaces")
    print("Blackhole Pull = Go back 5 spaces")
    print("Neutron Star Collision = Start from space 15")
    print("---------------------------------------------------")

def start():
    """
    Gives the player a choice to start the game or not
    """
    choice = input("Start the race? Type 'y' to start & 'n' to quit: \n").lower()

    if choice == "n":
        print("You let the alien take over humanity!")
        quit()
    elif choice == "y":
        print("You chose to race for humanity's sake!")
    else:
        print("Invalid choice. Let's try again.")
        start()


def create_board():
    """
    Creates a board for the race that contains a list of 31 spaces
    with None value, except for some spaces that have obstacles to
    hinder progress in the race.
    """
    board = [None] * 31
    board[4] = "move_back_1"
    board[8] = "move_back_3"
    board[10] = "move_back_5"
    board[12] = "move_back_1"
    board[16] = "move_back_5"
    board[18] = "move_back_3"
    board[20] = "move_back_5"
    board[23] = "move_back_1"
    board[25] = "move_back_3"
    board[27] = "start_over"
    return board


class spaceship:
    """
    Creates an instance Spaceship that moves itself as per the steps
    and its position won't go below 0
    """
    def __init__(self, name):
        self.name = name
        self.position = 0

    def move(self, steps):
        self.position += steps
        # Does not allow the spaceship to go below board length
        if self.position < 0:
            self.position = 0

    def start_fifteen(self):
        self.position = 15


def ask_to_continue():
    """
    Asks for yes or no input for game continuation. Anything else typed will
    raise a ValueError.
    """
    while True:
        try:
            response = input("Continue the race? (type 'y' or 'n'): \n").lower()
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
    # Sets an artificial capping when step count exceeds max length
    # of the board so that the game doesn't end, preventing instant win
    if spaceship.position > len(board) - 1:
        spaceship.position = len(board) - 2

    # Sets values for spaces
    if spaceship.position - 1 < len(board):
        space = board[spaceship.position]
    else:
        space = None

    # Checks for obstacles
    if space == "start_over":
        print(f"!{spaceship.name} is hit with Neutron Star Collision! Start from 15")
        spaceship.start_fifteen()
    elif space == "move_back_5":
        print(f"!{spaceship.name} is hit with Blackhole Pull! Move back 5 spaces")
        spaceship.move(-5)
    elif space == "move_back_3":
        print(f"!{spaceship.name} is hit with Gamma Ray Blast! Move back 3 spaces")
        spaceship.move(-3)
    elif space == "move_back_1":
        print(f"!{spaceship.name} is hit with Asteroid Impact! Move back 1 spaces")
        spaceship.move(-1)


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
    if player.position >= 30:
        return player.name
    elif alien.position >= 30:
        return alien.name
    else:
        return None


def handle_turn(player, alien, board):
    """
    Handles the turn based functionality between the player and the
    alien(computer) and returns the winner. Turn-based logic ensures
    that only one entity can win per game loop.
    """
    count = 0
    while True:
        count += 1
        print(f"==> {player.name} is at space {player.position} VS {alien.name} is at space {alien.position}")
        print("---------------------------------------------------")
        print(f"🟢 Turn {count} - Player's turn: ")
        # Closes the game
        if ask_to_continue() is False:
            print("You forsake humanity!")
            quit()
        # Counts player's steps
        step_counter(player, board)
        winner = check_winner(player, alien)
        if winner:
            return winner

        print("Alien's turn: ")
        # Counts alien's steps
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

    # Value input
    board = create_board()
    player = spaceship("🚀 Player")
    alien = spaceship("👾 Alien")

    winner = handle_turn(player, alien, board)
    if winner:
        print(f"{winner} wins the space race!")


# Calls main() function
main()
