class Card:
    def __init__(self, value=0):
        match value:
            case 1:
                self.value = 11
            case 10 | 11 | 12 | 13:
                self.value = 10
            case _:
                self.value = value      

    def getvalue(self):
        return self.value

    def __add__(self, other):
        return self.value + other.value
    
    def __sub__(self, other):
        return self.value - other.value
    
    def __eq__(self, other):
        return isinstance(other, Card) and self.value == other.value

    def __str__(self):
        return str(self.value)