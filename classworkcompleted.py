# This file has some sample conditionals for you to build and utilize

# Make a variable that asks the user for their name:
name = input("What is your name? ")

# Make a conditional that greets the person with a special greeting
# if their name matches a certain string (could be your name!) and
# gives them a standard greeting otherwise.
if name == "Mr. G":
    print("Yo what's up Mr. G")
else:
    print("Oh, hello", name)

# Make a variable of a tuple of your 3 favorite teachers
favteachers = ("Murad", "Harrison", "Lorenzet")

# Make a conditional that checks if "Guzauckas" is in the tuple,
# and says "Great Choice" if it is. Then check if "Lorenzet" is
# in the tuple, and say "Lorenzet is also a great choice", and
# then say "You could have made better choices" if neither are in
# the tuple.
if "Guzauckas" in favteachers:
    print("Great Choice")
elif "Lorenzet" in favteachers:
    print("Lorenzet is also a great choice")
else:
    print("You could have made better choices")

# Make a float variable that asks the user for their grade in
# this class as a float (0 for 0%, 0.5 for 50%, 1 for 100%, etc.).
grade = float(input("Enter your grade as a float: "))

# Then, print the user's letter grade based on their entered
# numerical grade (A, B, C, D, or F, don't worry about +/-)
if grade >= 0.9:
    print("A")
elif grade >= 0.8:
    print("B")
elif grade >= 0.7:
    print("C")
elif grade >= 0.6:
    print("D")
else:
    print("F")

# Make a variable of a list with your top 4 classes this year
# (in order! The first slot should be your favorite class)
favclasses = ["AP CS Principles", "Intro to CS", "Honors Pre-Calculus", "Math Lab"]

# Make a conditional that looks for our class (AP CS Principles)
# in each slot of the list and make a statement regarding which
# place it got. (i.e., "First place, awesome!", "Second place is
# alright", etc. and "Oh no! We didn't make the list" if it is
# not in the list)
favclass = "AP CS Principles"
if favclasses[0] == favclass:
    print("First place, awesome!")
elif favclasses[1] == favclass:
    print("Second place is alright!")
elif favclasses[2] == favclass:
    print("Third is at least still podium!")
elif favclasses[3] == favclass:
    print("On the list is better than not on the list!")
else:
    print("Oh no! We didn't make the list")
