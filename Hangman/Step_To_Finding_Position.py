import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(chosen_word)
#TODO-1: create a "placeholder" with the same number of blanks as the chosen word.

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)
guess =input("Guess a letter :").lower()
#TODO-2: create a "display" that the puts the guess letter in the right position and_in the rest of the string.

display = ""
for letter in chosen_word:
    if letter == guess:
        display += letter
    else:
        display += "_"
print(display)



