import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the grid size and basic shapes
GRID_SIZE = 20

# Define five basic shapes: square, triangle, circle, cross, and DNA-like shape
shapes = {
    "square": np.array([
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1]
    ]),
    "triangle": np.array([
        [0, 0, 1, 0, 0],
        [0, 1, 1, 1, 0],
        [1, 1, 1, 1, 1]
    ]),
    "circle": np.array([
        [0, 1, 1, 1, 0],
        [1, 1, 0, 1, 1],
        [1, 0, 0, 0, 1],
        [1, 1, 0, 1, 1],
        [0, 1, 1, 1, 0]
    ]),
    "cross": np.array([
        [0, 1, 0],
        [1, 1, 1],
        [0, 1, 0]
    ]),
    "dna": np.array([
        [0, 0, 1, 0, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 0, 1, 0],
        [1, 0, 0, 1, 0, 0, 0, 1],
        [0, 1, 0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 0, 1, 0, 0]
    ])
}

# Function to center a shape on the grid
def center_shape_on_grid(grid_size, shape):
    grid = np.zeros((grid_size, grid_size), dtype=int)
    shape_height, shape_width = shape.shape
    start_x = (grid_size - shape_height) // 2
    start_y = (grid_size - shape_width) // 2
    grid[start_x:start_x + shape_height, start_y:start_y + shape_width] = shape
    return grid

# Define the function to update the grid for animation
def update_shape(frame_num, img, grid):
    new_grid = grid.copy()
    mutation_rate = 0.1  # Mutation rate to simulate randomness

    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if np.random.rand() < mutation_rate:
                new_grid[i, j] = 1 if grid[i, j] == 0 else 0  # Mutate randomly

            # Apply Game of Life rules
            neighbors = sum(grid[(i + dx) % GRID_SIZE, (j + dy) % GRID_SIZE]
                            for dx in (-1, 0, 1) for dy in (-1, 0, 1)
                            if dx != 0 or dy != 0)
            if grid[i, j] == 1 and (neighbors < 2 or neighbors > 3):
                new_grid[i, j] = 0
            elif grid[i, j] == 0 and neighbors == 3:
                new_grid[i, j] = 1

    img.set_data(new_grid)
    grid[:] = new_grid
    return img,

# Create a video for each shape
def create_animation_for_shape(shape_name, shape, file_name):
    grid_with_shape = center_shape_on_grid(GRID_SIZE, shape)

    fig, ax = plt.subplots()
    img = ax.imshow(grid_with_shape, interpolation='nearest', cmap='gist_rainbow')
    plt.title(f"Evolving {shape_name.capitalize()} Shape Animation")

    ani_shape = animation.FuncAnimation(fig, lambda frame: update_shape(frame, img, grid_with_shape), frames=30, blit=True)
    ani_shape.save(file_name, writer='imagemagick', fps=10)
    plt.close()

# List of shapes to animate
shape_list = ["square", "triangle", "circle", "cross", "dna"]

# Generate and save animations for all shapes
for shape_name in shape_list:
    shape = shapes[shape_name]
    file_name = f"{shape_name}_shape_evolution.gif"
    create_animation_for_shape(shape_name, shape, file_name)
