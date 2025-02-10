import chess
import chess.engine
import os

# Proje klasöründe yer alan "stockfish" klasörü ve ".exe" dosyası.
stockfish_path = os.path.join(os.getcwd(), "stockfish", "stockfish.exe")

def analyze_fen(fen, stockfish_path=stockfish_path):
    try:
        # Satranç tahtasını FEN kodu ile oluştur.
        board = chess.Board(fen)
    except ValueError:
        print("Hatalı FEN kodu yazdınız!")
        return None

    # Stockfish motorunu başlat.
    with chess.engine.SimpleEngine.popen_uci(stockfish_path) as engine:
        # En iyi hamle (Hesaplama süresi = 5 sn)
        best_move_result = engine.play(board, chess.engine.Limit(time=5.0))
        best_move = best_move_result.move

        # Konum değerlendirmesi (Derinlik = 20)
        info = engine.analyse(board, chess.engine.Limit(depth=20))
        score = info["score"].relative

        # "Mat" durumu kontrolü
        if score.is_mate():
            mate_moves = abs(score.mate())
            evaluation = "Mat!" if mate_moves == 0 else f"{mate_moves} hamlede mat!"
        else:
            # Skoru yüzdesel hale getir.
            evaluation = score.score() / 100
            # Hamle sırası siyahlarda ise, işareti tersine çevir.
            if board.turn == chess.BLACK:
                evaluation = -evaluation

        return best_move, evaluation

# Örnek FEN kodu
fen_code = "r1bqk2r/pppp1ppp/2n2n2/2b1p1N1/2B1P3/8/PPPP1PPP/RNBQK2R w KQkq - 6 5"
result = analyze_fen(fen_code)

if result:
    best_move, evaluation = result
    print(f"En iyi hamle: {best_move}")
    print(f"Konum: {evaluation}")
