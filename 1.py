#!/usr/bin/python3.10

with open('1.input') as f:
    calories_lists_raw = f.read().split("\n\n")
    calories_str_list = [cal.split() for cal in calories_lists_raw]

    summed_calories = [
        sum([int(s) for s in calories_str])
        for calories_str in calories_str_list
    ]

    print(max(summed_calories))
