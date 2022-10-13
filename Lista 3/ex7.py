binario = str(input('Digite um número binário para transformar em decimal: '))
dec = 0
listabin = []

for c in range (len(binario)):
    listabin.append(int(binario[c]))
    c += 1 
pot = (len(listabin) -1)

for c in range (len(listabin)):
    listabin[c] = listabin[c] * (2 ** pot)
    dec = dec + int(listabin[c])
    pot -= 1 
    
print(f'O número binário {binario} em decimal é {dec}')