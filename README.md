# visualisation-python

Clean examples of visualisation code. Uses synthetic retail sales data as a running example.
- 12 stores
- 3970 products
- 63 days (9 weeks)

The synthetic sales data was generated using ancestral sampling on a graph constructed using `igraph`.

## packages used

`pathlib`: object-oriented, clean syntax, built-in methods for handling file systems.  
`numpy`: including `.npz` compressed file storage for Numpy arrays.  
`matplotlib.pyplot`: used to visualise a graph structure.  
`seaborn`: built on top of matplotlib.  
`imagio`: used to make a GIF.  
`igraph`: used to create a graph (nodes and edges) showing the structure of a hypothetical retail business.  

## data/
  
`synthetic_data.npz`. Compressed Numpy file containing three arrays:
- `dates`: (63, ) array of integers (not dates).
- `synth_sales_data`: (12, 3970, 63) array of integer sales quantities
- `fitted_line`: (12, 3970, 63) array of doubles fitted through the sales quantities.

## src/
 
`visualisation.py` is a tiny (but stylish) visualisation library.

`panelplot.py`
- loads Numpy arrays stored as `.npz`
- `visualisation.PanelPlot.plot_store_products(dates, synth_data, fitted_line)` generates a panel plot.
 ![seaborn_panel_plot](https://github.com/user-attachments/assets/a43aa5dc-350d-4d04-a8d7-520d4b4f6c1b)

`panelplotgif.py`
- like `panelplot.py` but uses a time-loop a) to create frames and b) to zoom out to grids of increasing size
- `visualisation.PanelPlot.plot_store_products_gif(dates, synth_data, fitted_line, grid_size, n)` makes a GIF from panel plot frames.
![dynamic_graph](https://github.com/user-attachments/assets/c6717be5-ac17-477d-9e5e-7e9ee24dc848)

`graphlayout.py`
- creates a graph structure with node types: store group, store, product group, product and product-location.
- `igraph` is used a) to create the graph structure and b) to configure the plot using `igraph.plot()`
- `matplotlib.pyplot` is used to render the graph structure manually.
![graph_structure](https://github.com/user-attachments/assets/e0fbab9b-e7b7-4d07-9322-0770c4ae14dc)

    
