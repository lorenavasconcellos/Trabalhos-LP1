h = float(input('Digite sua altura: '))
sexo = str(input('Digite seu sexo (F/M): ')).upper()
if sexo == 'F':
    peso = (62.1 * h) - 44.7
if sexo == 'M':
    peso = (72.7 * h) - 58.0
print(f'Seu peso ideal é de {peso:.2f} kg')