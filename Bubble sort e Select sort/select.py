array = [33, 9, 3, 18, 20]
print(f'Lista {array}')
for i in range(len(array) - 1):
    min = i
    for c in range(i + 1, len(array)):
        if array[c] < array[min]:
            min = c
    if min != i:
        aux = array[i]
        array[i] = array[min]
        array[min] = aux
print(f'Lista em ordem crescente {array}')