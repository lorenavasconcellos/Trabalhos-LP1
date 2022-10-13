a = float(input('Digite o coeficiente a: '))
b = float(input('Digite o coeficiente b: '))
c = float(input('Digite o coeficiente c: '))

delta = (b ** 2) - 4 * a * c

if a == 0:
    print('O valor de a deve ser diferente de 0')
elif delta < 0:
    print('Não possui raízes reais')
else:
    x1 = (-b + delta ** (1/2)) / (2 * a)
    x2 = (-b - delta ** (1/2)) / (2 * a)

    print(f'Suas raízes são: {x1} e {x2}')

pergunta = str(input('Deseja realizar um novo cálculo?(S/N) ')).upper()

while pergunta == 'S':
    a = float(input('Digite o coeficiente a: '))
    b = float(input('Digite o coeficiente b: '))
    c = float(input('Digite o coeficiente c: '))

    delta = (b ** 2) - 4 * a * c

    if a == 0:
        print('O valor de a deve ser diferente de 0')
    elif delta < 0:
        print('Não possui raízes reais')
    else:
        x1 = (-b + delta ** (1/2)) / (2 * a)
        x2 = (-b - delta ** (1/2)) / (2 * a)

        print(f'Suas raízes são: {x1} e {x2}')
    pergunta = str(input('Deseja realizar um novo cálculo?(S/N) ')).upper()
else:
    print('FIM')