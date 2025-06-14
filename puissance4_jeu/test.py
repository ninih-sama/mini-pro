import tkinter as tk
from tkinter import messagebox
import random

ROWS, COLS = 6, 7
EMPTY, JOUEUR_1, JOUEUR_2 = 0, 1, 2
plateau = [[EMPTY] * COLS for _ in range(ROWS)]
joueur_initial = JOUEUR_1
victoires = {JOUEUR_1: 0, JOUEUR_2: 0}
game_mode = "PVP"  # ou "IA"
game_over = False

# --- Fonctions Plateau ---
def get_next_open_row(col):
    for r in range(ROWS - 1, -1, -1):
        if plateau[r][col] == EMPTY:
            return r
    return None

def placer_palet(col):
    global joueur_initial, game_over
    if game_over: return
    row = get_next_open_row(col)
    if row is not None:
        plateau[row][col] = joueur_initial
        draw_board()
        if check_winner(row, col):
            victoires[joueur_initial] += 1
            messagebox.showinfo("Victoire", f"Joueur {joueur_initial} a gagné !")
            update_score()
            game_over = True
            root.after(1000, lambda: [reset_board(), set_game_active()])
            return
        joueur_initial = 3 - joueur_initial
        label_joueur.config(text=f"Joueur {joueur_initial} ({'Rouge' if joueur_initial == 1 else 'Jaune'})")
        if game_mode == "IA" and joueur_initial == JOUEUR_2:
            root.after(500, ia_minimax_joue)

def check_line(row, col, dr, dc):
    count, joueur = 0, plateau[row][col]
    r, c = row + dr, col + dc
    while 0 <= r < ROWS and 0 <= c < COLS and plateau[r][c] == joueur:
        count += 1
        r += dr
        c += dc
    return count

def check_winner(row, col):
    return any(1 + check_line(row, col, dr, dc) + check_line(row, col, -dr, -dc) >= 4
               for dr, dc in [(0, 1), (1, 0), (1, 1), (-1, 1)])

def reset_board():
    global plateau, joueur_initial
    plateau = [[EMPTY] * COLS for _ in range(ROWS)]
    joueur_initial = JOUEUR_1
    label_joueur.config(text="Joueur 1 (Rouge)")
    draw_board()

def set_game_active():
    global game_over
    game_over = False

# --- IA Minimax (simplifié pour profondeur 2) ---
def ia_minimax_joue():
    col = best_move(2)
    if col is not None:
        placer_palet(col)

def best_move(depth):
    valid_cols = [c for c in range(COLS) if get_next_open_row(c) is not None]
    best_score, best_col = -float('inf'), random.choice(valid_cols)
    for col in valid_cols:
        row = get_next_open_row(col)
        temp = [r.copy() for r in plateau]
        temp[row][col] = JOUEUR_2
        score = evaluate(temp, JOUEUR_2)
        if score > best_score:
            best_score, best_col = score, col
    return best_col

def evaluate(board, joueur):
    score = 0
    for r in board:
        for i in range(COLS - 3):
            window = r[i:i+4]
            score += window.count(joueur)
    return score

# --- Interface Graphique ---
def draw_board():
    canvas.delete("all")
    for r in range(ROWS):
        for c in range(COLS):
            x1, y1 = c * 50, r * 50
            x2, y2 = x1 + 50, y1 + 50
            color = "white" if plateau[r][c] == EMPTY else ("red" if plateau[r][c] == JOUEUR_1 else "yellow")
            canvas.create_oval(x1, y1, x2, y2, fill=color)

def update_score():
    label_score.config(text=f"Score - J1: {victoires[JOUEUR_1]} | J2: {victoires[JOUEUR_2]}")

# --- Menu de démarrage ---
def lancer_jeu(mode):
    global game_mode
    game_mode = mode
    menu_frame.destroy()
    game_frame.pack()
    draw_board()

# --- Tkinter Setup ---
root = tk.Tk()
root.title("Puissance 4")

menu_frame = tk.Frame(root)
tk.Label(menu_frame, text="Choisir le mode de jeu", font=("Arial", 16)).pack(pady=10)
tk.Button(menu_frame, text="Joueur vs Joueur", font=("Arial", 14), command=lambda: lancer_jeu("PVP")).pack(pady=5)
tk.Button(menu_frame, text="Joueur vs Ordinateur", font=("Arial", 14), command=lambda: lancer_jeu("IA")).pack(pady=5)
menu_frame.pack()

game_frame = tk.Frame(root)
canvas = tk.Canvas(game_frame, width=COLS * 50, height=ROWS * 50, bg="blue")
canvas.grid(row=0, column=0, columnspan=COLS)

for col in range(COLS):
    tk.Button(game_frame, text=str(col+1), width=5, command=lambda c=col: placer_palet(c)).grid(row=1, column=col)

label_joueur = tk.Label(game_frame, text="Joueur 1 (Rouge)", font=("Arial", 14))
label_joueur.grid(row=2, column=0, columnspan=COLS)

label_score = tk.Label(game_frame, text="Score - J1: 0 | J2: 0", font=("Arial", 12))
label_score.grid(row=3, column=0, columnspan=COLS)

root.mainloop()
