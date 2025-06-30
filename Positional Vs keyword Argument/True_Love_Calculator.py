def calculate_love_score():

    print("Welcome to the Love Calculator!")

    # Get the first name from the user
    name1 = input("What is your name? \n")
    # Get the second name from the user
    name2 = input("What is their name? \n")

    # Combine both names and convert to lowercase for case-insensitive comparison
    combined_names = (name1 + name2).lower()

    # Calculate the "TRUE" score
    t = combined_names.count('t')
    r = combined_names.count('r')
    u = combined_names.count('u')
    e = combined_names.count('e')
    true_score = t + r + u + e

    # Calculate the "LOVE" score
    l = combined_names.count('l')
    o = combined_names.count('o')
    v = combined_names.count('v')
    e = combined_names.count('e')
    love_score = l + o + v + e

    # Combine the scores to make a two-digit number
    # Convert scores to string and concatenate them
    love_score_str = str(true_score) + str(love_score)

    # Convert the combined string back to an integer
    final_love_score = int(love_score_str)

    # Print the final love score
    print(f"Your love score is {final_love_score}")

# Call the function to run the love calculator
calculate_love_score()
