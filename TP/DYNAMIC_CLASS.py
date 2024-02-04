# class CompteBancaire:
#     def __init__(self, numero_compte, solde_initial):
#         self.numero_compte = numero_compte
#         self.solde = solde_initial

# compte1 = CompteBancaire("12345", 1000)

# compte1.type_compte = "Epargne"
# compte1.taux_interet = 0.05

# print(compte1.numero_compte)
# print(compte1.solde)
# print(compte1.type_compte)
# print(compte1.taux_interet)

class PortefeuilleInvestissement:
    def __init__(self, nom):
        self.nom = nom

# Création dynamique d'attributs pour suivre les informations supplémentaires du portefeuille
portefeuille1 = PortefeuilleInvestissement("Portefeuille 1")
portefeuille1.actions = ["Depense", "Revenu"]
portefeuille1.obligations = ["Dollars US"]

# Affichage des attributs du portefeuille (y compris les attributs ajoutés dynamiquement)
print(portefeuille1.nom)        # Affiche "Portefeuille 1"
print(portefeuille1.actions)    # Affiche ["AAPL", "GOOGL", "MSFT"]
print(portefeuille1.obligations) # Affiche ["US Govt", "Corporate"]
