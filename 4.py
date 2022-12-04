#!/usr/bin/python3
import re

with open('4.input') as f:
    cleaning = f.read()

cleaning_list = cleaning.split("\n")
cleaning_list.pop()

result1 = 0
result2 = 0

for c in cleaning_list:
    ranges = re.findall(r"(\d+)-(\d+),(\d+)-(\d+)", c)[0]
    e1_min, e1_max, e2_min, e2_max = [int(v) for v in ranges]

    if (e1_max < e2_min or e2_max < e1_min):
        continue

    result2 += 1

    if (e1_min >= e2_min and e1_max <= e2_max) or (e2_min >= e1_min and e2_max <= e1_max):
        result1 += 1

print(f"Reslut 1 {result1}")
print(f"Reslut 2 {result2}")
