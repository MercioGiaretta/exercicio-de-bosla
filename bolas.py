def calcArea(lado):
    area = (lado * lado)
    return area

lado = int(input("Digite o lado do quadrado"))
area = calcArea(lado)
print(f"A area do quadrado é {area}")