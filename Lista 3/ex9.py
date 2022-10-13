salario = float(input('Digite o valor do salário para reajuste: '))
if salario <= 2000:
    reajuste = salario + (salario * 50/100)
elif salario > 2000 and salario <= 5000:
    reajuste = salario + (salario * 40/100)
elif salario > 5000 and salario <= 7000:
    reajuste = salario + (salario * 20/100)
elif salario > 7000:
    reajuste = salario + (salario * 10/100)
print(f'O salário com reajuste será R${reajuste:.2f}')