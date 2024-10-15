import tkinter as tk
import random
import time

# Game of Life configurations
GRID_SIZE = 20
CELL_SIZE = 20
UPDATE_DELAY = 500  # in milliseconds

# Create the main window
root = tk.Tk()
root.title("ChatGPT UI with AI TV LIVE & Game of Life")
root.geometry("800x800")

# Game of Life State
game_running = False

# Function to initialize a random grid
def initialize_grid():
    global grid
    grid = [[random.choice([0, 1]) for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    draw_grid()

# Function to update the grid based on Game of Life rules
def update_grid():
    global grid, game_running
    if game_running:
        new_grid = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
        
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                live_neighbors = count_live_neighbors(row, col)
                
                if grid[row][col] == 1:  # Live cell
                    if live_neighbors < 2 or live_neighbors > 3:
                        new_grid[row][col] = 0  # Dies
                    else:
                        new_grid[row][col] = 1  # Lives
                else:  # Dead cell
                    if live_neighbors == 3:
                        new_grid[row][col] = 1  # Becomes a live cell
        
        grid = new_grid
        draw_grid()
        root.after(UPDATE_DELAY, update_grid)  # Schedule the next update

# Function to count live neighbors of a cell
def count_live_neighbors(row, col):
    neighbors = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    live_count = 0
    
    for dr, dc in neighbors:
        r, c = row + dr, col + dc
        if 0 <= r < GRID_SIZE and 0 <= c < GRID_SIZE and grid[r][c] == 1:
            live_count += 1
            
    return live_count

# Function to draw the grid on the canvas
def draw_grid():
    canvas.delete("all")
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            color = "black" if grid[row][col] == 1 else "white"
            canvas.create_rectangle(
                col * CELL_SIZE, row * CELL_SIZE, 
                (col + 1) * CELL_SIZE, (row + 1) * CELL_SIZE, 
                fill=color, outline="gray"
            )

# Function to start the Game of Life simulation
def start_game():
    global game_running
    game_running = True
    update_grid()

# Function to stop the Game of Life simulation
def stop_game():
    global game_running
    game_running = False

# Function to reset the grid
def reset_grid():
    stop_game()
    initialize_grid()

# Create a frame for AI TV LIVE and Game of Life
main_frame = tk.Frame(root)
main_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# AI TV LIVE! section
tv_frame = tk.Frame(main_frame)
tv_frame.pack(side=tk.TOP, padx=10, pady=10, fill=tk.BOTH, expand=True)

# Create AI TV LIVE! window for messages
tv_window = tk.Text(tv_frame, state=tk.DISABLED, wrap=tk.WORD, height=5)
tv_window.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Create a canvas for Game of Life graphical content
canvas = tk.Canvas(main_frame, width=GRID_SIZE * CELL_SIZE, height=GRID_SIZE * CELL_SIZE, bg="white")
canvas.pack(padx=10, pady=10)

# Create control buttons for Game of Life
control_frame = tk.Frame(root)
control_frame.pack(pady=20)

start_button = tk.Button(control_frame, text="Start AI TV LIVE!", command=start_game)
start_button.pack(side=tk.LEFT, padx=5)

stop_button = tk.Button(control_frame, text="Stop", command=stop_game)
stop_button.pack(side=tk.LEFT, padx=5)

reset_button = tk.Button(control_frame, text="Reset", command=reset_grid)
reset_button.pack(side=tk.LEFT, padx=5)

# Initialize the grid and draw it for the first time
initialize_grid()

# Run the application
root.mainloop()
