from abc import ABC, abstractmethod

class CompteBancaire(ABC):
    def __init__(self, solde_initial):
        self.solde = solde_initial

    @abstractmethod
    def calculer_interets(self):
        pass

# Sous-classe représentant un compte d'épargne
class CompteEpargne(CompteBancaire):
    def calculer_interets(self):
        taux_interet = 0.05
        interets = self.solde * taux_interet
        return interets

Sous-classe représentant un compte-chèques
class CompteCheques(CompteBancaire):
    def calculer_interets(self):
        # Les comptes de chèques ne génèrent généralement pas d'intérêts
        return 0

# Utilisation des sous-classes pour calculer les intérêts de comptes spécifiques
compte_epargne = CompteEpargne(1000)
interets_epargne = compte_epargne.calculer_interets()
print("Intérêts du compte d'épargne:", interets_epargne)

compte_cheques = CompteCheques(1500)
interets_cheques = compte_cheques.calculer_interets()
print("Intérêts du compte-chèques:", interets_cheques)
