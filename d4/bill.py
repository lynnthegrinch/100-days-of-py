import random
names_string = input("give me the names separated by a comma")
names = names_string.split(",")
print(names)
random_name = random.choice(names)
print(random_name)
print(random_name + " will pay the bill")
