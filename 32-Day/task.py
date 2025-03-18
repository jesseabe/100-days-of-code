#LISTAS E TUPLAS
#Zip é uma função integrada que recebe duas ou mais sequencias e devolve uma lista de tuplas onde cada tupla
#contém um elemento de cada sequência
s = 'abc'
t = [0, 1, 2]
zip(s, t)
#O resultado é um objeto zip que sabe como percorrer os pares

for pair in zip(s, t):
    print(pair)

#Se quiser usar operadores e métodos de lista, você pode usar objeto zip para fazer uma lista
print(list(zip(s, t)))

#Se as sequecias não forem do mesmo comprimento, o resultado tem o comprimento da mais curta
test_list = list(zip('Anne', 'Elk'))
print(test_list)

#Usando a atribuição de tuplas em um loop for para atravessar uma lista de tuplas:
t = [('a', 0), ('b', 1), ('c', 2)]
for letter, number in t:
    print(letter, number)


#has_match recebe duas sequências, t1 e t2 e retorna True se houver um índice i tal que t1[i] == t2[i]
def has_match(t1, t2):
    for x, y in zip(t1, t2):
        if x == y:
            return True
    return False

#Se precisar atravessar os elementos de uma sequência e seus índices, você pode
#usar a função integrada enumerate:
for index, element in enumerate('abc'):
    print(index, element)



#DICIONÁRIOS E TUPLAS 
#Onde cada tupla é um par chave-valor:
d = {'a':0, 'b':1, 'c':2}
t = d.items()
print(t)


tupla_teste = ('a', 'b', 'c')
for index, letter in enumerate(tupla_teste):
    print(index, letter)

tupla_teste_2 = ('d',) + tupla_teste[1:]
print(tupla_teste_2)


#Você pode utilizar uma lista de tuplas para inicializar um novo dicionario
t = [('a', 0), ('c', 2), ('b', 1)]
d = dict(t)
print(d)

#Combinar dict com zip produz uma forma concisa de criar um dicionário:
d = dict(zip('abc', range(3)))
print(d)


import random
teste_numbers = list(range(1, 51))
select_number = random.choice(teste_numbers)
print(select_number)