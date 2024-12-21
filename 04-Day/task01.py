import random
#Lists
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia"]

states_of_america.extend(["Angelaland", "Jack Bauer Land"])

#1st Option
print(random.choice(states_of_america))

#2nd Option
random_index = random.randint(0,4)
print(states_of_america[random_index])

print(len(states_of_america)-1)

#---------------------------#
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
dirty_dozen = [fruits, vegetables]
 
print(dirty_dozen[1][1])
