# Create a program that ask for a sentence as input
# Display the number of words, vowels and consonants in the input 

count_char = input("Enter your sentence here: ")

def _words(num_words = 1, num_vwls = 0, num_cons = 0):
    loop_str = count_char.upper()
    for index in loop_str:
        if index in " ":
            num_words += 1
        elif index in "aeiou":
            num_vwls += 1



