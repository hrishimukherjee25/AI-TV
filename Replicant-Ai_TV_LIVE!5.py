import tkinter as tk
import random
import time

# Parameters for the Game of Life grid
GRID_SIZE = 20  # Number of cells in each row and column
CELL_SIZE = 20  # Size of each cell in pixels

# Player colors
COLORS = {
    0: "white",    # Empty cell (dead)
    1: "red",      # Player 1
    2: "green",    # Player 2
    3: "blue",     # Player 3
    4: "yellow"    # Player 4
}

# Function to handle Game of Life logic for a 4-player game
def game_of_life_step():
    global grid
    new_grid = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

    # Apply Game of Life rules to each cell
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            live_neighbors = count_live_neighbors(grid, i, j)
            if grid[i][j] != 0:  # If cell is alive
                if live_neighbors[grid[i][j]] < 2 or sum(live_neighbors.values()) > 3:
                    new_grid[i][j] = 0  # Cell dies
                else:
                    new_grid[i][j] = grid[i][j]  # Cell survives
            else:  # If cell is dead
                max_player = max(live_neighbors, key=live_neighbors.get)
                if live_neighbors[max_player] == 3:
                    new_grid[i][j] = max_player  # Cell becomes alive under the dominant player

    grid = new_grid
    draw_grid()

# Function to count live neighbors for a given cell (by player)
def count_live_neighbors(grid, x, y):
    live_neighbors = {1: 0, 2: 0, 3: 0, 4: 0}  # Count neighbors for each player
    for i in range(max(0, x-1), min(GRID_SIZE, x+2)):
        for j in range(max(0, y-1), min(GRID_SIZE, y+2)):
            if (i, j) != (x, y) and grid[i][j] != 0:
                live_neighbors[grid[i][j]] += 1
    return live_neighbors

# Function to draw the current state of the grid
def draw_grid():
    canvas.delete("all")  # Clear the canvas
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            color = COLORS[grid[i][j]]
            canvas.create_rectangle(j * CELL_SIZE, i * CELL_SIZE, 
                                    (j + 1) * CELL_SIZE, (i + 1) * CELL_SIZE, 
                                    fill=color, outline="gray")

# Function to initialize a random grid state with 4 players
def initialize_grid():
    global grid
    grid = [[random.choice([0, 1, 2, 3, 4]) for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    draw_grid()

# Function to start the 4-player Game of Life evolution
def start_game_of_life():
    tv_window.config(state=tk.NORMAL)
    tv_window.insert(tk.END, "AI TV LIVE! 4-Player Game of Life started...\n")
    tv_window.config(state=tk.DISABLED)
    tv_window.yview(tk.END)

    for _ in range(50):  # Simulate 50 generations
        game_of_life_step()
        root.update()  # Update the GUI to reflect changes
        time.sleep(0.2)

# Create the main window
root = tk.Tk()
root.title("ChatGPT UI with AI TV LIVE! - 4-Player Game of Life")
root.geometry("1200x800")

# Create a frame for chat and AI TV LIVE!
main_frame = tk.Frame(root)
main_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Chat section
chat_frame = tk.Frame(main_frame)
chat_frame.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH, expand=True)

# Create chat window
chat_window = tk.Text(chat_frame, state=tk.DISABLED, wrap=tk.WORD, height=15)
chat_window.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Create input text box
user_input = tk.Text(chat_frame, height=3)
user_input.pack(padx=10, pady=10, fill=tk.X)

# Create a send button
send_button = tk.Button(chat_frame, text="Send")
send_button.pack(padx=10, pady=5)

# AI TV LIVE! section
tv_frame = tk.Frame(main_frame)
tv_frame.pack(side=tk.RIGHT, padx=10, pady=10, fill=tk.BOTH, expand=True)

# Create AI TV LIVE! window for messages
tv_window = tk.Text(tv_frame, state=tk.DISABLED, wrap=tk.WORD, height=5)
tv_window.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Create a canvas for AI TV LIVE! grid content
canvas = tk.Canvas(tv_frame, width=GRID_SIZE * CELL_SIZE, height=GRID_SIZE * CELL_SIZE, bg="white")
canvas.pack(padx=10, pady=10)

# Create buttons for AI TV LIVE! action
ai_tv_button = tk.Button(tv_frame, text="Initialize Grid", command=initialize_grid)
ai_tv_button.pack(padx=10, pady=5)

start_button = tk.Button(tv_frame, text="Start Game of Life!", command=start_game_of_life)
start_button.pack(padx=10, pady=5)

# Initialize the grid as a global variable
grid = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

# Run the application
root.mainloop()
