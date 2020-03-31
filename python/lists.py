# returns from beginning to index 4
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

#-1 is excluded in this example
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

# change item in list
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

# check if item in list
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")

# add  item
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

# add item in specific order
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

### REMOVING FROM LIST 
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

# pop - removes from index, removes last item if index not specified
thislist = ["apple", "banana", "cherry"]
thislist.pop(0)
print(thislist)

# delete keyword of index
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

# empty list w clear
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

# COPYING Lists
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

# JOINING LISTS 
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

# can  also join through appending
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
    list1.append(x)

print(list1)

# can also try extend method - to join list 
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

####SORTING
# try sort method 
cars = ['Ford', 'BMW', 'Volvo']
cars.sort()
print(cars)
numbers = [100,5,20,3]
numbers.sort()
print(numbers)

# try  reverse sort
numbers = [100,5,20,3]
numbers.sort(reverse=True)
print(numbers)

# sort by the length of value
def myFunc(e):
    return len(e)

cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']

cars.sort(key=myFunc)
print(cars)

# sort based on list of dics 

def myFunc(e):
    return e['year']

cars = [
  {'car': 'Ford', 'year': 2005},
  {'car': 'Mitsubishi', 'year': 2000},
  {'car': 'BMW', 'year': 2019},
  {'car': 'VW', 'year': 2011}
]

cars.sort(key=myFunc)
print(cars)

# sort by length of vals,  and  in  reverse 
def myFunc(e):
    return len(e)

cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']
cars.sort(reverse=True, key=myFunc)
print(cars)

#####


