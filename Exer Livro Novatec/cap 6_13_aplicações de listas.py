L = [1, 8, 2, 7, 5, 12, 15, 5, 10]
P = []
I = []
for e in L:
    if e % 2 == 0:
        P.append(e)
    else:
        I.append(e)
print("Pares :", P)
print("Ímpares :", I)
    
