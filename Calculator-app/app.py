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
    print("Add:", add(3, 5))
    print("Sub:", subtract(3, 5))
    print("Mul:", multiply(3, 5))
    print("Div:", divide(5, 3))
    print("Rem:", remainder_divide(5, 3))
    print("Floor:", floor_divide(5, 3))
