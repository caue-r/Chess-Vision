import pygame
import sys
import chess
import chess.engine

pygame.init()

WIDTH, HEIGHT = 640, 720
SQUARE_SIZE = WIDTH // 8
LIGHT_BROWN = (240, 217, 181)
DARK_BROWN = (181, 136, 99)
HIGHLIGHT_COLOR = (0, 255, 0, 100)
BEST_MOVE_COLOR = (0, 0, 255, 100)
IMAGES = {}

def load_images():
    pieces = ['wp', 'bp', 'wr', 'br', 'wn', 'bn', 'wb', 'bb', 'wq', 'bq', 'wk', 'bk']
    for piece in pieces:
        IMAGES[piece] = pygame.transform.scale(pygame.image.load(f"{piece}.png"), (SQUARE_SIZE, SQUARE_SIZE))

def draw_board(screen, flipped):
    colors = [LIGHT_BROWN, DARK_BROWN]
    for r in range(8):
        for c in range(8):
            draw_r = 7 - r if flipped else r
            draw_c = 7 - c if flipped else c
            pygame.draw.rect(screen, colors[(r+c)%2], pygame.Rect(draw_c*SQUARE_SIZE, draw_r*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

def draw_pieces(screen, board, flipped):
    for r in range(8):
        for c in range(8):
            piece = board[r][c]
            if piece != '--':
                draw_r = 7 - r if flipped else r
                draw_c = 7 - c if flipped else c
                screen.blit(IMAGES[piece], pygame.Rect(draw_c*SQUARE_SIZE, draw_r*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

def highlight_squares(screen, squares, color, flipped):
    s = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE), pygame.SRCALPHA)
    s.fill(color)
    for square in squares:
        c = square % 8
        r = 7 - (square // 8)
        draw_r = 7 - r if flipped else r
        draw_c = 7 - c if flipped else c
        screen.blit(s, (draw_c*SQUARE_SIZE, draw_r*SQUARE_SIZE))

def draw_turn_display(screen, turn):
    font = pygame.font.SysFont("Arial", 30)
    text = "Vez: Brancas" if turn else "Vez: Pretas"
    text_surface = font.render(text, True, (0,0,0))
    pygame.draw.rect(screen, LIGHT_BROWN, (0, HEIGHT - 80, WIDTH, 40))
    screen.blit(text_surface, (WIDTH//2 - text_surface.get_width()//2, HEIGHT - 75))

def draw_flip_button(screen):
    font = pygame.font.SysFont("Arial", 24)
    pygame.draw.rect(screen, DARK_BROWN, (WIDTH//2 - 60, HEIGHT - 40, 120, 35))
    text = font.render("Inverter Tabuleiro", True, (255,255,255))
    screen.blit(text, (WIDTH//2 - text.get_width()//2, HEIGHT - 35))

def get_board_matrix(fen):
    board = [['--' for _ in range(8)] for _ in range(8)]
    rows = fen.split()[0].split('/')
    for r in range(8):
        c = 0
        for char in rows[r]:
            if char.isdigit():
                c += int(char)
            else:
                color = 'w' if char.isupper() else 'b'
                piece = char.lower()
                board[r][c] = color + piece
                c += 1
    return board

def promotion_choice(screen, color):
    font = pygame.font.SysFont("Arial", 24)
    pieces = ['q', 'r', 'b', 'n']
    piece_images = [IMAGES[color + p] for p in pieces]
    while True:
        screen.fill(LIGHT_BROWN)
        text = font.render("Escolha a peça para promoção", True, (0,0,0))
        screen.blit(text, (WIDTH//2 - text.get_width()//2, 50))
        for idx, img in enumerate(piece_images):
            x = WIDTH//2 - 2*SQUARE_SIZE + idx*SQUARE_SIZE
            y = HEIGHT//2 - SQUARE_SIZE//2
            screen.blit(img, (x, y))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                if HEIGHT//2 - SQUARE_SIZE//2 <= my <= HEIGHT//2 + SQUARE_SIZE//2:
                    for idx in range(4):
                        x = WIDTH//2 - 2*SQUARE_SIZE + idx*SQUARE_SIZE
                        if x <= mx <= x + SQUARE_SIZE:
                            return pieces[idx]

def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Xadrez - Melhor Jogada, Promoção, Desfazer e Inverter")
    clock = pygame.time.Clock()
    load_images()

    board = chess.Board()
    engine = chess.engine.SimpleEngine.popen_uci("stockfish.exe")
    best_move_squares = []
    possible_moves_squares = []
    selected_square = None
    flipped = False
    running = True

    promotion_map = {'q': chess.QUEEN, 'r': chess.ROOK, 'b': chess.BISHOP, 'n': chess.KNIGHT}

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_u:
                    if board.move_stack:
                        board.pop()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                if HEIGHT - 40 <= my <= HEIGHT - 5 and WIDTH//2 - 60 <= mx <= WIDTH//2 + 60:
                    flipped = not flipped
                elif my < WIDTH:
                    col = 7 - (mx // SQUARE_SIZE) if flipped else mx // SQUARE_SIZE
                    row = mx // SQUARE_SIZE if flipped else 7 - (my // SQUARE_SIZE)
                    row = 7 - (my // SQUARE_SIZE) if not flipped else my // SQUARE_SIZE
                    square = chess.square(col, row)
                    piece = board.piece_at(square)
                    if selected_square is None:
                        if piece is not None and piece.color == board.turn:
                            selected_square = square
                            possible_moves_squares = [move.to_square for move in board.legal_moves if move.from_square == selected_square]
                    else:
                        move = chess.Move(selected_square, square)
                        if chess.Move(selected_square, square, promotion=chess.QUEEN) in board.legal_moves:
                            color = 'w' if board.turn else 'b'
                            choice = promotion_choice(screen, color)
                            promotion_piece = promotion_map[choice]
                            move = chess.Move(selected_square, square, promotion=promotion_piece)
                        if move in board.legal_moves:
                            board.push(move)
                        selected_square = None
                        possible_moves_squares = []

        if not board.is_game_over():
            result = engine.analyse(board, chess.engine.Limit(time=0.1))
            move = result['pv'][0]
            best_move_squares = [move.from_square, move.to_square]

        draw_board(screen, flipped)
        if possible_moves_squares:
            highlight_squares(screen, possible_moves_squares, HIGHLIGHT_COLOR, flipped)
        if best_move_squares:
            highlight_squares(screen, best_move_squares, BEST_MOVE_COLOR, flipped)
        board_matrix = get_board_matrix(board.fen())
        draw_pieces(screen, board_matrix, flipped)
        draw_turn_display(screen, board.turn)
        draw_flip_button(screen)
        pygame.display.flip()
        clock.tick(60)

    engine.quit()
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
