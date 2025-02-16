import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")
print(data.head())


#TO DO 1: CREATE A DICTIONARY 
phonetic_dict = {row.letter:row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

#TO DO 2: CREATE A LIST OF THE PHONETIC CODE WORDS FROM A WORD THAT THE USER INPUTS
word = input("Enter a word: ").upper()

# output_list = [phonetic_dict[letter] for letter in word]
# print(output_list)

for letter in word:
    print(phonetic_dict[letter])