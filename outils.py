import tkinter as tk
from random import shuffle

def coupPredict(mainBanque, maMain):
    stay = "stay"
    hit = "hit"
    double = "double"
    split = "split"

    """Cas du double"""
    if maMain[0].egal(maMain[1]):
        print("double")
        """Double 2 ou 3"""
        if maMain[0] == "2" or maMain[0] == "3":
            if mainBanque < "8":
                return split
            else:
                return hit
        
        """Double 4"""
        if maMain[0] == "4":
            if mainBanque == "5" or mainBanque == "6":
                return split
            else:
                return hit
        
        """Double 5"""
        if maMain[0] == "5":
            if mainBanque == "10" or mainBanque == "A":
                return hit
            else:
                return double
        
        """Double 6"""
        if maMain[0] == "6":
            if mainBanque < "7":
                return split
            else:
                return hit

        """Double 7"""
        if maMain[0] == "7":
            if mainBanque < "8":
                return split
            else:
                return hit

        """Double 9"""
        if maMain[0] == "9":
            if mainBanque == "7" or mainBanque == "10" or mainBanque == "A":
                return stay
            else:
                return split
        
        """Double 10"""
        if 10 in maMain:
            return split
        
        """Double A ou 8"""
        if maMain[0] == "A" or maMain[0] == "8":
            return split
        
    """Cas de A + autre"""
    if "A" in maMain:
        """A + 2 ou 3"""
        if "2" in maMain or "3" in maMain:
            if mainBanque == "5" or mainBanque == "6":
                return double
            else:
                return hit
        
        """A + 4 ou 5"""
        if "4" in maMain or "5" in maMain:
            if mainBanque == "5" or mainBanque == "6" or mainBanque == "4":
                return double
            else:
                return hit
        
        """A + 6"""
        if "6" in maMain:
            if "2" < mainBanque < "7":
                return double
            else:
                return hit

        """A + 7"""
        if "7" in maMain:
            if mainBanque == "2" or mainBanque == "7" or mainBanque == "8":
                return split
            if mainBanque < "7" and mainBanque != "2":
                return double
            else:
                return hit
        
        """A + 7 ou 8 ou 9 ou 10"""
        if "7" in maMain or "8" in maMain or "9" in maMain or "10" in maMain:
            return stay
    
    """Tous les autres cas"""
    #maMain = str(additionCarte(maMain))
    maMain = maMain[0].add(maMain[1])
    maMain = str(maMain)
    mainBanque = str(mainBanque)
    """Ligne 17 +"""
    if "16" < maMain < "20":
        return stay
    
    """Ligne de 16 a 13"""
    if "12" < maMain < "17":
        if "1" < mainBanque < "7":
            return stay
        else : 
            return hit

    """Ligne 12"""
    if maMain == "12":
        if "3" < mainBanque < "7":
            return stay
        else:
            return hit

    """Ligne 11"""
    if maMain == "11":
        if mainBanque == "A":
            return hit
        else :
            return double

    """Ligne 10"""
    if maMain == "10":
        if mainBanque == "A" or mainBanque == "10":
            return hit
        else :
            return double

    """Ligne 9"""
    if maMain == "9":
        if "2" < mainBanque < "6":
            return double
        else :
            return hit
    
    """Ligne 5 a 8"""
    if "4" <maMain < "9":
        return hit

class Carte():
    def __init__(self, hauteur, couleur):
        """Initialise les attibuts de l'objet"""
        self.hauteur = hauteur
        self.couleur = couleur
        
    def __repr__(self):
        """Créé la méthode du retour de la fonction print de l'objet"""
        haut={2:"2",3:"3",4:"4",5:"5",
                 6:"6",7:"7",8:"8",9:"9",
                 10:"10",11:"10",12:"10",13:"10",14:"11"}
       
        return str(haut[self.hauteur])
    
    def add(self, other):
        return self.hauteur + other.hauteur 
    
    def egal(self, other):
        if self.hauteur == other.hauteur:
            print("egal")
            return True
        print("pas egal")
        return False
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
        
    def ajouter_paquet(self, paquet):
        """Méthode qui ajoute un autre paquet au paquet"""
        while not paquet.est_vide():
            self.ajouter_carte(paquet.tirer_carte())

    def distribuer(self, nbjoueurs):
        """Distribuer un paquet en nbjoueurs paquets """
        Paquets=[PaquetDeCartes([]) for i in range(nbjoueurs)]
        numero=0
        while not self.est_vide():
            Paquets[numero].ajouter_carte(self.tirer_carte())
            numero=(numero+1)%nbjoueurs
        return Paquets
def testJeu():
    if __name__ == "__main__":
        #Main program    
        jeu52=PaquetDeCartes([])
        for i in range(2,15):
            for couleur in ["K","T","P","C"]:
                jeu52.ajouter_carte(Carte(i,couleur))
                
        #print("il y a ",jeu52.taille()," cartes dans le paquet")
        jeu52.battre()
        maMain = jeu52.tirer_carte(), jeu52.tirer_carte()
        #print(maMain)
        mainBanque = jeu52.tirer_carte()
        #print(mainBanque)
        #print(jeu52.taille())
        return maMain, mainBanque

mains = testJeu()
print(mains)

maMain=mains[0]
print(maMain)

mainBanque=mains[1]
print(mainBanque)

print(maMain[0])
print(maMain[1])

print(type(maMain[0]))

print(coupPredict(mainBanque, maMain))
