def add(*args) :
    print(args[0])
    sum = 0
    for n in args :
        sum += n
    print(sum)


add(3,5,6,9)

def calculate(n, **kwargs) :
    print(kwargs)
    print(kwargs["add"])
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)



calculate(5 , add = 3 , multiply = 5 )

class Car:
    def __init__(self, **kwargs):
        self.color = kwargs.get("color")
        self.model = kwargs.get("model")
        self.makeyear = kwargs.get("year")


my_car = Car(year = 2020)
print(my_car.model)
