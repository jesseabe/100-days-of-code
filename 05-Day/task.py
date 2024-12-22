import random

letters = ['a', 'b', 'c', 'd']
numbers = ['0', '1', '2', '3', '4', '5']
symbols = ['!', '#', '$', '%', '&']


#Password Generator 
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n "))

#Easy Level
# password = " "

# for char in range(0, nr_letters):
#     password += random.choice(letters)

# for char in range(0, nr_symbols):
#     password += random.choice(symbols)

# for char in range(0, nr_numbers):
#     password += random.choice(numbers)

# print(password)

# Hard Level
password_list = []

for char in range(0, nr_letters):
    password_list.append(random.choice(letters))

for char in range(0, nr_symbols):
    password_list.append(random.choice(symbols))

for char in range(0, nr_numbers):
    password_list.append(random.choice(numbers))

print(password_list)
random.shuffle(password_list)
print(password_list)

#Turn list in string
password = ""
for char in password_list:
    password += char
print(f"Your password is {password}")