def SameZeroOne(tab, n):
    somme = 0
    fin = -1
    for i in range(0, n-1):
        somme = -1 if (tab[i]== 0 ) else 1

        # parcourir les sous tableaux
        for j in range(i + 1, n):
            somme = somme + (-1) if (tab[j] == 0) else somme + 1
            if (somme == 0 and fin < j-i + 1):
                fin = j - i + 1
                debut = i
    
    if (fin == -1):
        print("tableau n'exist pas")
    else:
        print(debut, " à ", debut+ fin -1)
    return fin

T = [0, 0, 1, 1, 0]
SameZeroOne(T, len(T))