#!/usr/bin/python3
print("{}{}".format(0, 1), end='')
for i in range(10):
    for j in range(i+1, 10):
        print(", {}{}".format(i, j), end='')
print("".format())
