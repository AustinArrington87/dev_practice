# source : https://www.w3schools.com/python/python_while_loops.asp
i = 1

while i < 6:
    print(i)
    i += 1

# try break statement - to stop loop 

i = 1

while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

# using the continue statement - stop the current iteration and continue w the rest 

i = 1

while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

#########  else 

while i < 6:
    print(i)
    i += 1
else:
    print("i no longer less than 6")