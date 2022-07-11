
def sortowanie(lista):

    i = 0
    k = 0
    
    while i < (len(lista)-1):
        if (lista[i] > lista[i+1]):
            k = lista[i]
            lista[i] = lista[i+1]
            lista[i+1] = k           
        i += 1
    return lista

A = [2,1,5,3,6]
print(sortowanie(A))
