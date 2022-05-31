#!/usr/bin/python3
print("{}{}".format(0, 1), end='')
for i in range(0, 10):
    for j in range(i+1, 10):
        if (i == 0 and j == 1):
            continue
        print(", {}{}".format(i, j), end='')
print("".format())
