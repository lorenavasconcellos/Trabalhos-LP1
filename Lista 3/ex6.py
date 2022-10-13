dec = int(input('Digite um número decimal para ser transformado em binário: '))
restos = []
binario = ''
while dec > 0:
    resto = dec % 2
    restos.append(resto)
    dec = dec // 2
for c in range (len(restos) -1, -1, -1):
    binario += str(restos[c])
print(f'O número {dec} em binário é {binario}')