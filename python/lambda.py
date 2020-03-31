x = lambda a : a + 10
print(x(5))

x = lambda a, b: a * b
print(x(5, 6))

x = lambda a, b, c: a + b + c
print(x(5, 6, 3))

# nestsing lambda inside another function

def myFunc(n):
    return lambda a : a * n

myDoubler = myFunc(2)
print(myDoubler(11))