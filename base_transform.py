import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import matplotlib.animation as animation
from matplotlib.animation import PillowWriter

# Set up the grid size and number of players
grid_size = 1600  # You can reduce this size to make it more manageable (e.g., 800x800 or 1600x1600)
num_players = 4

# Initialize the grid with random player cells, using 4 players + empty state
grid = np.random.randint(0, num_players + 1, size=(grid_size, grid_size))

# Set up colors for players using 'gist_rainbow' colormap
colors = plt.cm.gist_rainbow(np.linspace(0, 1, num_players + 1))
cmap = ListedColormap(colors)

# Function to rearrange the existing cells to form a sword that is at least half the size of the grid
def rearrange_to_half_grid_sword(grid):
    center = grid.shape[0] // 2
    half_grid_size = grid.shape[0] // 2

    # Blade (vertical line covering half the grid)
    grid[center - half_grid_size//2:center + half_grid_size//2, center] = 1  # Blade

    # Crossguard (horizontal line that spans the width of the blade area)
    grid[center, center - half_grid_size//3:center + half_grid_size//3] = 2  # Crossguard

    # Handle (shorter vertical line below the crossguard)
    grid[center + half_grid_size//2:center + half_grid_size//2 + 200, center] = 3  # Handle

    return grid

# Function to rearrange the existing cells to form a dog-like shape
def rearrange_to_dog(grid):
    center = grid.shape[1] // 2

    # Dog's body (a rectangle in the middle)
    grid[center-10:center+10, center-15:center+15] = 1  # Body

    # Dog's head (a smaller square above the body)
    grid[center-20:center-10, center-12:center+12] = 2  # Head

    # Dog's legs (four small rectangles)
    grid[center+10:center+15, center-18:center-15] = 3  # Front left leg
    grid[center+10:center+15, center+15:center+18] = 3  # Front right leg
    grid[center-5:center, center-18:center-15] = 3  # Back left leg
    grid[center-5:center, center+15:center+18] = 3  # Back right leg

    return grid

# Function to rearrange the existing cells to form a house-like shape
def rearrange_to_house(grid):
    center = grid.shape[1] // 2

    # House base (square for the main structure)
    grid[center-10:center+10, center-15:center+15] = 1  # House base

    # Roof (triangle-like top part)
    for i in range(10):
        grid[center-20+i, center-i:center+i+1] = 2  # Roof

    # Door (rectangle in the middle of the house base)
    grid[center+5:center+10, center-3:center+3] = 3  # Door

    return grid

# Function to create frames for rearranging from sword to dog to house
def rearrange_sequence(grid, steps):
    frames = []

    # Rearrange to sword
    grid_sword = rearrange_to_half_grid_sword(grid.copy())
    for _ in range(steps):
        frames.append(grid_sword.copy())

    # Rearrange to dog
    grid_dog = rearrange_to_dog(grid.copy())
    for _ in range(steps):
        frames.append(grid_dog.copy())

    # Rearrange to house
    grid_house = rearrange_to_house(grid.copy())
    for _ in range(steps):
        frames.append(grid_house.copy())

    return frames

# Set up parameters for animation
steps = 100  # Number of frames for each shape
frames = rearrange_sequence(grid, steps)

# Create the figure for animation
fig, ax = plt.subplots()
img = ax.imshow(frames[0], cmap=cmap, interpolation='nearest')
ax.axis('off')

# Update function for each frame
def update_frame(i):
    img.set_data(frames[i])
    return img

# Create the animation
ani = animation.FuncAnimation(fig, update_frame, frames=len(frames), interval=150, repeat=False)

# Save the animation as a GIF
gif_filename = "sword_to_dog_to_house.gif"
ani.save(gif_filename, writer=PillowWriter(fps=10))

# Display the saved GIF (this requires an environment that can display GIFs)
from IPython.display import Image
Image(gif_filename)
