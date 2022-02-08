comp = float(input('Digite o comprimento do cômodo: '))
larg = float(input('Digite a largura do cômodo: '))
h = float(input('Digite a altura do cômodo: '))
vol = comp * larg * h 
caixa = 1.5
qntd = vol / caixa
print(f'Cabem {qntd} caixas de azulejo no seu cômodo.')