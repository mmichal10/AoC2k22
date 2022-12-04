#!/usr/bin/python3

with open('4.input') as f:
    cleaning = f.read()

cleaning_list = cleaning.split("\n")
cleaning_list.pop()

result1 = 0
result2 = 0

for c in cleaning_list:
    e1, e2 = c.split(',')

    e1_min, e1_max = e1.split('-')
    e1_min, e1_max = int(e1_min), int(e1_max)

    e2_min, e2_max = e2.split('-')
    e2_min, e2_max = int(e2_min), int(e2_max)

    if (e1_max < e2_min or e2_max < e1_min):
        continue

    result2 += 1

    if (e1_min >= e2_min and e1_max <= e2_max) or (e2_min >= e1_min and e2_max <= e1_max):
        result1 += 1

print(f"Reslut 1 {result1}")
print(f"Reslut 2 {result2}")
