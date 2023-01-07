# TD 1 de Kaoutar

## Exercice 1 :
Un programme principal saisit une chaîne d'ADN valide et une séquence d'ADN valide (valide signifie qu'elles ne sont pas vides et sont formées exclusivement d'une combinaison arbitraire de "a", "t", "g" ou "c").

Écrire une fonction valide qui renvoie vrai si la saisie est valide, faux sinon.

Écrire une fonction saisie qui effectue une saisie valide et renvoie la valeur saisie sous forme d'une chaîne de caractères.

Écrire une fonction proportion qui reçoit deux arguments, la chaîne et la séquence et qui retourne la proportion de séquence dans la chaîne (c'est-à-dire son nombre d'occurrences).

Le programme principal appelle la fonction saisie pour la chaîne et pour la séquence et affiche le résultat.

Exemple d'affichage :
```
chaîne : attgcaatggtggtacatg
séquence : ca
Il y a 10.53 % de "ca" dans votre chaîne.
```

## Exercice 2 :
Soit la classe Date définie par le diagramme de classe UML suivant :


```mermaid
classDiagram
    class Date{
    +jour: int
    +mois : int
    +annee : int
    }
```


1. Implémenter cette classe en Python.
2. Dans la méthode de construction de la classe, prévoir un dispositif pour éviter les dates impossibles (du genre 32/14/2020). Dans ce cas, la création doit provoquer une erreur, chose possible grâce à l’instruction raise (documentation à rechercher !).
3. Ajouter une méthode `__repr__` permettant d’afficher la date sous la forme "25 janvier 1989". Les noms des mois seront définis en tant qu’attribut de classe à l’aide d’une liste.
4. Ajouter une méthode `__lt__` qui permet de comparer deux dates.
5. L’expression d1 < d2 ( d1 et d2 étant deux objets de type Date ) doit grâce à cette méthode renvoyer True ou False.

## Exercice 3 : Classe Compte bancaire :

1. Créer une classe Python nommée `CompteBancaire` qui représente un compte bancaire, ayant pour attributs : `numeroCompte` (type numérique ) , `nom` (nom du propriétaire du compte du type chaine), `solde`.
2. Créer un `constructeur` ayant comme paramètres : `numeroCompte`, `nom`, `solde`.
3. Créer une méthode `Versement()` qui gère les versements.
4. Créer une méthode `Retrait()` qui gère les retraits.
5. Créer une méthode `Agios()` permettant d'appliquer les agios à un pourcentage de 5 % du solde
6. Créer une méthode `afficher()` permettant d’afficher les détails sur le compte
7. Donner le code complet de la classe CompteBancaire.

# TD 2 de Kaoutar

## Exercice 1

1. Définir une `classe Book` avec les attributs suivants : `Title`, `Author` (Nom complet), `Price`.
2. Définir un constructeur ayant comme attributs : `Title`, `Author`, `Price`.
3. Définir la méthode `View()` pour afficher les informations d'une instance object Book.
4. Ecrire un programme pour `tester la classe Book`.

## Exercice 2

Write a program to build a simple Student Management System using Python which can perform the following operations:

1. `Accept` : This method takes details from the user like name, roll number, and marks for two different subjects.
2. `Display` : This method displays the details of every student.
3. `Search` : This method searches for a particular student from the list of students. This method will ask the user for roll number and then search according to the roll number
4. `Delete` : This method deletes the record of a particular student with a matching roll number.
5. `Update` : This method updates the roll number of the student. This method will ask for the old roll number and new roll number. It will replace the old roll number with a new roll number.

## Exercice 3

Décrire ce que fait ce programme et son output :

```python
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

```
