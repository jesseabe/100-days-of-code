#Capítulo 11: Dicionarios

eng2sp = dict()
eng2sp['one'] = 'uno'
print(eng2sp)

eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
#A função len é compatível com dicionarios e retorna o número de pares
print(len(eng2sp))

# O operador in funciona em dicionários: ele acusa se aparece como chave
print('one' in eng2sp)
print('uno' in eng2sp)

#Para verificar se algo aparece como um valor em um dicionario
vals = eng2sp.values()
print('uno' in vals)


#Suponha que você receba uma string e queira contar quantas vezes cada letra aparece nela

test = "Uma string e quer contar quantas letras tem nela"
contador = 0

print(len(test))

for i in test:
    contador += 1
print(contador)