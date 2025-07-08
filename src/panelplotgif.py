import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt
import imageio.v2 as iio

from visualisation import PanelPlot


"""
# pathlib:
# - cwd: current working directory
# - cwd.parent: up one level from the current working directory
# - note that / is not in quotation marks. pathlib overloads / to become an operator that joins strings.
# - we go from the current "src/" folder, up to the parent and back down to the "data/" folder.
"""

# Specify paths
cwd = Path.cwd()

# ... path to the data file
data_path = cwd.parent / "data" / "synthetic_data.npz"

# ... path to the folder in which to store frames for the GIF
frames_path = cwd.parent / "frames"

# ... create the frames folder (and any required parent folders) if it doesn't already exist
frames_path.mkdir(parents=True, exist_ok=True)


"""
npz:
- very fast
- the .names attribute (e.g. data.names) contains the names of the arrays in the file
"""

# Load the npz file
data = np.load(data_path)

# Access individual arrays by name
dates = data["dates"]
synth_sales_data = data["synth_sales_data"]
fitted_line = data["fitted_line"]

# Print the shapes of the arrays
print(dates.shape)
print(synth_sales_data.shape)
print(fitted_line.shape)


"""
Don't try to plot the whole dataset at once!
Keep the grid size relatively small.
"""

max_grid_size = 8

synth_data_subset = synth_sales_data[:max_grid_size, :max_grid_size, :]
fitted_line_subset = fitted_line[:max_grid_size, :max_grid_size, :]

# Define a function to set the size of the plotted grid dynamically
def set_grid_size(n):
    
    # Set grid size
    if n < 14:
        
        grid_size = 1
        
    elif n < 28:
        
        grid_size = 2
        
    elif n < 42:
        
        grid_size = 4
        
    else:
        
        grid_size = max_grid_size
        
    return grid_size



# Loop through time steps to create and save frames
N, = dates.shape
pp = PanelPlot()

for n in range(N):
    
    # Set the grid size to display
    grid_size = set_grid_size(n)
    
    # Generate a panel plot
    fig, axes = pp.plot_store_product_grid_gif(dates, synth_data_subset, fitted_line_subset, grid_size, n)
    
    # Save and close the plot
    fig.savefig(f'{frames_path}/frame_{n}.png', dpi=150)
    plt.close(fig)

plt.show()

print("finished creating frames")


# Create the GIF taking care to stream frames into memory and not load all at once
filenames = [f'{frames_path}/frame_{n}.png' for n in range(N)]

with iio.get_writer(f'{frames_path}/dynamic_graph.gif', mode='I', duration=0.5, loop=0) as writer:
    for fn in filenames:
        frame = iio.imread(fn)
        writer.append_data(frame)


print("finished creating GIF")


