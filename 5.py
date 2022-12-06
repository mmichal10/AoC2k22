#!/usr/bin/python3
import re
from itertools import islice, tee

with open('5.input') as f:
    data = f.read()

data = data.split("\n")
data.pop()
data = iter(data)

def transpose_and_filter(stacks, ids):
    ret = stacks
    ret.insert(0, ids)

    # Transpose
    ret = [[stacks[j][i] for j in range(len(stacks))] for i in range(len(stacks[0]))]

    # Filter out columns with spaces and square brackets
    ret = [
            # Filter out empty spaces from lower stacks
            [x for x in s if x.isalpha()]
            for s in ret if s[0].isnumeric()
        ]

    return ret

horizontal_stacks = []

while True:
    l = next(data)
    if '[' not in l:
        break

    horizontal_stacks.append(l)

stacks_count = int(l[-1])
ids = l

data, data_copy = tee(data)

stacks = transpose_and_filter(horizontal_stacks, ids)

stacks_copy = [[e for e in stack] for stack in stacks]

def _get_instruction_details(instruction):
    matches = re.findall(r"move (\d+) from (\d+) to (\d+)", instruction)[0]

    count, src, dst = matches

    src = int(src) - 1
    dst = int(dst) - 1
    count = int(count)

    return src, dst, count

def part1(stacks, data):
    for instruction in data:
        if len(instruction) == 0:
            continue

        src, dst, count = _get_instruction_details(instruction)

        while count:
            elem = stacks[src].pop(0)
            stacks[dst].insert(0, elem)
            count -= 1

    return ''.join([x[0] for x in stacks])

def part2(stacks, data):
    for instruction in data:
        if len(instruction) == 0:
            continue

        src, dst, count = _get_instruction_details(instruction)

        stacks[dst] = stacks[src][:count] + stacks[dst]
        stacks[src] = stacks[src][count:]

    return ''.join([x[0] for x in stacks])


print(f"Result 1: {part1(stacks, data)}")
print(f"Result 2: {part2(stacks_copy, data_copy)}")
