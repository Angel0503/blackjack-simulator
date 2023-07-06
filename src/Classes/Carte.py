
class Carte:
    def __init__(self, hauteur=0):
        match hauteur:
            case 1:
                self.hauteur = 11
            case 10 | 11 | 12 | 13:
                self.hauteur = 10
            case _:
                self.hauteur = hauteur      

    def getHauteur(self):
        return self.hauteur

    def __add__(self, other) -> int:
        """
        Permet D'additionner deux cartes entre elles.
        :param other:
        :return:
        """
        return self.hauteur + other.hauteur
    
    def __sub__(self, other):
        return self.hauteur - other.unAs
    
    def __eq__(self, other) -> bool:
        return self.hauteur == other

    def __str__(self) -> int:
        """
        Créé la méthode du retour de la fonction print de l'objet
        :return: Points de la Carte.
        """
        return str(self.hauteur)