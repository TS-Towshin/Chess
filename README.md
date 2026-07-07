# Chess Engine
This is an implementation of chess using python. The plan is to implement an AI to play against other players autonomously. But version 1.0 will be just the implementation of the base game.<br>
The base game logic implementation is not yet finished.

## Installation
Windows:<br>
```
python -m venv .venv
.venv\Scripts\activate.bat
pip install pygame
python main.py
```
Linux:<br>
```
python3 -m venv .venv
source .venv/bin/activate
pip install pygame
python3 main.py
```
This will create a virtual environment only for this program and install related dependencies in there and run the game.

## TODOs
Finished -<br>

<ul>
  <li>Pawn Moves</li>
  <li>Rook Moves(except castling)</li>
  <li>Bishop Moves</li>
  <li>Knight Moves</li>
  <li>King Moves</li>
  <li>Queen Moves</li>
  <li>Piece Capture</li>
  <li>Undo</li>
</ul>

Yet to be finished -<br>

V1:
<ul>
  <li>Checks</li>
  <li>Checkmate</li>
  <li>Castling</li>
  <li>Stalemate</li>
  <li>Promotion</li>
  <li>En Passant</li>
</ul>

V2:
<ul>
  <li>AI</li>
</ul>

## Keybinding
Press U to undo a move
