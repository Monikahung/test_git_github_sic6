a = 10
b = 20

def newton1(a,b):
    return a ** 2 + b ** 2

def newton2(a,b):
    return (a / b) + (a ** 2 + b ** 2)

def newton3(a,b):
    return (a * b) + (b / a) + (3.14 * a ** 2)