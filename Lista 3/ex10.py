print('Misto quente (R$4,50) - Código 100\nRefrigerante (R$5,00) - Código 101\nPão de queijo (R$2,00) - Código 102\nSuco (R$6,00) - Código 103')

qntd = int(input('Qual a quantidade de itens que você deseja pedir? '))
valor = 0
cont = 0
itens = []

if qntd == 0:
    print('Nenhum pedido a ser realizado')

else:
    while cont != qntd:
        codigo = int(input('Digite o código do(s) seu(s) pedido(s): '))
        if codigo == 100:
            valor += 4.50
            print('Misto quente')
            itens.append('Misto quente')
        elif codigo == 101:
            valor += 5.00
            print('Refrigerante')
            itens.append('Refrigerante')
        elif codigo == 102:
            valor += 2.00 
            print('Pão de queijo')
            itens.append('Pão de queijo')
        elif codigo == 103:
            valor += 6.00 
            print('Suco')
            itens.append('Suco')
        cont += 1
    
    print(f'Seus pedidos foram: {itens}')
    print(f'O total a ser pago é R${valor}')