import sys, copy
from http.client import responses

from numpy.ma.core import masked_print_option

# Dictionary and template, can be copy.copy() at start
STARTING_PIECES = {'a8': 'bR', 'b8': 'bN', 'c8': 'bB', 'd8': 'bQ',
'e8': 'bK', 'f8': 'bB', 'g8': 'bN', 'h8': 'bR', 'a7': 'bP', 'b7': 'bP',
'c7': 'bP', 'd7': 'bP', 'e7': 'bP', 'f7': 'bP', 'g7': 'bP', 'h7': 'bP',
'a1': 'wR', 'b1': 'wN', 'c1': 'ww', 'd1': 'wQ', 'e1': 'wK', 'f1': 'ww',
'g1': 'wN', 'h1': 'wR', 'a2': 'wP', 'b2': 'wP', 'c2': 'wP', 'd2': 'wP',
'e2': 'wP', 'f2': 'wP', 'g2': 'wP', 'h2': 'wP'}

BOARD_TEMPLATE = """
    a    b    c    d    e    f    g    h
   ____ ____ ____ ____ ____ ____ ____ ____
  ||||||    ||||||    ||||||    ||||||    |
8 ||{}|| {} ||{}|| {} ||{}|| {} ||{}|| {} |
  ||||||____||||||____||||||____||||||____|
  |    ||||||    ||||||    ||||||    ||||||
7 | {} ||{}|| {} ||{}|| {} ||{}|| {} ||{}||
  |____||||||____||||||____||||||____||||||
  ||||||    ||||||    ||||||    ||||||    |
6 ||{}|| {} ||{}|| {} ||{}|| {} ||{}|| {} |
  ||||||____||||||____||||||____||||||____|
  |    ||||||    ||||||    ||||||    ||||||
5 | {} ||{}|| {} ||{}|| {} ||{}|| {} ||{}||
  |____||||||____||||||____||||||____||||||
  ||||||    ||||||    ||||||    ||||||    |
4 ||{}|| {} ||{}|| {} ||{}|| {} ||{}|| {} |
  ||||||____||||||____||||||____||||||____|
  |    ||||||    ||||||    ||||||    ||||||
3 | {} ||{}|| {} ||{}|| {} ||{}|| {} ||{}||
  |____||||||____||||||____||||||____||||||
  ||||||    ||||||    ||||||    ||||||    |
2 ||{}|| {} ||{}|| {} ||{}|| {} ||{}|| {} |
  ||||||____||||||____||||||____||||||____|
  |    ||||||    ||||||    ||||||    ||||||
1 | {} ||{}|| {} ||{}|| {} ||{}|| {} ||{}||
  |____||||||____||||||____||||||____||||||
"""
WHITE_SQUARE = '||'
BLACK_SQUARE = ' '

# Print the current Chessboard
def print_chess_board(board):
    squares = []
    is_white_square = True
    for y in '87654321':
        for x in 'abcdefgh':
            #print(x, y, is_white_square)  # DEBUG: Shows coordinates in order.
            if x + y in board.keys():
              squares.append(board[x + y])
            else:
              if is_white_square:
                squares.append(WHITE_SQUARE)
              else:
                squares.append(BLACK_SQUARE)
            is_white_square = not is_white_square
        is_white_square = not is_white_square

    print(BOARD_TEMPLATE.format(*squares))

# Print header and instructions
def print_help():
    print('Interactive Chess Board')
    print('by mermerh')
    print()
    print('Pieces:')
    print('  w - White, b - Black')
    print('  P - Pawn, N - Knight, B - Bishop, R - Rook, Q - Queen, K - King')
    print('Commands:')
    print('  move e2 e4 - Moves the piece at e2 to e4.')
    print('  remove e2 - Removes the piece at e2.')
    print('  set e2 wP - Sets square e2 to a white pawn.')
    print('  validate - Check if the board is valid.')
    print('  reset - Reset pieces back to their starting squares.')
    print('  clear - Clear the entire board.')
    print('  fill wP - Fill entire board with white pawns.')
    print('  help - Show this help information.')
    print('  quit - Quits the program.')

# Validate the Chessboard against the dictionary
def isValidChessBoard(board):
    piece_counts = {'w': 0, 'b': 0}
    king_counts = {'w': 0, 'b': 0}
    pawn_counts = {'w': 0, 'b': 0}
    valid_positions = {f"{file}{rank}" for file in "abcdefgh" for rank in "12345678"}
    valid_pieces = {'pawn', 'knight', 'bishop', 'rook', 'queen', 'king'}

    for position, piece in board.items():
        # Check square validity
        if position not in valid_positions:
            print(f"Invalid position: {position}")
            return False

        # Check piece name
        if len(piece) < 2:
            print(f"Invalid piece name (too short): {piece}")
            return False
        color = piece[0]
        name = piece[1:].lower()

        if color not in ('w', 'b') or name not in valid_pieces:
            print(f"Invalid piece type: {piece}")
            return False

        # Count pieces
        piece_counts[color] += 1
        if name == 'king':
            king_counts[color] += 1
        if name == 'pawn':
            pawn_counts[color] += 1

    if king_counts['w'] != 1 or king_counts['b'] != 1:
        print("Missing or extra king(s).")
        return False
    if piece_counts['w'] > 16 or piece_counts['b'] > 16:
        print("Too many pieces for one color.")
        return False
    if pawn_counts['w'] > 8 or pawn_counts['b'] > 8:
        print("Too many pawns for one color.")
        return False

    return True

# Manipulate the Chessboard
main_board = copy.copy(STARTING_PIECES)
print_help()
while True:
    print_chess_board(main_board)
    response = input('> ').split()

    if response[0] == 'move':
        main_board[response[2]] = main_board[response[1]]
        del main_board[response[1]]
    elif response[0] == 'remove':
        del main_board[response[1]]
    elif response[0] == 'set':
        main_board[response[1]] = [response[2]]
    elif response[0] == 'reset':
        main_board = copy.copy(STARTING_PIECES)
    elif response[0] == 'clear':
        main_board = {}
    elif response[0] == 'validate':
        if isValidChessBoard(main_board):
            print("++ Board is valid.")
        else:
            print("xx Board is invalid.")
    elif response[0] == 'fill':
        for y in '87654321':
            for x in 'abcdefgh':
                main_board[x + y] = response[1]
    elif response[0] == 'quit':
        sys.exit()