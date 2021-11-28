# Create a program that check if password is valid


import sys

print ("These are the CRITERIA FOR VALID PASSWORD:\n   a. Greater than 15 letters \n   b. Have at least one capital letter\n   c. Have at least one number\n   d. Have at least one special char (!@#$%^&*()_+ etc)\n" )
passw = input("Enter your PASSWORD in the space provided below.\n")

def _passw():
    _letters = 0
    while _letters <= 15:
        for index in passw:
            count = _letters + 1
            _letters += 1
        if count <= 15:
            print("\nYour Password is INVALID. \nCriteria A. - \"Greater than 15 characters\" is not met. \nPlease read the criteria and try again.\n")
            sys.exit
        else:
            break

    while capital:
        for index in _passw:
            if index.isupper():
                _capital == true
                None 
             
