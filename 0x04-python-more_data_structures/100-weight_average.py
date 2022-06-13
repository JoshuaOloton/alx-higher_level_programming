#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    weighted_sums = list(map(lambda x: x[0] * x[1], my_list))
    denum = [i[1] for i in my_list]
    return sum(weighted_sums)/sum(denum)
