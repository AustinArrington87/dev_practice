# source = https://thispointer.com/python-filter-a-dictionary-by-conditions-on-keys-or-values/


dictOfNames = {
    7: 'Sam',
    8: 'John',
    9: 'Matthew',
    10: 'Riti',
    11: 'Sitli',
    12: 'Sanach'
}

# iterate over and find even key entries

#  have to create new dic to dump the even vals intto 

newDict = dict()

for (key, value) in dictOfNames.items():
    if key % 2 == 0:
        newDict[key] = value

print('Filtered Dictionary: ')
print(newDict)

### variation on above exercise

dictOfNums = {
    "John": '813-132-1234',
    "Joe": '913-231-1234',
    'Bo': '123-123-4124',
    'Jil': '123-123-2131'
}

newNums = dict()

for (key, value) in dictOfNums.items():
    if len(key) % 2 == 0:
        newNums[key] = value
        
print("Filtered Nums: ")
print(newNums)

################################

## That's cool, now checkout how to package into a function with callback 

dictOfNames = {
    7: 'Sam',
    8: 'John',
    9: 'Matthew',
    10: 'Riti',
    11: 'Sitli',
    12: 'Sanach'
}

def filterTheDic(dictObj, callback):
    newDict = dict()
    for (key, value) in dictObj.items():
        if callback((key, value)):
            newDict[key] = value
    
    return newDict

# call function / filter dic to keep elements whose keys are even
newDict = filterTheDic(dictOfNames, lambda elem : elem[0] % 2 == 0)
print("Filtered Dic")
print(newDict)

######### that  was filtering by keys, now let's filter by vals  
newDict = filterTheDic(dictOfNames, lambda elem : len(elem[1]) == 6)
print(newDict)
























