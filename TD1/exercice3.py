class CompteBancaire:
    def __init__(self, numeroCompte, nom, solde):
        self.numeroCompte = numeroCompte
        self.nom = nom
        self.solde = solde
    
    def Versement(self, montant):
        self.solde += montant
    
    def Retrait(self, montant):
        self.solde -= montant
    
    def Agios(self):
        self.solde *= 0.95
    
    def afficher(self):
        print(f"Numéro de compte : {self.numeroCompte}")
        print(f"Nom du propriétaire : {self.nom}")
        print(f"Solde : {self.solde}")

compte1 = CompteBancaire(12345, "John Doe", 1000)
compte1.Versement(500)
compte1.Retrait(200)
compte1.Agios()
compte1.afficher()