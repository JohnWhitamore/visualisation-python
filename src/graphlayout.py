import matplotlib.pyplot as plt

import graph as grph
import visualisation as viz

# Graph structure

# ... stores, each belonging to a store group
store_group_sizes = [2, 1, 2]
num_stores = sum(store_group_sizes)

# ... products, each belonging to a product group
product_group_sizes = [1, 3, 2]
num_products = sum(product_group_sizes)

# ... create the graph
graph_config = num_stores, store_group_sizes, num_products, product_group_sizes
graph_components = grph.create_graph(*graph_config)
g, stores, products, store_groups, product_groups, store_to_group, product_to_group, type_to_colour = graph_components


# Display graph structure

# ... build a grid-based layout
gs = viz.GraphStructure()

layout = gs.create_layout(stores, products, 
                  store_groups, product_groups,
                  store_to_group, product_to_group)

# ... extract the node colours from the graph
colours = g.vs["colour"]

# ... create the figure using the layout
fig, ax = gs.create_figure(g, layout, colours, type_to_colour)
    
# ... display the figure
plt.show()

