print("Sorting a list of numbers")

def sorting(lista):
    l = len(lista)
    for i in range(l - 1):
        for j in range(l):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

lst = list(map(int, input("Enter numbers separated by spaces: ").split()))
print("your list: ", lst)
print("sorted list: ", sorting(lst))