qntdm = int(input('Digite a quantidade de maçãs da compra: '))
if qntdm >= 12:
    valorm = 0.36
else:
    valorm = 0.45
custo = qntdm * valorm
print(f'O custo total da sua compra de {qntdm} maçãs será de R${custo}')