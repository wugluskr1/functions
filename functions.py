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