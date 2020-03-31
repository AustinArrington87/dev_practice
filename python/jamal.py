
names = ["John", "Mary", "Joe", "Luke"]

def namePrint(names):
    for name in names:
        if len(name) > 3:
            print(name)
    
namePrint(names)

phoneNumbers = {"Joe": "814.404.7040", "austin": "7182133204"}

print(phoneNumbers["Joe"])

print(phoneNumbers["austin"])