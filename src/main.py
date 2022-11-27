class Carte:
    def __init__(self, hauteur):
        """
        Initialise un objet de type Carte.
        :param hauteur: Numéro de la Carte.
        """
        match hauteur:
            case 1:
                self.hauteur = 11
            case 10 | 11 | 12 | 13:
                self.hauteur = 10
            case _:
                self.hauteur = hauteur
                

    def __add__(self, other) -> int:
        """
        Permet D'additionner deux cartes entre elles.
        :param other:
        :return:
        """
        return self.hauteur + other.hauteur
    
    def __sub__(self, other):
        return self.hauteur - other.unAs
    
    def __str__(self) -> int:
        """
        Créé la méthode du retour de la fonction print de l'objet
        :return: Points de la Carte.
        """
        
        match self.hauteur:
            case 1:
                return str(11)
            case _:
                return str(self.hauteur)


class MainJoueur:
    def __init__(self, carte1, carte2):
        self.carte1 = carte1
        self.carte2 = carte2
        self.hauteur = Carte(carte1+carte2)
        self.unAs = 11
    
    def __str__(self):
        return 'Carte1 : ' + str(self.carte1.hauteur) + ' Carte2 : ' + str(self.carte2.hauteur) + ' Total : ' + str(self.hauteur)
    
    
    def estPaire(self):
        return True if self.carte1.hauteur == self.carte2.hauteur else False
    
    def contientAs(self):
        return True if self.carte1.hauteur == 11 or self.carte2.hauteur == 11 else False
    
    def choix(self, mainBanque):
        stand = "stand"
        hit = "hit"
        double = "double"
        split = "split"

        if self.estPaire():
            match self.carte1.hauteur:
                case 2 | 3:
                    return split if mainBanque.hauteur < 8 else hit
                case 4:
                    return split if mainBanque.hauteur in [4, 5] else hit
                case 5:
                    return hit if mainBanque.hauteur > 9 else double
                case 6:
                    return split if mainBanque.hauteur < 7 else hit 
                case 7:
                    return split if mainBanque.hauteur < 8 else hit  
                case 9: 
                    return stand if mainBanque.hauteur in [7, 10, 11] else split
                case 10:
                    return split
                case 8 | 11:
                    return split
        elif self.contientAs():
            match self.hauteur - self:
                case 2 | 3:
                    return double if mainBanque.hauteur in [5, 6] else hit
                case 4 | 5:
                    return double if mainBanque.hauteur in [4, 5, 6] else hit
                case 6:
                    return double if mainBanque.hauteur in [3, 4, 5, 6] else hit
                case 7:
                    if mainBanque.hauteur > 8:
                        return hit
                    else:
                        return stand if mainBanque.hauteur in [2, 7, 8] else double
                case _:
                    return stand
        else:
            match self.hauteur:
                case 5 | 6 | 7 | 8:
                    return hit
                case 9:
                    return double if mainBanque.hauteur in [3, 4, 5] else hit
                case 10:
                    return hit if mainBanque.hauteur in [10, 11] else double
                case 11:
                    return hit if mainBanque.hauteur == 11 else double
                case 12:
                    return stand if mainBanque.hauteur in [4, 5, 6] else hit
                case 13 | 14 | 15 | 16:
                    return stand if mainBanque.hauteur < 7 else hit
                case _:
                    return stand
                
                
if __name__ == '__main__':
    c1 = Carte(1)
    c2 = Carte(10)
    maMain = MainJoueur(c1, c2)
    print(maMain.contientAs())
    print(maMain.estPaire())
    
    carteBanque = Carte(1)
    
    print(maMain.choix(carteBanque))
