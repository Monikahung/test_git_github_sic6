a = 2
b = 0

def penjumlahan(a,b):
    return a + b

def pengurangan(a,b):
    return a - b

def perkalian(a,b):
    return a * b

def pembagian(a,b):
    if b == 0:
        return 0
    return a / b

result = pembagian(a, b)
print(result) # type: ignore