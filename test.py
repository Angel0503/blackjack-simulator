from time import sleep

def decider(carte1, carte2, carte3):
    """
    Permet à l'utilisateur de saisir ses deux cartes
    :return:
    """
    c1: Carte = Carte(carte1)
    c2: Carte = Carte(carte2)
    c3: Carte = Carte(carte3)
    print(Carte(c1+c2).choix(c3))


class Carte:
    def __init__(self, hauteur):
        """
        Initialise un objet de type Carte.
        :param hauteur: Numéro de la Carte.
        """
        match hauteur:
            case 1:
                self.hauteur = 11
            case 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9:
                self.hauteur = hauteur
            case _:
                self.hauteur = 10

    def __add__(self, other) -> int:
        """
        Permet D'additionner deux cartes entre elles.
        :param other:
        :return:
        """
        return self.hauteur + other.hauteur

    def __repr__(self) -> int:
        """
        Créé la méthode du retour de la fonction print de l'objet
        :return: Points de la Carte.
        """

        match self.hauteur:
            case 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10:
                return self.hauteur
            case _:
                return 11

    def choix(self, other):
        stand = "stand"
        hit = "hit"
        double = "double"
        split = "split"

        maMain = self.hauteur
        mainBanque = other.hauteur

        if maMain == mainBanque:
            match self.hauteur:
                case 2 | 3 | 7:
                    return split if mainBanque < 8 else hit
                case 4:
                    return split if mainBanque in [5, 6] else hit
                case 5:
                    return hit if mainBanque > 9 else double
                case 6:
                    return split if mainBanque < 7 else hit
                case 8 | "A":
                    return split
                case 9:
                    return stand if mainBanque in [7, 10, 11] else split
                case 10:
                    return stand

        if maMain == 11:
            match mainBanque:
                case 2 | 3:
                    return double if mainBanque in [5, 6] else hit
                case 4 | 5:
                    return double if mainBanque in [4, 5, 6] else hit
                case 6:
                    return double if mainBanque in [3, 4, 5, 6] else hit
                case 7:
                    return stand if mainBanque in [2, 7, 8] else double if mainBanque in [3, 4, 5, 6] else hit
                case 8 | 9 | 10:
                    return stand

        match self.hauteur:
            case 5 | 6 | 7 | 8:
                return hit
            case 9:
                return double if mainBanque in [3, 4, 5] else hit
            case 10:
                return hit if mainBanque in [10, 11] else double
            case 11:
                return hit if mainBanque == 11 else double
            case 12:
                return stand if mainBanque in [4, 5, 6] else hit
            case 13 | 14 | 14 | 16:
                return stand if mainBanque < 7 else hit
            case _:
                return stand


if __name__ == '__main__':
    for i in range(2,12):
        for j in range(2,12):
            for k in range(2,12):
                decider(i,j,k)
                print(i,j,k)
                sleep(1)