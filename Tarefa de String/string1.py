# Faça o algoritmo estruturado, fluxograma e o programa para inverter uma string, ou seja, o último carácter se torna o primeiro, o penúltimo se torna o segundo e assim por diante.

contador = 0
letras = 0
frase = input('Digite uma frase para ser invertida: ')
frase = frase + '\0'
while frase[contador] != '\0':
    contador = contador + 1
    letras = contador
frase_invertida = frase[letras]
letras = letras - 1
while letras >= 0:
    frase_invertida = frase_invertida + frase[letras]
    letras = letras - 1
print (f'{frase_invertida}')