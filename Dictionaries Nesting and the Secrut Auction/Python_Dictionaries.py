programming_dictionary = {
    "Bug": "An error in a program that prevents the program form running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

#print(programming_dictionary["Function"])

programming_dictionary["Loop"] = "The action of doing somthing over and over again."

empty_dictionary = {}
# wipe an existing dictionary

#programming_dictionary = {}
#print(programming_dictionary)
# edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer."
#print(programming_dictionary)
# loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])