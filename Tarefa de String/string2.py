# Faça o algoritmo estruturado, fluxograma e o programa para saber quantas palavras tem em uma string.

contador = 0
espaço = 0
qntd_palavras = 1
frase = input('Digite uma frase: ')
frase = frase + '\0'
while frase[contador] != '\0':
    if frase[contador] == ' ':
        espaço = espaço + 1
        qntd_palavras = qntd_palavras + 1
    contador = contador + 1
print(f'O número de palavras da sua frase é {qntd_palavras}')