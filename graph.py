import numpy as np
import matplotlib.pyplot as plt

# Generate a range of x values
x = np.linspace(-np.pi, np.pi, 100)

# Compute sin(x) and cos(x)
y_sin = np.sin(x)
y_cos = np.cos(x)

# Create a new figure
plt.figure()

# Plot sin(x)
plt.plot(x, y_sin, label='sin(x)')
# Plot cos(x)
plt.plot(x, y_cos, label='cos(x)')

# Set the limit of x and y axis
plt.xlim(-np.pi, np.pi)
plt.ylim(-1.5, 1.5)

# Add a legend
plt.legend()

# Show the plot
plt.show()
