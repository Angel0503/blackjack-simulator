
from .Carte import Carte
from random import shuffle
               
class PaquetDeCartes():
    def __init__(self, liste_cartes):
        """Méthode qui initialise l'attributs d'un jeu de carte"""
        self.contenu = liste_cartes
    
    def __repr__(self):
        """Méthode qui affiche le jeu complet avec l'appel de la fonction print"""
        affichage=""
        for i in range(len(self.contenu)):
            affichage=affichage + str(self.contenu[i]) + "\n"
        return affichage
        
    def taille(self):
        """Méthode qui renvoie le nombre de carte du jeu"""
        return len(self.contenu)
    
    def est_vide(self):
        """Méthode qui renvoie true si le jeu est vide sinon False"""
        if self.contenu == []:
            return True
        else:
            return False
    
    def battre(self):
        """Méthode qui mélange les cartes"""
        shuffle(self.contenu)
        
    def tirer_carte(self):
        """Méthode qui permet de tirer une carte du paquet de carte"""
        if self.est_vide():
            return None
        else:
            carte = self.contenu[0]
            del self.contenu[0]
            return carte
        
    def ajouter_carte(self, carte):
        """Méthode qui ajoute une carte au paquet"""
        self.contenu.append(carte)
        
    def distribuer(self):
        """Distribuer 2 cartes au joueur et 1 a la banque """
        self.battre()
        c1 = self.tirer_carte()
        c2 = self.tirer_carte()
        carteBanque = self.tirer_carte()
        
        return c1, c2, carteBanque