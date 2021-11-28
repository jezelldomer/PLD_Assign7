# Create a program that check if password is valid


import sys

print ("\033[1;35;40m╔═══════════════════════════════════════════════════════════════════════╗")
print ("\033[1;35;40m                 These are the CRITERIA FOR A VALID PASSWORD:\n   \033[0;35;40ma. Greater than 15 letters \n   b. Have at least one capital letter\n   c. Have at least one number\n   d. Have at least one special char (!@#$%^&*`~()-_+=\/{}'[]|;:,<>.?)" )
print ("\033[1;35;40m╚═══════════════════════════════════════════════════════════════════════╝\n")
passw = input("\033[1;37;3mEnter your PASSWORD\n »•»\033[1;37;40m ")

def _passw():
    _letters = 0
    while _letters <= 15:
        for index in passw:
            count = _letters + 1
            _letters += 1
        if count <= 15:
            print("\n\033[0;31;40mYour Password is \033[1;31;3mINVALID. \033[0;31;40m\nOne of the criterias (Criteria A) is not met. \nPlease read the criteria and try again.\n")
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
            print("\n\033[0;31;40mYour Password is \033[1;31;3mINVALID. \033[0;31;40m\nOne of the criterias (Criteria B) is not met. \nPlease read the criteria and try again.\n")
            sys.exit()
    # Criteria C
    digitnum = False
    while not(digitnum):
        for index in passw:
            if index.isdigit() or index.isnumeric():
                digitnum = True
                break
            else:
                continue
        else:
            print("\n\033[0;31;40mYour Password is \033[1;31;3mINVALID. \033[0;31;40m\nOne of the criterias (Criteria C) is not met. \nPlease read the criteria and try again.\n")     
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
            space = '\n\033[0;31;40mYour Password must not contain a space. PASSWORD is \033[1;31;40mINVALID. \033[0;31;40m\nPlease try again.\n'
            print(space)
            sys.exit()    
        else:
            print("\n\033[0;31;40mYour Password is \033[1;31;3mINVALID. \033[0;31;40m\nOne of the criterias (Criteria C) is not met. \nPlease read the criteria and try again.\n")
            sys.exit() 

print (f"\n\033[0;32;40m       Your password is \033[0;33;40m{passw} \033[1;32;40m\n                  Password is VALID. ")
    
    
final = _passw()            
