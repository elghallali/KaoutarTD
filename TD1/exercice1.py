def est_valide(chaine, sequence):
    # On vérifie que la chaîne et la séquence ne sont pas vides
    if not chaine or not sequence:
        return False
    # On vérifie que la chaîne et la séquence ne contiennent que des "a", "t", "g" ou "c"
    if not all(c in "atgc" for c in chaine) or not all(c in "atgc" for c in sequence):
        return False
    return True

def saisie():
    # On effectue une saisie en boucle jusqu'à ce qu'elle soit valide
    while True:
        chaine = input("Entrez une chaîne d'ADN : ")
        sequence = input("Entrez une séquence d'ADN : ")
        if est_valide(chaine, sequence):
            return chaine, sequence
        else:
            print("La chaîne ou la séquence saisies sont invalides. Veuillez réessayer.")

def proportion(chaine, sequence):
    # On compte le nombre d'occurrences de la séquence dans la chaîne
    occurrences = chaine.count(sequence)
    # On renvoie la proportion de séquence dans la chaîne
    return 100*occurrences / len(chaine)

def afficher(chaine, sequence,proportion):
    print(f"chaîne : {chaine}")
    print(f"séquence : {sequence}")
    print(f"Il y a {proportion:.2f} % de '{sequence}' dans votre chaîne.")

# On effectue une saisie valide
chaine, sequence = saisie()

# On calcule la proportion de séquence dans la chaîne
proportion = proportion(chaine, sequence)

# On affiche le résult
afficher(chaine, sequence, proportion)
