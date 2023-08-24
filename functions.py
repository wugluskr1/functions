lst = input(("Enter a string:"))
lst = lst.lower()
lst = lst.split()
print(lst)
lst = list(filter(lambda x: len(x) != 1, lst))
print(lst)
print(list(filter(lambda x: x == x[::-1], lst)))

















