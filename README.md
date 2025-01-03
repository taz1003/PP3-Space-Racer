# Ultimate Space Racer
Ultimate Space Racer is a Python Terminal game, which runs in the Code Institute mock terminal on Heroku.

Users take on the role of humanity's champion in a high-stakes space race against an alien opponent, which is played by the computer. The fully text-based game provides a fun and engaging way to experience exciting gameplay through a simple Python interface.

[Here is the live version of my project](https://ultimate-space-racer-9ee32e5b59c8.herokuapp.com/)

## How To Play
There are 30 total spaces in this race starting from space 1.
- __Objective :__
The user as the player, has to be the first to reach space 30 while navigating a board filled with hazards that can hinder their progress.

- __Turns :__
The game alternates turns between the player and an alien opponent.

- __Roll the Dice :__
On each turn, the player and the alien roll a virtual die to move forward by 1 to 6 spaces.

- __Obstacles :__
Certain spaces contain hazards that push the player back or reset the player's progress:
    - Asteroid Impact - Move back 1 space.
    - Gamma Ray Blast - Move back 3 spaces.
    - Blackhole Pull - Move back 5 spaces.
    - Neutron Star Collision - Reset to space 15.

- __Win Condition :__
 The first to reach space 30 wins the race and determines humanity’s fate.

## Controls
- Type y to roll the dice and continue the race.
- Type n to quit the game and concede victory to the aliens.

## Features
### Existing Features
- __Interactive Gameplay :__
Turn-based mechanics allow for alternating moves between the player and the alien. In this way, there can only be one winner, negating the need for any tie mechanics.

- __Randomized Rolls :__
The dice rolls are completely random, ensuring each playthrough is unique.

- __Obstacle Mechanics :__
Special hazardous board spaces add an element of unpredictability, making each game suspenseful.

- __Customizable Turn Continuation :__
The player can choose to continue or quit the game at any turn.

- __Exciting Win Condition :__
The game requires a precise dice roll to land exactly on space 30 to win. Even if the dice roll exceeds space 30, the player will remain in the game, adding an extra layer of suspense and excitement.

- __Clear Feedback :__
Informative prompts and messages provide clarity about the current state of the game.

- __Error Handling :__
Built-in error handling and input validation ensures smooth gameplay by validating user inputs and managing unexpected issues, such as invalid commands other than the fixed controls or out-of-range moves.

- __Emojis for Immersion :__
Emojis like 🚀, 👾 and 🟢 are used to represent the spaceships and turns, adding a touch of personality and fun to the game experience

### Future Features

- __Enhanced Obstacles :__
Introduce new hazards like "Wormhole Teleportation" that randomly relocate players.

- __Multiplayer Mode :__
Allow two human players to compete against each other, inserting their own names instead of the fixed names given by me.

- __Power-Ups :__
Add special spaces where the player can gain advantages, like immunity to hazards for a few turns.

- __Dynamic Difficulty :__
Adjust alien difficulty based on the player's performance.

- __Visual Enhancements :__
Replace text-based feedback with a graphical interface for more immersive gameplay.

## Data Model
I decided to structure the game around the following components:
1. __Spaceship Class :__
    - __Attributes__ 
        - __name -__ Name of the spaceship (fixed as Player or Alien).
        - __position -__ Current position of the spaceship on the board.
    - __Methods__
        - __move(steps) -__ Updates the spaceship’s position based on the dice roll.
        - __start_fifteen() -__ Resets the spaceship’s position to space 15 after encountering a "Neutron Star Collision."

2. __Board__
    - A list of 31 spaces with predefined obstacles :
    move_back_1, move_back_3, move_back_5, start_over.

3. __Game Logic__
    - Functions for handling turns, checking for obstacles, rolling the dice, and determining the winner.
    - Turn-based mechanics ensure fair competition between the player and the alien.

4. __Input Validation__
    - Robust input validation for user choices (e.g., continuing or quitting the game).

## Testing
I have manually tested the project by doing the following:
 - Passed the code through [PEP8 Linter](https://pep8ci.herokuapp.com/) and confirmed that there are no errors.
 
 - An unrelated problem is presented that says "print() strings are too long" which is strictly a [PEP8 Linter](https://pep8ci.herokuapp.com/) issue and does not affect the python code whatsoever.
 
 - Tested in my local terminal and the Code Institue Heroku terminal with no issue.

## Bugs
### Solved Bugs
- During the project, an error occured that said "'space' is not associated with any value". I fixed it by first ensuring the spaceship position does not exceed board length, then associating space with spaceship's current position through the board parameter in the __check_obstacles__ function.

- While playing the game, the alien's turn was not ending. I fixed the issue by passing accurate parameters in the __step_counter__ function.

- The game was not ending as neither of the enitities could reach 30. I fixed it by increasing the size of the board list by 1 which accounted for the __spaceship.position - 1 < len(board)__ code snippet in the __check_obstacles__ function.

### Remaining Bugs
- No bugs remaining.

### Validator Testing
- No errors were returned from [PEP8 Linter](https://pep8ci.herokuapp.com/).

## Deployment
This project was deployed using Code Institute's mock terminal for Heroku.

The steps to deploy are as follows:
- Fork or clone this GitHub repository
- Create a new Heroku app
- Set the buildpacks to __Python__ and __NodeJS__ in that order
- Link the Heroku app to the GitHub repository
- Click on manual __Deploy__

## Credits
- The errors in the __check_obstacles__ function were fixed and some codes were refactored after extensive research on Google, YouTube and my Code Institue lessons
- The creation of the __handle_turn__ function was inspired by some coding videos from the YouTube channel [Code Coach](https://www.youtube.com/@CodeCoachh/videos)

## Acknowledgements
- My Mentor for the continuous helpful feedback.
- The Code Institute Tutor Support for their support.