from Classes.Carte import Carte
from Classes.MainJeu import MainJeu
from Classes.PaquetDeCartes import PaquetDeCartes  

def distribuer(jeu52):
    for i in range(1,14):
        for _ in ["K","T","P","C"]:
            jeu52.ajouter_carte(Carte(i))
    (carte1, carte2, carteBanque) = jeu52.distribuer()
    listeMaMain = [carte1, carte2]
    maMain = MainJeu(listeMaMain, Carte(1))
    mainBanque = MainJeu([carteBanque], Carte(1))
    return maMain, mainBanque

def hit(paquet, maMain):
    nvlleCarte = paquet.tirer_carte()
    maMain.ajouterCarte(nvlleCarte)
    print(maMain)

def stand(maMain):
    maMain.stand = True

def double(paquet, maMain):
    maMain.ajouterMise()
    hit(paquet, maMain)

def split(paquet, maMain):
    carte = maMain.uneMain[0]
    del maMain.uneMain[0]
    mainSplit = MainJeu([carte], Carte(1))

    hit(paquet, maMain)
    hit(paquet, mainSplit)

    return mainSplit

if __name__ == '__main__':
    jeu52=PaquetDeCartes([])
    maMain, mainBanque = distribuer(jeu52)

    print(maMain)
    print(mainBanque)
    print(maMain.choix(mainBanque))

    match maMain.choix(mainBanque):
        case "hit":
            hit(jeu52, maMain)
        case "split":
            split(jeu52, maMain)
        case "double":
            double(jeu52, maMain)
        case "stand":
            stand(maMain)