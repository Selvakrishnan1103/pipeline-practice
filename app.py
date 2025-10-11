from operator import __not__


def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a, b):
    return a / b 

def remainder_divide(a,b):
    return a % b

def floor_divide(a,b):
    return a // b 

if __name__ == "__main__":
    print("Add", add(3, 5))
    print("Sub", add(3, 5))
    print("Mul", add(3, 5))
    print("Div", add(5, 3))
    print("Rem", add(5, 3))
    print("Floor", add(5, 3))
