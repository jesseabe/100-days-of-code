
# known = {0:0, 1:1} 

# def fibonacci(n):
#     if n in known: 
#         return known[n]
#     res = fibonacci(n-1) + fibonacci(n-2) 
#     known[n] = res
#     return res

# # Variaveis globais
# # Nesse caso a variavel global não se altera, o problema é que exemple1 cria uma nova variavel local 
# been_called = False
# def exemple1():
#     been_called = True

# #Para atribuir uma variavel local dentro de uma função, é preciso declarar a variavel global antes de usar
# been_called = False
# def exemple2():
#     global been_called
#     been_called = True


# count = 0
# def exemple3():
#     global count
#     count += 1
#     print(count)

# exemple3()



# known = {0:0, 1:1} 
# def exemple4():
#     global known
#     known = dict()
#     print(known)

# exemple4()

# #11.1
# text_file = open("word.txt", "r")
# content = text_file.read()
# print(content)

# list_words = content.split()

# d = {word: i for i, word in enumerate(list_words, 1)}
# print(d)

# #11.2
# notas={'João'   :  9,
#        'Maria'  : 10,
#        'José': 4}

# notas.setdefault('Peart', 8)
# print(notas)


# Criando a funcão para ler as palavras e armazenar em um dicionario
def create_word_dict(filename):
    word_dict = {}
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            word = line.strip()
            word_dict[word] = None
    return word_dict

teste_dict = create_word_dict('word.txt')
print(teste_dict)

def invert_dict(d):
    inverted = {}
    for key, value in d.items():
        inverted.setdefault(value, []).append(key)
    return inverted

teste_inverter = invert_dict(teste_dict)
print(teste_inverter)