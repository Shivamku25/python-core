import random
stages = ['''
  +---+
  |   | 
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   | 
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   | 
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   | 
  O   |
 /|   |
      |
      |
=========
''', ''' 
  +---+
  |   | 
  O   |
  |   |
      |
      |
=========
''', '''    
  +---+
  |   | 
  O   |
      |
      |
      |
=========
''', '''    
  +---+
  |   | 
      |
      |
      |
      |
=========
''']

word_list = ["aardvark", "baboon", "camel"]
lives = 6
chosen_word = random.choice(word_list)
print(chosen_word)

word_length = len(chosen_word)
display = "_" * word_length
print(display)

game_over = False
correct_letters = set()

while not game_over:
    guess = input("Guess a letter:").lower()
    correct_letters.add(guess)
    display = ""
    for letter in chosen_word:
        if letter in correct_letters:
            display += letter
        else:
            display += "_"
    print(display)

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("You Lose.")

    if "_" not in display:
        game_over = True
        print("You Win.")

    print(stages[lives])