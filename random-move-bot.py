import random
from gtp_bot import GtpBot

def genmove(game, color):
    legal_moves = []
    
    # Gather all legal moves
    for col in range(game.goban.width):
        for row in range(game.goban.height):
            if game.is_legal_move([col, row], color):
                legal_moves.append([col, row])
    
    # Choose a random legal move if available, otherwise return "pass"
    if legal_moves:
        return random.choice(legal_moves)
    
    # No legal moves left, so pass
    return "pass"

def place_free_handicap(game, handicap):
    moves = []
    for i in range(handicap):
        for j in range(1000):
            move = genmove(game, 1)
            if 0 == moves.count(move):
                break
        moves.append(move)
    return moves

bot = GtpBot(place_free_handicap, genmove)

bot.run()
