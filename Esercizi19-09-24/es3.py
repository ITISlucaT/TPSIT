#Dizionario: {"a": 1, "b": 2, "c": 3}, scambio la posizione tra chiave e valore

dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {j : i for i, j in dict1.items()} #dict1.items() mi restituisce una lista di tuple, che vengono assegnate ad i (chiavi)e a j(valori), assegnango valori al dizionario swappo valori con chiavi

print(dict2)
