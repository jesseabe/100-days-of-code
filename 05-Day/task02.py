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
    if number % 3 == 0 and number % 5 == 0: 
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)  
