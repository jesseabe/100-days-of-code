import random 

# Generate the word 
words_list = ["uva", "pessego", "banana", "abacaxi", "bergamota", "laranja", "melao", "amora"]
chosen_word = random.choice(words_list).lower()
print(chosen_word)

#Input the letter
letter = input("Digite uma letra: ")
print(letter)

word_lenght = len(chosen_word)
print(word_lenght)

placeholder = ""

for position in range(word_lenght):
    placeholder += "_"
print(placeholder)

