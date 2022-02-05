num = int(input('Digite um número para o cálculo do seu faotorial: '))
valor = 1
cont = 1 
while cont <= num:
    valor = valor * cont
    cont = cont + 1 
print(f'O fatorial de {num} é {valor}')