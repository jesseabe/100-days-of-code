# Range Function with For Loop

# for number in range(1, 11):
#     print(number)
 

 # Solve the Gauss Challenge
total = 0

for number in range(1, 101):
    total += number
print(total)


#FizzBuzz Game
for number in range(1, 101):  # Loop from 1 to 100 (inclusive)
    if number % 3 == 0 and number % 5 == 0:  # Divisible by both 3 and 5
        print("FizzBuzz")
    elif number % 3 == 0:  # Divisible by 3
        print("Fizz")
    elif number % 5 == 0:  # Divisible by 5
        print("Buzz")
    else:
        print(number)  # Not divisible by 3 or 5
