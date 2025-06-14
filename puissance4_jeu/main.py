import tkinter as tk

# Constants
ROWS = 6
COLS = 7
EMPTY = 0
JOUEUR_1 = 1
JOUEUR_2 = 2

# InitiaLisation du plateau de jeu
plateau = [[EMPTY] * COLS for _ in range(ROWS)]
joueur_initial = JOUEUR_1

def placer_palet(col):
    global joueur_initial
    row = get_next_open_row(col)
    if row is not None:
        plateau[row][col] = joueur_initial
        draw_board()
        if check_winner(row, col):
            print(f"Joueur {joueur_initial} a gagne!")
            reset_board()
        else:
            joueur_initial = 3 - joueur_initial  # changer de joueur

def get_next_open_row(col):
    for row in range(ROWS - 1, -1, -1):
        if plateau[row][col] == EMPTY:
            return row
    return None

def check_winner(row, col):
    directions = [(0, 1), (1, 0), (1, 1), (-1, 1)]
    for dr, dc in directions:
        count = 1 + check_line(row, col, dr, dc) + check_line(row, col, -dr, -dc)
        if count >= 4:
            return True
    return False

def check_line(row, col, delta_row, delta_col):
    count = 0
    while 0 <= row + delta_row < ROWS and 0 <= col + delta_col < COLS and \
            plateau[row][col] == plateau[row + delta_row][col + delta_col]:
        count += 1
        row += delta_row
        col += delta_col
    return count

def draw_board():
    canvas.delete("all")  # effacer le plateau avant de redessiner

    cell_size = 50
    for row in range(ROWS):
        for col in range(COLS):
            x1, y1 = col * cell_size, row * cell_size
            x2, y2 = x1 + cell_size, y1 + cell_size

            color = "white" if plateau[row][col] == EMPTY else ("red" if plateau[row][col] == JOUEUR_1 else "yellow")
            canvas.create_oval(x1, y1, x2, y2, fill=color)

def reset_board():
    global plateau, joueur_initial
    plateau = [[EMPTY] * COLS for _ in range(ROWS)]
    joueur_initial = JOUEUR_1
    draw_board()

# Creer la fenetre principale
root = tk.Tk()
root.title("puissance 4")

# creer bouton en bas
buttons = []
for col in range(COLS):
    button = tk.Button(root, text=str(col + 1), command=lambda col=col: placer_palet(col))
    button.grid(row=ROWS, column=col)
    buttons.append(button)

# Creer le plateau 
canvas = tk.Canvas(root, width=350, height=300)
canvas.grid(row=0, column=0, rowspan=ROWS, columnspan=COLS)

# dessiner le plateau initial
draw_board()

# placer les palets
root.mainloop()