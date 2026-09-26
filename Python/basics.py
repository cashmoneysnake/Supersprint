## Write one .py file that declares and prints an int, float, str, bool, list, tuple, dict and set

name = "Elijah" ## string
number = 1 ##int
number_F = 1.0 ##float
truth_Value = True ##bool
people = ['me', 'myself', 'i'] ##list
characters = ('sasuke', 'gohan') ## tuple
fav_User = {"password", "cool"} ## dict
optimal_Fruit = {'bannanas', 'strawberry'} ##set


##print(" string = ",name, "\n","int = ", number,"\n", "float = ",number_F,"\n", "boolean = ", 
##      truth_Value,"\n", "list = ", people,"\n", "tuple = ", characters,"\n", "dict = ", fav_User,"\n","set = ", optimal_Fruit)




##Write a script that takes a number from input() and classifies it with if / elif / else.

inputting = input("choose any whole number") 
big_Small_Or_Not = int(inputting)


if big_Small_Or_Not >= 10000:
    print("Your number is big")
elif big_Small_Or_Not <= 10:
    print("Your number is small")
else:
    print("Your number is neither")