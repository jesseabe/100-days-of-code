def foo(a, b=4, c=6):
    print(a, b, c)

foo(1)



def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum

print(add(3, 5, 6))



def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)



class Car:

    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw["model"]

my_car = Car(make = "Nissan", model = "GT-R")
print(my_car.model)



def bar(spam, eggs, toast='yes please!', ham=0):
    print(spam, eggs, toast, ham)
 
bar(1, 2)



def bar(spam, eggs, toast='yes please!', ham=0):
    print(spam, eggs, toast, ham)
 
bar(toast='nah', spam=4, eggs=2)


def all_aboard(a, *args, **kw): 
    print(a, args, kw)
 
all_aboard(4, 7, 3, 0, x=10, y=64)