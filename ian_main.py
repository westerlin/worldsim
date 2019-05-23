import random

names = open("male.txt").readlines()
names = [n.strip('\n') for n in names]

i = 0
name = None
while name != "James Ryan":
    i += 1
    first_name = random.choice(names)
    last_name = random.choice(names)
    name = first_name + " " + last_name

print(" - Name:", name);
print (" - Iterations: ", i)
