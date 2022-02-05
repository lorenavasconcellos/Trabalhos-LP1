kminicial = float(input('Digite a marcação do Km no início do dia: '))
kmfinal = float(input('Digite a marcação do Km no final do dia: '))
litrosgas = float(input('Digite a quantidade de litros de gasolina gastos no dia: '))
valorrecebido = float(input('Digite o valor total recebido dos passageiros: '))
valorgas = 2.75
mediacons = (kmfinal - kminicial) / litrosgas
gasto = (valorgas / mediacons) * (kmfinal - kminicial)
lucro = valorrecebido - gasto
print(f'Sua média de consumo de gasolina por Km foi de {mediacons} Km/L\nSeu gasto total com gasolina foi de R${gasto}\nSeu lucro (líquido) total foi de R${lucro}')
