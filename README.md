# visualisation-python

Clean examples of visualisation code. Uses synthetic retail sales data as a running example.
- 12 stores
- 3970 products
- 63 days (9 weeks)

## packages used

`pathlib`: object-oriented, clean syntax, built-in methods for handling file systems.  
`numpy`: including `.npz` compressed file storage for Numpy arrays.  
`matplotlib.pyplot`: used to visualise a graph structure.  
`seaborn`: built on top of matplotlib.  

## data/
  
`synthetic_data.npz`. Compressed Numpy file containing three arrays:
- `dates`: (63, ) array of integers (not dates).
- `synth_sales_data`: (12, 3970, 63) array of integer sales quantities
- `fitted_line`: (12, 3970, 63) array of doubles fitted through the sales quantities.

## src/

`main.py` is the entry point where you can load data and call functions in the visualisation library.
  
`visualisation.py` is a tiny (but perfectly-formed) visualisation library.
  - `plot_store_product_grid(dates, synth_data, fitted_line)` generates a slightly Tufte-ish panel plot.

 ![seaborn_panel_plot](https://github.com/user-attachments/assets/a43aa5dc-350d-4d04-a8d7-520d4b4f6c1b)

  
