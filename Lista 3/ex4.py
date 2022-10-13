totalkm = float(input('Digite o total de quilômetros percorridos: '))
total_abast = float(input('Digite o total que foi abastecido: '))
media = totalkm / total_abast
print(f'A média de consumo foi de {media:.2f}Km/L')
while totalkm > 0:
    totalkm = float(input('Digite o total de quilômetros percorridos: '))
    total_abast = float(input('Digite o total que foi abastecido: '))
    media = totalkm / total_abast
    print(f'A média de consumo foi de {media:.2f}Km/L')
print('FIM')