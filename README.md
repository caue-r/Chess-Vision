# ♟️ Chess Vision

Chess Vision é um **projeto experimental** de treino de xadrez em Python com visualização das melhores jogadas calculadas pelo Stockfish, destaque de movimentos legais, promoção customizada, desfazer jogadas e opção de inverter o tabuleiro para treinar de diferentes perspectivas.

Ideal para **estudo e prática de partidas com feedback visual em tempo real**.

---

## ✅ Recursos

- Destaque em **azul** da **melhor jogada** sugerida pelo Stockfish em tempo real.
- Destaque em **verde** dos **movimentos legais** da peça selecionada.
- **Promoção customizada** (dama, torre, bispo, cavalo).
- **Desfazer jogadas** (tecla `U`).
- **Botão de inverter tabuleiro** para treinar de ambos os lados.
- Interface leve em **Pygame**.

---

## 🚀 Como usar

### 1️⃣ Clonar o repositório

```bash
git clone https://github.com/caue-r/chess-vision.git
cd chess-vision
```

### 2️⃣ Instalar dependências

```bash
pip install pygame python-chess
```

### 3️⃣ Baixar e configurar o Stockfish

O projeto usa o [Stockfish](https://stockfishchess.org/download/) para calcular as melhores jogadas:

- Baixe a versão do Stockfish para o seu sistema operacional.
- Extraia o executável (ex: `stockfish_16_x64_avx2.exe`).
- Renomeie para `stockfish.exe`.
- Coloque o `stockfish.exe` na **mesma pasta do `chess_game.py`**.

---

## 🎮 Controles

- **Clique em uma peça** para ver seus movimentos legais em verde.
- **Clique no destino** para mover a peça.
- **Tecla `U`**: desfaz a última jogada.
- **Botão “Inverter Tabuleiro”**: alterna a visão do tabuleiro.

---

## 🖼️ Créditos dos ícones

As peças utilizadas são do conjunto **Fresca** do [Lichess](https://lichess.org), disponíveis sob licença CC0 no repositório:

🔗 [https://github.com/lichess-org/lila/tree/master/public/piece/fresca](https://github.com/lichess-org/lila/tree/master/public/piece/fresca)

---

## ⚠️ Aviso

Este é **apenas um projeto experimental** para fins de aprendizado e treino pessoal.  
Não recomendado para uso em produção ou análise avançada de partidas.

---
