#def cat(name):
#    print("Your cat's name is " + str(name))
#
#name = "John"
#
#cat(name)
#
#def addOne(number):
#    number = int(number)
#    number = number+1
#    if number >= 7:
#        return "Number out of range"
#    else:
#        return number
#
#print(addOne("5"))
#print(addOne("6"))
#
#names = ["John", "Mary", "Joe", "Luke"]
#
#def namePrint(names):
#    for name in names:
#        if len(name) > 3:
#            print(name)
#
#namePrint(names)


############################

#phoneBook = {"John": "123-456-7823", "Gary": "123-231-2342"}
#
##print(phoneBook["John"])
#
#def printNum(name):
#    for name in phoneBook:
#        return phoneBook[name]
#    
#printNum(name)

#############

names = ["John", "Joe", "Mary"]

def printName(names):
    for name in names:
        print(name)

printName(names)
    
phoneBook = [{"John": "123-234-5422"}, {"Joe": "814-123-4252"}, {"Mary": "123-421-7321"}]


def printPhoneBook(phoneBook):
    for entry in phoneBook:
        print(entry)
        

printPhoneBook(phoneBook)
    




