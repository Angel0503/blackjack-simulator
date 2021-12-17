def additionCarte(carte):
    return int(carte[0]) + int(carte[1])

def coupPredict(mainBanque, maMain):
    stay = "stay"
    hit = "hit"
    double = "double"
    split = "split"

    """Cas du double"""
    if maMain[0] == maMain[1]:
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
    maMain = str(additionCarte(maMain))
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

print(coupPredict("7", "105"))