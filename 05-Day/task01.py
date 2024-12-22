# fruits = ["Apple", "Peach", "Pear"]
# #Loop exemple
# for fruit in fruits:
#     print(fruit)
#     print(fruit + " pie")

import random

student_scores = []

while len(student_scores) < 20:
    number = random.randint(80, 150)
    student_scores.append(number)

print(student_scores)

max_score = 0 

for score in student_scores:
    if score > max_score:
        max_score = score
print(max_score)