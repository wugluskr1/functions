from random import randint
import math
import time

def new_func():
    lst = input(("Enter a string:"))
    lst = lst.lower()
    lst = lst.split()
    print(lst)
    lst = list(filter(lambda x: len(x) != 1, lst))
    print(list(filter(lambda x: x == x[::-1], lst)))


new_func()


def outer(n): 
    sp = [n] 
    def inner():
        nonlocal n
        while n > 1:
            if n % 2 == 0:
                n = n // 2
            else:
                n = 3 * n + 1
            sp.append(n)
        for i in sp:
            print(i, end = ' ')
    inner()

outer(int(input(("Enter a number:" ))))

def time_of_function(function):
    def wrapped(*args):
        start_time = time.perf_counter_ns()
        res = function(*args)
        print("Время:",time.perf_counter_ns() - start_time)
        return res
    return wrapped

@time_of_function
def sqrt():
    j = int(input("\nВведите число символов в списке: "))
    numbers =  [randint(1, 100) for i in range(j)]
    print(numbers)
    while True:
        try:
            flag = int(input("\nВведите направление округления (0 - в меньшую сторону 1 - в большую): "))
            if flag == 0 or flag == 1: 
                break
        except ValueError:
            print('\nНеправильный ввод, повторите')
    if flag == 0:
        numbers = list(map(lambda x: math.floor(x**(0.5)), numbers))
    else:
        numbers = list(map(lambda x: math.ceil(x**(0.5)), numbers))
    return numbers
print(sqrt())

