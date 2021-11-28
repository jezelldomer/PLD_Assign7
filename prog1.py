# Create a program that ask for a sentence as input
# Display the number of words, vowels and consonants in the input 

count_ = input("Enter your sentence here: ")

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
print (count_)
print ("Output: ")

Statement = '\nWords: {} \nVowels: {} \nConsonant: {}\n'.format(words, vwls, cons)
print(Statement)
