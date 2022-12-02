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

class ExpectedResult(Enum):
    LOST = 1
    DRAW = 2
    WIN = 3

    X = LOST
    Y = DRAW
    Z = WIN

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

def _get_beating_shape_value(shape):
    match shape:
        case Shape.ROCK:
            return Shape.PAPER.value
        case Shape.PAPER:
            return Shape.SCISSORS.value
        case Shape.SCISSORS:
            return Shape.ROCK.value

def _get_beaten_shape_value(shape):
    match shape:
        case Shape.ROCK:
            return Shape.SCISSORS.value
        case Shape.PAPER:
            return Shape.ROCK.value
        case Shape.SCISSORS:
            return Shape.PAPER.value

def result_part2(opponent, expected_result):
    opponent_shape = Shape[opponent]
    expected_result = ExpectedResult[expected_result]

    if expected_result == ExpectedResult.DRAW:
        return DRAW_BONUS + opponent_shape.value

    if expected_result == ExpectedResult.WIN:
        return WINNING_BONUS + _get_beating_shape_value(opponent_shape)

    if expected_result == ExpectedResult.LOST:
        return LOOSING_BONUS + _get_beaten_shape_value(opponent_shape)

with open('2.input') as f:
    duels = f.read()

duel_list = duels.split('\n')

duel_list.pop() # The last element is empty

results1 = [result_part1(*d.split()) for d in duel_list]
results2 = [result_part2(*d.split()) for d in duel_list]

print(f"Result 1: {sum(results1)}")
print(f"Result 2: {sum(results2)}")
