import random
from random import randint
up = int(input("How many random integers you want? "))
def rand_int_gen(up):
    count = up
    _nums = []
    while count > 0:
        _nums.append(random.randint(1,100))
        count -= 1
    return _nums

run_input = rand_int_gen(up)

print(run_input)

def running_sum_counter(my_list):
    sum_list = [0] * len(my_list)
    sum_list[0] = my_list[0]
    for i in range(1, len(my_list)):
        sum_list[i] = sum_list[i-1] + my_list[i]
    return sum_list

print(running_sum_counter(run_input))
