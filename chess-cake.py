import chess.engine
import os
import math

# Stockfish programının konumu ve "executable file" ismi
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
            evaluation = "Mat!" if mate_moves == 0 else f"{mate_moves} hamlede mat!"
            win_rate = 100  # Mat garantisi varsa, kazanç olasılığı %100 olarak gösterilir.

            # Eğer konum "mat" ise, sadece evaluation ve win_rate (?) dön - (bu kısım düzeltilebilir)
            if mate_moves == 0:
                return evaluation, win_rate
            # X hamlede mat varsa, diğer bilgileri de göster.
            else:
                turn_side = "Siyah" if " b " in fen else "Beyaz"
                return best_move, evaluation, win_rate, turn_side
        else:
            # Skoru yüzdelik hale getir
            evaluation = score.score() / 100.0  # Convert centipawns to pawn units
            if board.turn == chess.BLACK:
                evaluation = -evaluation

            # Kazanç olasılığını hesapla.
            win_rate = evaluation_to_win_probability(evaluation)

            # Yüzdelik hâle getir ve tam sayı yap
            win_rate = int(round(win_rate * 100))

        # Sıra kimde?
        turn_side = "Siyah" if " b " in fen else "Beyaz"

        return best_move, evaluation, win_rate, turn_side

# Kullanıcıdan FEN kodunu al.
fen_code = input("FEN kodunu yapıştır (sağ tık): ")

result = analyze_fen(fen_code)

if result:
    if len(result) == 2:  # Konum "mat" ise, sadece konum puanını göster.
        evaluation, win_rate = result
        print(f"Konum: {evaluation}")
    else:  # X hamlede mat veya normal pozisyon için tüm bilgiler gösterilir.
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
