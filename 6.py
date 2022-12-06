#!/usr/bin/python3
import re
from itertools import islice, tee

MARKER_LEN = 4
MESSAGE_MARKER_LEN = 14

with open('6.input') as f:
    data = f.read()

data = data.split("\n")[0]


def decode(data, marker_len):
    marker = [next(data) for _ in range(marker_len - 1)]

    for i, s in enumerate(data):
        if not s in marker and len(marker) == len(set(marker)):
            return i + marker_len

        marker.pop(0)
        marker.append(s)


print(f"Part 1: {decode(iter(data), MARKER_LEN)}")
print(f"Part 2: {decode(iter(data), MESSAGE_MARKER_LEN)}")
