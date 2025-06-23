print("Welcome to the Rollercoaster!")

height = int(input("What is your height in cm ?\n "))
if height >= 120:
    print("You can ride")
    age = int(input("How many year old you are ?\n"))
    if age <= 12:
        bill = 7
        print("Child tickets are $7")
    elif age <= 18:
        bill = 10
        print("Youth tickets are $10")
    elif 18 <= age <= 45:
        bill = 15
        # print("You can ride for free")
        print("Adult tickets are $15")
    else:
        bill = 0
        print("Senior tickets are free")
        # print("Adult tickets are $15")

    wants_photo = input("Do you want a photo taken? Y for Yes or N for No.\n")

    if wants_photo == "Y":  # Corrected indentation here
        bill += 3
    print(f"Your final bill is ${bill}.")  # Using an f-string for cleaner output
else:
    print("Sorry, you are not tall enough to ride.")