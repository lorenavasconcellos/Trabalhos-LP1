array = [33, 9, 3, 18, 20]
tam_arr = len(array)
cont = 0
print(f'Lista {array}')
while cont < tam_arr:
    for i in range(tam_arr - 1):
        if array[i + 1] < array[i]:
            aux = array[i]
            array[i] = array[i + 1]
            array[i + 1] = aux
            cont += 1
print(f'Lista em ordem crescente {array}')