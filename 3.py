#!/usr/bin/python3

from collections import Counter
from itertools import islice

with open('3.input') as f:
    rucksacks = f.read()

rucksack_list = rucksacks.split("\n")
rucksack_list.pop()

rucksack_gen = iter(rucksack_list)

def _get_priority(item):
    if item.islower():
        return ord(item) - ord('a') + 1
    else:
        return ord(item) - ord('A') + 27

def part1(rucksack_list):
    result = 0

    for r in rucksack_list:
        c1 = set(r[:len(r)//2])
        c2 = set(r[len(r)//2:])

        repeated = list(c1 & c2)[0]

        result += _get_priority(repeated)

    return result

def part2(rucksack_list):
    result = 0

    while True:
        try:
            first, second, third = islice(rucksack_list, 3)
        except ValueError:
            break

        first = set(first)
        second = set(second)
        third = set(third)

        badge = list(first & second & third)[0]

        result += _get_priority(badge)

    return result

print(f"Result 1 {part1(rucksack_list)}")
print(f"Result 2 {part2(rucksack_gen)}")
