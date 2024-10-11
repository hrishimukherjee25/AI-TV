import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the grid size and DNA shape
GRID_SIZE = 20
dna_shape = np.array([
    [0, 0, 1, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 1, 0, 1, 0],
    [1, 0, 0, 1, 0, 0, 0, 1],
    [0, 1, 0, 0, 1, 0, 1, 0],
    [0, 0, 1, 0, 0, 1, 0, 0]
])

# Determine the placement of the DNA shape in the grid
shape_height, shape_width = dna_shape.shape
start_x = (GRID_SIZE - shape_height) // 2
start_y = (GRID_SIZE - shape_width) // 2

# Initialize the grid with the DNA shape correctly centered
grid_with_dna_shape = np.zeros((GRID_SIZE, GRID_SIZE), dtype=int)
for i in range(shape_height):
    for j in range(shape_width):
        grid_with_dna_shape[start_x + i, start_y + j] = dna_shape[i, j]

# Define the function to update the grid
def update_with_dna_shape(frame_num, img, grid):
    new_grid = grid.copy()
    mutation_rate = 0.1  # Mutation rate to simulate randomness

    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if np.random.rand() < mutation_rate:
                new_grid[i, j] = 1 if grid[i, j] == 0 else 0  # Mutate randomly

            # Apply Game of Life rules outside the DNA shape area
            if not (start_x <= i < start_x + shape_height and start_y <= j < start_y + shape_width):
                count = sum(grid[(i + dx) % GRID_SIZE, (j + dy) % GRID_SIZE]
                            for dx in (-1, 0, 1) for dy in (-1, 0, 1)
                            if dx != 0 or dy != 0)
                if grid[i, j] == 1 and (count < 2 or count > 3):
                    new_grid[i, j] = 0
                elif grid[i, j] == 0 and count == 3:
                    new_grid[i, j] = 1

    img.set_data(new_grid)
    grid[:] = new_grid
    return img,

# Set up the plot for video animation
fig, ax = plt.subplots()
img = ax.imshow(grid_with_dna_shape, interpolation='nearest', cmap='gist_rainbow')
plt.title("Evolving DNA-Like Shape Animation")

# Create the video animation
ani_video = animation.FuncAnimation(fig, lambda frame: update_with_dna_shape(frame, img, grid_with_dna_shape), frames=30, blit=True)

# Save the video
video_path = 'DNA_Shape_Evolution.mp4'
ani_video.save('DNA_Shape_Evolution.gif', writer='imagemagick', fps=10)


plt.close()  # Close the plot to prevent it from displaying now
