#!/usr/bin/python3.10

from collections import Counter

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
        c1 = list(r[:len(r)//2])
        c2 = list(r[len(r)//2:])

        c1 = list(set(c1))
        c2 = list(set(c2))

        repeated = Counter(c1 + c2).most_common(1)[0][0]

        result += _get_priority(repeated)

    return result

print(f"Result 1 {part1(rucksack_gen)}")
