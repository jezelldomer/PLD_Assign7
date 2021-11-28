# Create a program that check if password is valid


import sys

print ("These are the CRITERIA FOR A VALID PASSWORD:\n   a. Greater than 15 letters \n   b. Have at least one capital letter\n   c. Have at least one number\n   d. Have at least one special char (!@#$%^&*()_+ etc)\n" )
passw = input("Enter your PASSWORD in the space provided below.\n")

def _passw():
    _letters = 0
    while _letters <= 15:
        for index in passw:
            count = _letters + 1
            _letters += 1
        if count <= 15:
            print("\nYour Password is INVALID. \nOne of the criterias (Criteria A) is not met. \nPlease read the criteria and try again.\n")
            sys.exit
        else:
            break
    # Criteria B
    capital = False 
    while not(capital):
        for index in passw:
            if index.isupper():
                capital = True
                break
            else:
                continue
        if index.isupper() == True:
            None
        else:
            print("\nYour Password is INVALID. \nOne of the criterias (Criteria B) is not met. \nPlease read the criteria and try again.\n")
            sys.exit()
    # Criteria C
    digitnum = False
    while not(digitnum):
        for index in passw:
            if index.isdigit():
                digitnum = True
                break
            else:
                continue
        if (index.isdigit()) == True:
            None
        else:
            print("\nYour Password is INVALID. \nOne of the criterias (Criteria C) is not met. \nPlease read the criteria and try again.\n")     
            sys.exit()
    # Criteria D
    spcletter = False
    while not(spcletter):
        for index in passw:
            if index in "!@#$%^&*`~()-_+=\/{}'[]|;:,<>.?":
                spcletter = True
                break
            elif index.isspace():
                break
            else:
                continue
        if index in "!@#$%^&*`~()-_+=\/{}'[]|;:,<>.?":
            None
        elif index.isspace():
            space = '\nYour Password must not contain a space. PASSWORD is INVALID. \nPlease try again.\n'
            print(space)
            sys.exit()    
        else:
            print("\nYour Password is INVALID. \nOne of the criterias (Criteria C) is not met. \nPlease read the criteria and try again.\n")
            sys.exit() 

print (f"Your password is {passw}. Password is VALID. ")
    
    
final = _passw()            
