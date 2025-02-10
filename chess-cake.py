import chess
import chess.engine
import os
import math

# Stockfish motorunun yolu
stockfish_path = os.path.join(os.getcwd(), "stockfish", "stockfish.exe")

def evaluation_to_win_probability(evaluation):
    """ Convert absolute Stockfish evaluation (centipawns) to win probability """
    k = 0.4  # Tuning factor
    return 1 / (1 + math.exp(-k * abs(evaluation)))

def analyze_fen(fen, stockfish_path=stockfish_path):
    try:
        board = chess.Board(fen)
    except ValueError:
        print("Hatalı FEN kodu yazdınız!")
        return None

    # Stockfish motorunu başlat.
    with chess.engine.SimpleEngine.popen_uci(stockfish_path) as engine:
        # En iyi hamleyi bul (5 saniye)
        best_move_result = engine.play(board, chess.engine.Limit(time=5.0))
        best_move = best_move_result.move

        # Konum değerlendirmesi (Derinlik 20)
        info = engine.analyse(board, chess.engine.Limit(depth=20))
        score = info["score"].relative

        # Mat kontrolü
        if score.is_mate():
            mate_moves = abs(score.mate())
            evaluation = "Mat!" if mate_moves == 0 else f"{mate_moves} hamlede mat!"
            win_rate = 100  # Mat pozisyonlarında kazanç garantili

            # Eğer hemen mat varsa, "Oyun bitti!" yaz
            if mate_moves == 0:
                best_move = "Oyun bitti!"
                # Only print the position when the game is checkmated
                return evaluation, win_rate  # Return only evaluation and win_rate
        else:
            # Skoru yüzdelik hale getir
            evaluation = score.score() / 100.0  # Convert centipawns to pawn units
            if board.turn == chess.BLACK:
                evaluation = -evaluation

            # Kazanma olasılığını hesapla
            win_rate = evaluation_to_win_probability(evaluation)

            # Yüzdelik hale getir ve tam sayı yap
            win_rate = int(round(win_rate * 100))

        # Sıra kimde?
        turn_side = "Siyah" if " b " in fen else "Beyaz"

        return best_move, evaluation, win_rate, turn_side

# Örnek FEN kodu
fen_code = "r1bqk2r/pppp1Bpp/2n2n2/2b1p1N1/4P3/8/PPPP1PPP/RNBQK2R b KQkq - 0 5"

result = analyze_fen(fen_code)

if result:
    if len(result) == 2:  # Game is checkmated, only print position.
        evaluation, win_rate = result
        print(f"Konum: {evaluation}")
    else:
        best_move, evaluation, win_rate, turn_side = result
        print(f"Konum: {evaluation}")
        print(f"Kazanma olasılığı: %{win_rate}")
        print("*")
        print(f"Hamle sırası: {turn_side}")
        print(f"En iyi hamle: {best_move}")
