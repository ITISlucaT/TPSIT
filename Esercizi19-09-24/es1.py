#Da lista1 = [1, 2, 3, 4, 5], creo lista2 che ha tutti i valori raddoppiati
list1 = [1,2,3,4,5]

list2 = [list1[i]*2 for i in range(len(list1))] #uso il for in linea per moltiplicare ogni campo della lista

print(list2)
#