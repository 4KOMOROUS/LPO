# data una lista, si determina il massimo e il mininmo

def max_min_lista(lista):
    results = [max(lista), min(lista)]
    return results

lista = [1, 6, 2, 8, 9, 5, 0, 9]
results = max_min_lista(lista)
print("max lista: ", results[0], "\nmin lista: ", results[1])
