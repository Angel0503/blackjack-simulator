from Classes.Carte import Carte
from Classes.MainJeu import MainJeu
from Classes.PaquetDeCartes import PaquetDeCartes
    
def testJeu():
    #Main program    
    jeu52=PaquetDeCartes([])
    for i in range(1,14):
        for couleur in ["K","T","P","C"]:
            jeu52.ajouter_carte(Carte(i))
           
    (carte1, carte2, mainBanque) = jeu52.distribuer()
    
    print(carte1,carte2)
    listeMaMain = [carte1, carte2]
    maMain = MainJeu(listeMaMain)
    print(maMain)
    print(maMain.estPaire())
    print(maMain.contientAs())
    
  
    
    """
    print(maMain)
    print(mainBanque)
    print(maMain.contientAs())
    print(maMain.estPaire())
    """
    """
    carteTest1 = Carte(1)
    carteTest2 = Carte(1)
    listeTest = [carteTest1, carteTest2]
    mainTest = MainJeu(listeTest)
    print(mainTest)
    print(mainTest.contientAs())
    print(mainTest.estPaire())
    """
    
if __name__ == '__main__':    
    testJeu()

            
