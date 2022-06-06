#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    list_c = []
    for i in range(2):
        list_c.append(tuple_a[i] + tuple_b[i])
