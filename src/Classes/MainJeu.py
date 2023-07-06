class MainJeu:
    def __init__(self,listeCarte, unAs):
        self.uneMain = listeCarte
        self.unAs = unAs
        self.hauteur = self.uneMain[0].hauteur + self.uneMain[1].hauteur
        
    def __str__(self):
        message=""
        for elmt in self.uneMain:
            message += "Carte : " + str(elmt.hauteur) + " "
        return message
    
    def getCarte1(self):
        return self.uneMain[0]
    
    def getCarte2(self):
        return self.uneMain[1]

    def estPaire(self):
        return self.uneMain[0] == self.uneMain[1]
    
    def contientAs(self):
        return True if self.uneMain[0] == self.unAs or self.uneMain[1] == self.unAs else False
    
    def ajouterCarte(self, carte):
        self.uneMain.append(carte)
        
    def choix(self, mainBanque):
        stand = "stand"
        hit = "hit"
        double = "double"
        split = "split"
        
        if self.estPaire():
            match self.uneMain[0].hauteur:
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
            match self.hauteur - self.unAs.hauteur:
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