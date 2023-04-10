b = int(input("Digite o valor da base: "))
h = int(input("Digite o valor da altura: "))

def perimetro(b, h):
    return int(b + b + h + h)

def area(b, h):
    return int(b * h / 2)

print("Perímetro:",perimetro(b, h))
print("Área:",area(b, h))
