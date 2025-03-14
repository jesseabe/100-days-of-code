#Tuplas -> São imutáveis
#Sintaticamente, uma tupla é uma lista de valores separados por vírgulas:
t = ('a', 'b', 'c', 'd', 'e')
#OBS: Um único valor entre parenteses não é uma tupla. Para ser uma tupla precisa incluir vírgula no final. Ex:
t1 = 'a',
print(type(t1))

#Outra forma de criar tuplas é usar o argumento tuple()
t = tuple('lupins')
print(t)

print(t[0])
print(t[1:4])

#Como tuplas são imutáveis, você não pode alterar um dos elementos, mas pode substituir uma tupla por outra
t = ('A',) + t[1:]
print(t)

#Para dividir um endereço de email em um nome de usuário e um domínio:
addr = 'monty@python.org'
uname, domain = addr.split('@')
print(uname)
print(domain)

#TUPLAS COMO VALORES DE RETORNO
#Ex: Se você quiser dividir dois numeros inteiros e calcular o quociente e o resto é possível calcular ambos ao mesmo tempo
#A função integrada divmod toma dois argumentos e devolve uma tupla de dois valores: o quociente e o resto.
t = divmod(7, 3)
print(t)

#para guardar os valores separadamente
quot, rem = divmod(7, 3)
print(quot)
print(rem)

#Função que retorna uma tupla
def min_max(t):
    return print(min(t), max(t))

min_max('alphavile')


#TUPLAS COMO ARGUMENTOS DE COMPRIMENTO VARIÁVEL
def printall(*args):
    print(args)

printall(1, 2.5, '65', 'teste')

#O complemento de dividir é espalhar 
#Exemplo, o divmod recebe exatamente dois argumentos, ele não funciona com uma tupla
t = (7, 3)
#print(divmod(t))
#No entanto, se espalhar a tupla, aí funciona:
print(divmod(*t))


#Escreva uma função chamada sumall que receba qualquer número de argumentos e retorne a soma deles:
# def sumall(*args):
#     somador = 0
#     for i in args:
#         somador = i + somador 
#     return somador 

def sumall(*args):
    return sum(args)

print(sumall(5, 5, 5, 15))