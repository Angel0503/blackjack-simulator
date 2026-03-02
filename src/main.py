from Class.Game import Game  

if __name__ == '__main__':
    print("#----STARTING GAME----#")
    bj_game = Game()
    print(bj_game)

    bj_game.handlePlayerAction()

    print("#----GAME OVER----#")
    print(bj_game)
    print(bj_game.hasPlayerWin())