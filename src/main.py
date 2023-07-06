from Classes.Carte import Carte
from Classes.MainJeu import MainJeu
from Classes.PaquetDeCartes import PaquetDeCartes
    
def testJeu():
    #Main program    
    maMain, mainBanque = distribuer()
    print(maMain)
    print(mainBanque)
    print(maMain.choix(mainBanque))

def distribuer():
    jeu52=PaquetDeCartes([])
    for i in range(1,14):
        for _ in ["K","T","P","C"]:
            jeu52.ajouter_carte(Carte(i))
    (carte1, carte2, mainBanque) = jeu52.distribuer()
    listeMaMain = [carte1, carte2]
    maMain = MainJeu(listeMaMain, Carte(1))
    return maMain, mainBanque

if __name__ == '__main__':
    testJeu()

