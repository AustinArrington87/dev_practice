# tuples : https://www.w3schools.com/python/python_tuples.asp

# unchangeable . 

thisTuple = ("apple", "cherry", "banana")
print(thisTuple[0])

# if you need to change tuple, convert to list, then back to tuple
# chage 'cherry' to 'pineapple'
thisTuple = ("apple", "cherry", "banana")
thisTuple = list(thisTuple)
thisTuple[1] = "pineapple"
thisTuple = tuple(thisTuple)
print(thisTuple)

# for loop

for x in thisTuple:
    print(x)
    
# check if present 
if "pineapple" in thisTuple:
    print("Yes, pineapple is in this tuple.")
    
# SET 
# sets are unordered
thisSet = {"apple", "banana", "cherry"}
print(thisSet)

for x in thisSet:
    print(x)