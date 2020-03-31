def myFunction():
    print("Hello from my function")

myFunction()

# pass arguments into function 
def nameGenerator(firstName):
    print(firstName + " Foojooley")

nameGenerator("John")
nameGenerator("Gary")

#  add multiple arguments into function 
def fullName(firstName, lastName):
    print(firstName + " " + lastName)

fullName("John", "Jolly")
fullName("Boston", "Barrington")

#########
# what if you dont know number of args
def myFunction(*kids):
    print("The youngest child is " + kids[2])

myFunction("Tory", "Simon", "Kiely")

## default parameter value 
def myFunction(country = "USA"):
    print("I am from " + country)

myFunction("Japan")
myFunction()

#####################
# let function return value 
def myFunction(x):
    return 5 * x

print(myFunction(3))
print(myFunction(4))
    
## recursion - function can call itself
def tri_recursion(k):
    if(k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result

print("\n\nRecursion Example Results")
tri_recursion(5)

#### Lambda
# https://www.w3schools.com/python/python_lambda.asp

def multiplyNums(num1, num2):
    resultNum = num1*num2
    print(resultNum)
    return resultNum

multiplyNums(2,3)





