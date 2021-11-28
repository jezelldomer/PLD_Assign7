# Create a program that ask for a sentence as input
# Display the number of words, vowels and consonants in the input 

count_ = input("\n\033[1;37;40mEnter the sentence you want In the space provided:\n»•»  \033[1;36;40m ")

def _words(num_words = 1, num_vwls = 0, num_cons = 0):
    loop_str = count_.upper()
    for index in loop_str:
        if index in " ":
            num_words += 1
        elif index in "AEIOU":
            num_vwls += 1
        elif index in "BCDFGHJKLMNPQRSTVWXYZ":
            num_cons += 1
    return num_words, num_vwls, num_cons

words, vwls, cons = _words()
print ("\n╔═══════════╗")
print ("\033[1;32;40m   Output: ")
print ("╚═══════════╝")

Statement = '\n\033[1;31;40m»•»   Words: {} \n\033[1;33;40m»•»   Vowels: {} \n\033[1;35;40m»•»   Consonant: {}\n'.format(words, vwls, cons)
print(Statement)
