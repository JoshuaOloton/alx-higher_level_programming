#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    list_c = []
    if len(tuple_a) > 2 or len(tuple_b) > 2:
        tuple_a = tuple_a[:2]
        tuple_b = tuple_b[:2]
    if len(tuple_a) < 2 or len(tuple_b) < 2:
        for i in range(len(tuple_a), 2):
            tuple_a += (0,)
        for j in range(len(tuple_b), 2):
            tuple_b += (0,)
    for i in range(2):
        list_c.append(tuple_a[i] + tuple_b[i])
    return tuple(list_c)
