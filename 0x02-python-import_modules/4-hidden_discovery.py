#!/usr/bin/python3
import hidden_4
names = dir(hidden_4)
names.sort()
for name in names:
    if name.startswith('__'):
        continue
    print("{}".format(name))
