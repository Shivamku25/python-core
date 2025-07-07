import random

friends = ["Ankit","Ravi","Aman","Harsh"]

# 1 options
print(random.choice(friends))

# 2 options
random_index = random.randint(0,3)
print(friends[random_index])