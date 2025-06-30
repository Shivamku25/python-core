import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

word_length = len(chosen_word)
display = "_" * word_length
print(display)

game_over = False
correct_letters = set()

while not game_over:
    guess = input("Guess a letter: ").lower()
    correct_letters.add(guess)
    display = ""
    for letter in chosen_word:
        if letter in correct_letters:
            display += letter
        else:
            display += "_"
    print(display)
    if "_" not in display:
        game_over = True
        print("you Win!")