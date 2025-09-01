# ♟️ Chess Vision

Chess Vision is an **experimental project** for chess training in Python with visualization of the best moves calculated by Stockfish, highlighting legal moves, custom promotion, undo moves, and the option to flip the board to train from different perspectives.

Ideal for **studying and practicing games with real-time visual feedback**.

---

## ✅ Features

- **Blue highlight** for the **best move** suggested by Stockfish in real time.
- **Green highlight** for the **legal moves** of the selected piece.
- **Custom promotion** (queen, rook, bishop, knight).
- **Undo moves** (key `U`).
- **Flip board button** to train from both sides.
- Lightweight interface in **Pygame**.

---

## 🚀 How to Use

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/caue-r/chess-vision.git
cd chess-vision
```

### 2️⃣ Install Dependencies

Install all dependencies quickly using:

```bash
pip install -r requirements.txt
```

### 3️⃣ Download and Configure Stockfish

The project uses [Stockfish](https://stockfishchess.org/download/) to calculate the best moves:

- Download the Stockfish version for your operating system.
- Extract the executable (e.g., `stockfish_16_x64_avx2.exe`).
- Rename it to `stockfish.exe`.
- Place `stockfish.exe` in the **same folder as `chess_game.py`**.

---

## 🎮 Controls

- **Click a piece** to see its legal moves in green.
- **Click the destination** to move the piece.
- **Key `U`**: undo the last move.
- **“Flip Board” button**: switch the board perspective.

---

## 🖼️ Icon Credits

The pieces used are from the **Fresca** set by [Lichess](https://lichess.org), available under CC0 license in the repository:

🔗 [https://github.com/lichess-org/lila/tree/master/public/piece/fresca](https://github.com/lichess-org/lila/tree/master/public/piece/fresca)

---

## ⚠️ Warning

This is **only an experimental project** for learning and personal training purposes.  
Not recommended for production use or advanced game analysis.

---
