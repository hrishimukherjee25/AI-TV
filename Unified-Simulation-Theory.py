import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Simulation parameters
grid_size = 100  # Size of the grid
time_steps = 200  # Number of time steps
c = 1  # Propagation speed of the wave
dx = 0.1  # Spatial step
dt = 0.01  # Time step (must satisfy stability condition)

# Create initial fields (Psi at time t and t-1 for the update scheme)
Psi_t = np.zeros((grid_size, grid_size))
Psi_t1 = np.zeros((grid_size, grid_size))

# Initialize a Gaussian pulse in the center of the grid (representing an initial energy field)
x_center, y_center = grid_size // 2, grid_size // 2
width = 5  # Width of the Gaussian pulse
Psi_t[x_center-width:x_center+width, y_center-width:y_center+width] = np.exp(-((np.arange(-width, width)[:, None])**2 + (np.arange(-width, width)[None, :])**2))

# Create a figure for the animation
fig, ax = plt.subplots(figsize=(6, 6))
im = ax.imshow(Psi_t, cmap='inferno', vmin=-0.1, vmax=0.1, interpolation='bilinear')
ax.set_title('Field Propagation Simulation (Wave Equation)')

# Function to update the field using a simplified wave equation
def update_field(t):
    global Psi_t, Psi_t1
    # Apply the wave equation (discretized second-order differential equation)
    Psi_new = 2 * Psi_t - Psi_t1 + (c * dt / dx)**2 * (
        np.roll(Psi_t, 1, axis=0) + np.roll(Psi_t, -1, axis=0) +
        np.roll(Psi_t, 1, axis=1) + np.roll(Psi_t, -1, axis=1) - 4 * Psi_t
    )
    
    # Update the plot
    im.set_array(Psi_new)
    
    # Shift fields for the next time step
    Psi_t1 = Psi_t.copy()
    Psi_t = Psi_new
    
    return [im]

# Create the animation
ani = FuncAnimation(fig, update_field, frames=time_steps, interval=50, blit=True)

# Display the simulation
plt.show()
