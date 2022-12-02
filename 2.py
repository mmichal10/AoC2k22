#!/usr/bin/python3.10

from enum import Enum

WINNING_BONUS = 6
DRAW_BONUS = 3
LOOSING_BONUS = 0

class Shape(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

    # Opponent's shapes
    A = ROCK
    B = PAPER
    C = SCISSORS

    # My shapes for part 1
    X = ROCK
    Y = PAPER
    Z = SCISSORS

def result_part1(opponent, my):
    opponent_shape = Shape[opponent]
    my_shape = Shape[my]

    if opponent_shape == my_shape:
        return DRAW_BONUS + my_shape.value

    if my_shape == Shape.ROCK and opponent_shape == Shape.SCISSORS:
        return WINNING_BONUS + my_shape.value

    if my_shape == Shape.SCISSORS and opponent_shape == Shape.PAPER:
        return WINNING_BONUS + my_shape.value

    if my_shape == Shape.PAPER and opponent_shape == Shape.ROCK:
        return WINNING_BONUS + my_shape.value

    return LOOSING_BONUS + my_shape.value

with open('2.input') as f:
    duels = f.read()

duel_list = duels.split('\n')

duel_list.pop() # The last element is empty

results = [result_part1(*d.split()) for d in duel_list]

print(f"Result: {sum(results)}")
