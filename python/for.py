# source: https://www.w3schools.com/python/python_for_loops.asp

# loop through string\
for x in "banana":
    print(x)

# break statement
fruits = ["banana", "cherry", "grape"]

for x in fruits:
    print(x)
    if x == "cherry":
        break
        
# switch it . up 

for x in fruits:
    if x == "cherry":
        break
    
    print(x)
    
# continue statement -  to skip current iteration
for x in fruits:
    if x == "cherry":
        continue
    print(x)

    
# range 
for x in range(2,6):
    print(x)

# change the increment of sequence from default of 1 

for x in range(0,30,3):
    print(x)


for x in range(1,6):
    print(x)
else:
    print("Finally finished")

# nested FOR loops 
adj = ["red", "big", "tasty"]
fruit = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x,y)

    
    
    
    
    
    
    
    
    






