from math import sqrt
xA = float(input('Insira a coordenada xA: '))
xB = float(input('Insira a coordenada xB: '))
yA = float(input('Insira a coordenada yA: '))
yB = float(input('Insira a coordenada yB: '))
distXY = sqrt((xA - xB)**2) + ((yA - yB)**2)
print(f'A distância entre esses dois pontos é de {distXY}')