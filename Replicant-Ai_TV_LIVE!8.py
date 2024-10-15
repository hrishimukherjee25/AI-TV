import tkinter as tk
import random
import time
import numpy as np

# Parameters for the Game of Life grid
GRID_SIZE = 200  # Number of cells in each row and column
CELL_SIZE = 2  # Size of each cell in pixels
DIFFUSION_RATE = 0.1  # Diffusion constant
GROWTH_RATE = 0.05  # Growth rate constant

# Player colors based on life intensity
def get_color(value):
    if value > 0.66:
        return "red"  # Player 1 (strong alive)
    elif value > 0.33:
        return "yellow"  # Player 2 (partially alive)
    else:
        return "white"  # Dead or near dead

# Function to handle Game of Life logic with differential calculus
def game_of_life_step():
    global grid
    new_grid = np.copy(grid)  # Create a copy of the current grid

    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            laplacian = compute_laplacian(grid, i, j)  # Compute the Laplacian (neighbor average)
            new_grid[i][j] += DIFFUSION_RATE * laplacian + GROWTH_RATE * grid[i][j] * (1 - grid[i][j])

            # Ensure the values stay between 0 and 1
            new_grid[i][j] = min(max(new_grid[i][j], 0), 1)

    grid = new_grid  # Update the grid
    draw_grid()

# Function to compute the Laplacian (discrete 2D)
def compute_laplacian(grid, x, y):
    laplacian = 0
    for i in range(max(0, x-1), min(GRID_SIZE, x+2)):
        for j in range(max(0, y-1), min(GRID_SIZE, y+2)):
            if (i, j) != (x, y):
                laplacian += grid[i][j] - grid[x][y]
    return laplacian

# Function to draw the current state of the grid
def draw_grid():
    canvas.delete("all")  # Clear the canvas
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            color = get_color(grid[i][j])
            canvas.create_rectangle(j * CELL_SIZE, i * CELL_SIZE, 
                                    (j + 1) * CELL_SIZE, (i + 1) * CELL_SIZE, 
                                    fill=color, outline="gray")

# Function to initialize a random grid state with continuous values
def initialize_grid():
    global grid
    grid = np.random.rand(GRID_SIZE, GRID_SIZE)  # Random values between 0 and 1 for the grid
    draw_grid()

# Function to start the differential calculus-based Game of Life evolution
def start_game_of_life():
    tv_window.config(state=tk.NORMAL)
    tv_window.insert(tk.END, "AI TV LIVE! Differential Calculus Game of Life started...\n")
    tv_window.config(state=tk.DISABLED)
    tv_window.yview(tk.END)

    for _ in range(50):  # Simulate 50 generations
        game_of_life_step()
        root.update()  # Update the GUI to reflect changes
        time.sleep(0.2)

# Create the main window
root = tk.Tk()
root.title("ChatGPT UI with AI TV LIVE! - Differential Calculus Game of Life")
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

# Initialize the grid as a global variable with continuous values
grid = np.random.rand(GRID_SIZE, GRID_SIZE)

# Run the application
root.mainloop()
