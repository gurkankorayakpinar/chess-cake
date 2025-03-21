import chess.engine
import os
import math

# Stockfish klasörünün konumu ve "executable file" ismi
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

        # Konum değerlendirmesi (20 derinlik)
        info = engine.analyse(board, chess.engine.Limit(depth=20))
        score = info["score"].relative

        # Mat kontrolü
        if score.is_mate():
            mate_moves = abs(score.mate())
            if mate_moves == 0:
                return "Mat!"  # Eğer oyun bittiyse
            else:
                evaluation = f"{mate_moves} hamlede mat!"
                win_rate = None  # Kaçınılmaz mat (unavoidable mat) konumuna gelindiyse, artık "kazanç olasılığı" gösterilmez.
        else:
            # Skoru yüzdelik hâle getir
            evaluation = score.score() / 100.0  # Convert centipawns to pawn units
            if board.turn == chess.BLACK:
                evaluation = -evaluation

            # Kazanç olasılığını hesapla.
            win_rate = evaluation_to_win_probability(evaluation)

            # Yüzdelik hâle getir ve tam sayı yap.
            win_rate = int(round(win_rate * 100))

            # Mat garantisi yoksa, kazanma olasılığı en fazla %99 olarak gösterilir.
            win_rate = min(win_rate, 99)

        # Sıra kimde?
        turn_side = "Siyah" if " b " in fen else "Beyaz"

        return best_move, evaluation, win_rate, turn_side

# Kullanıcıdan FEN kodunu al.
fen_code = input("FEN kodunu (sağ tık ile) yapıştır: ")

result = analyze_fen(fen_code)

if result:
    if isinstance(result, str):  # Eğer oyun bittiyse
        print("")
        print(f"Konum: {result}")
        print("")
    elif isinstance(result[1], str) and "hamlede mat" in result[1]:  # Kaçınılmaz mat (unavoidable mat) durumu varsa
        best_move, evaluation, win_rate, turn_side = result
        print("")
        print(f"Konum: {evaluation}")
        print("")
        print(f"Hamle sırası: {turn_side}")
        print("")
        print(f"En iyi hamle: {best_move}")
        print("")
    else:  # Normal konum
        best_move, evaluation, win_rate, turn_side = result
        print("")
        print(f"Konum: {evaluation}")
        print("")
        print(f"Kazanma olasılığı: %{win_rate}")
        print("")
        print(f"Hamle sırası: {turn_side}")
        print("")
        print(f"En iyi hamle: {best_move}")
        print("")
