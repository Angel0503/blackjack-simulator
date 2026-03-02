from Class.Game import Game  

if __name__ == '__main__':
    bj_game = Game()
    print(bj_game)
    print(bj_game.playerChoice())
    bj_game.nextPlay()
    print(bj_game)
    print(bj_game.hasPlayerWin())