import numpy as np
from pathlib import Path

import visualisation as viz


"""
# pathlib is nice:
# - cwd: current working directory
# - cwd.parent: up one level from the current working directory
# - note that / is not in quotation marks. pathlib overloads / to become an operator that joins strings.
# - we go from the current "src/" folder, up to the parent and back down to the "data/" folder.
"""

# Specify the path to the data
cwd = Path.cwd()
data_path = cwd.parent / "data" / "synthetic_data.npz"

"""
npz is great:
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

# Select a subset of data to plot. Don't try to plot the whole dataset at once!
num_stores = 3
num_products = 3

synth_data_subset = synth_sales_data[:num_stores, :num_products, :]
fitted_line_subset = fitted_line[:num_stores, :num_products, :]

# Generate a (quite stylish) panel plot
viz.plot_store_product_grid(dates, synth_data_subset, fitted_line_subset)