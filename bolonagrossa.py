def calcArea(base, altura):
    area = (base * altura)/2
    return area

base = float(input('digite o raio do triangulo'))
altura = int(input("Digite o lado do tringulo"))
area = calcArea(base, altura)
print(f"A area do quadrado é {area}")