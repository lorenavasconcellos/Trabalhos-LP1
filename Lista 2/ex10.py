nome = str(input('Digite um nome: '))
maiuscula = nome.title()
print(f'{maiuscula}')
pergunta = str(input('Deseja digitar outro nome?(S/N): ')).upper()
while pergunta != 'N':
    nome = str(input('Digite um nome: '))
    maiuscula = nome.title()
    print(f'{maiuscula}')
    pergunta = str(input('Deseja digitar outro nome?(S/N): ')).upper()