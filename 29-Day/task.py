# Loops e Diciionarios
def histogram(s): 
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1 
        else:
            d[c] += 1 
    return d

h = histogram('brontosaurus')

print(h.get('b', 0))

def print_hist(h):
    for c in h:
        print(c, h[c])

h = histogram('parrot')
print_hist(h)

for key in sorted(h):
    print(key, h[key])



# Busca reversa
def reverse_lookup(d, v): 
    for k in d:
        if d[k] == v: 
            return k
    raise LookupError()

h = histogram('parrot')
k = reverse_lookup(h, 2)
k

def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse

hist = histogram('parrot')
print(hist)

inverse = invert_dict(hist)
print(inverse)


