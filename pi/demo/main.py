import chess, serial
from stockfish import Stockfish
#from chessvision import userInputStr

stockfish = Stockfish(path="/opt/homebrew/Cellar/stockfish/15/bin/stockfish",
depth = 15, parameters={"Threads": 6, "Minimum Thinking Time": 10})

stockfish2 = Stockfish(path="/opt/homebrew/Cellar/stockfish/15/bin/stockfish",
depth = 15, parameters={"Threads": 6, "Minimum Thinking Time": 10})

board = chess.Board()
outcome = board.is_game_over(claim_draw=True)

def blackTurn():
    san = input("San input: ") # input string would be given by opencv in integrated build
    try:
        print(san)
        board.push_san(san)
    except ValueError:
        print("Illegal move")
        board.turn = False
    except TypeError:
        print("Cant make move")
        board.turn = False


def whiteTurn():
    stockfish.set_fen_position(board.fen())
    san = stockfish.get_best_move_time(2000)
    try:
        print(san)
        ser.write(b"%s" % san)
        board.push_san(san)
    except ValueError:
        print("Illegal move")
        board.turn = True
    except TypeError:
        print("Cant make move")
        board.turn = False


def gameplayLoop():
    #display current board and turn
    print("\n==============================================================")
    print(f" Moves: {board.fullmove_number}")
    print(board)
    if board.turn:
        print("White's turn")
        whiteTurn()

    else:
        print("Black's turn")
        blackTurn()

def main():
    global ser
    ser = serial.Serial('/dev/tty.usbmodem1411', 9600)
    while not outcome:
        gameplayLoop()
        print(outcome)
        if board.is_checkmate():
            if board.turn:
                winner = "Black"
            else:
                winner = "White"
            print(f"checkmate: {winner} wins!")
            break
        elif board.is_stalemate():
            print("draw: stalemate")
            break
        elif board.is_fivefold_repetition():
            print("draw: 5-fold repetition")
            break
        elif board.is_insufficient_material():
            print("draw: insufficient material")
            break
        elif board.can_claim_draw():
            print("draw: claim")
            break
    ser.close()
    


main()