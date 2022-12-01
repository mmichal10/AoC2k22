#!/usr/bin/python3.10

with open('1.input') as f:
    calories_lists_raw = f.read()

calories_lists_raw = calories_lists_raw.split("\n\n")

calories_str_list = [cal.split() for cal in calories_lists_raw]

summed_calories = [
    sum([int(s) for s in calories_str])
    for calories_str in calories_str_list
]

summed_calories.sort(reverse=True)

print(f"Max value {summed_calories[0]}")
print(f"Sum of top 3 {sum(summed_calories[:3])}")
