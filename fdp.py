def calcArea(raio):
    area = pi * (raio * raio)
    return area

raio = float(input('digite o raio do circulo:'))
pi = 3.14
area = calcArea(raio)
print(f'A area do circulo com raio é {area}')