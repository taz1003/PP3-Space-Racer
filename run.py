import random

def create_board():
    """
    Creates a board for the race that contains a list of 25 spaces 
    with None value, except for some spaces that have disaster effects to
    hinder progress in the race.
    """
    board = [None] * 25
    board[4] = "asteroid_impact"
    board[7] = "gamma_ray_burst"
    board[8] = "supernova_pull"
    board[12] = "asteroid_impact"
    board[16] = "supernova_pull"
    board[20] = "gamma_ray_burst"
    board[23] = "blackhole_impact"
    return board


