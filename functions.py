lst = input(("Enter a string:"))
lst = lst.lower()
lst = lst.split()
print(lst)
print(list(filter(lambda x: x == x[::-1], lst)))

















