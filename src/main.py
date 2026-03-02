from Class.Deck import Deck  

if __name__ == '__main__':
    deck=Deck()
    playerHand, bankHand = deck.deal()

    print("Player")
    print(playerHand)

    print("Bank")
    print(bankHand)

    print("Choice")
    print(playerHand.bestChoice(bankHand))

    match playerHand.bestChoice(bankHand):
        case "hit":
            playerHand.hit(deck, playerHand)
        case "split":
            playerHand.split(deck)
        case "double":
            playerHand.double(deck)
        case "stand":
            playerHand.standAction()