#Debugging e solving the problem
def my_function():
    for i in range(1, 21):
        print(i)
        if i == 20:
            print("You got it")

my_function()

#-------------------------#
#Fix the error
from random import randint

dice_images = ["1", "2", "3", "4"]
dice_num = randint(0, 3)
print(dice_images[dice_num])
print(dice_num)

#-------------------------#
#Fix the error
year = int(input("What's your year of birth? "))

if year > 1980 and year < 1994:
    print("You are a millennial.")
elif year >= 1994:
    print("You are a Gen Z.")
else:
    print("You are Baby Boomer.")

#-------------------------#
#Fix the error
try:
    age = int(input("How old are you: "))
except ValueError:
    print("You have typed in an invalid number. Please, try again with a numeric response such as 15.")
    age = int(input("How old are you: "))

if age >= 18:
    print(f"You can drive at age {age}")
else:
    print("You can't drive")