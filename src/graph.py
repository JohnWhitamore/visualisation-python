import igraph as ig

def create_non_leaf_nodes(node_prefix, node_group_prefix, node_group_sizes):
    
    # ... non-leaf node labels
    node_groups = [node_group_prefix + f"{i}" for i in range(len(node_group_sizes))]
    
    # ... initialise collections
    nodes = []
    node_to_group = {}
    
    # ... iterate through nodes
    for i, size in enumerate(node_group_sizes):
        
        # ... lists of non-leaf nodes e.g. store groups, stores, product groups, products
        group_nodes = [node_prefix + f"{len(nodes) + j}" for j in range(size)]
        nodes.extend(group_nodes)
        
        # ... dictionary mapping stores to store groups, products to product groups
        for s in group_nodes:
            
            node_to_group[s] = node_groups[i]
            
    return node_groups, nodes, node_to_group

def create_leaf_nodes(leaf_node_prefix, parents_A, parents_B):
    
    # ... leaf node labels
    leaf_nodes_2D = [
        [leaf_node_prefix + f"_{a}_{b}" for b in parents_B]
        for a in parents_A
    ]
    
    # ... collection of leaf nodes
    leaf_nodes = [leaf_node for row in leaf_nodes_2D for leaf_node in row]
    
    return leaf_nodes, leaf_nodes_2D

def create_flat_lists_of_vertices(stores, store_groups,
                                  products, product_groups,
                                  product_locations):
    
    # ... flat lists
    vertices = store_groups + stores + product_groups + products + product_locations
    vertex_types = (
        ["store_group"] * len(store_groups) +
        ["store"] * len(stores) +
        ["product_group"] * len(product_groups) +
        ["product"] * len(products) +
        ["product_location"] * len(product_locations)
    )
    
    return vertices, vertex_types

def create_edges(stores, store_to_group, 
                 products, product_to_group, 
                 product_locations_2D):
    
    # ... initialise list of edges
    edges = []
    
    # ... store group to store
    for store, sg in store_to_group.items():
        edges.append((sg, store))
    
    # ... product group to product
    for product, pg in product_to_group.items():
        edges.append((pg, product))
    
    # ... product to product-location and store to product-location
    for i, store in enumerate(stores):
        for j, product in enumerate(products):
            pl_name = product_locations_2D[i][j]
            edges.append((product, pl_name))  # link from product
            edges.append((store, pl_name))    # link from store
            
    return edges

def create_graph(num_stores, store_group_sizes, num_products, product_group_sizes):

    # ... initialize a directed graph
    g = ig.Graph(directed=True)
    
    # Vertices
    
    # ... define store-related nodes
    store_prefix = "S"
    store_group_prefix = "SG"
    store_groups, stores, store_to_group = create_non_leaf_nodes(store_prefix, store_group_prefix, 
                                                                 store_group_sizes)
    
    # ... define product-related nodes
    product_prefix = "P"
    product_group_prefix = "PG"
    product_groups, products, product_to_group = create_non_leaf_nodes(product_prefix, product_group_prefix, 
                                                                       product_group_sizes)
    
    # ... define product-location nodes
    product_location_prefix = "PL"
    product_locations, product_locations_2D = create_leaf_nodes(product_location_prefix, stores, products)
    
    # ... lists of vertices and vertex types
    vertices, vertex_types = create_flat_lists_of_vertices(stores, store_groups,
                                                           products, product_groups,
                                                           product_locations)
    
    # ... add vertices and give them names and types
    g.add_vertices(vertices)
    g.vs["name"] = vertices
    g.vs["type"] = vertex_types
    
    # ... assign colours to each type of node
    type_to_colour = {
        "store_group": "#1f77b4",
        "store": "#2ca02c",
        "product_group": "#ff7f0e",
        "product": "#d62728",
        "product_location": "#9467bd",
        }
    
    g.vs["colour"] = [type_to_colour[t] for t in g.vs["type"]]
    
    # ... assign store and product metadata to product_location nodes
    for v in g.vs.select(type="product_location"):
        _, store_label, product_label = v["name"].split("_", 2)
        v["store_id"] = int(store_label[1:])
        v["product_id"] = int(product_label[1:])
        
    # Edges
            
    # ... create edges
    edges = create_edges(stores, store_to_group, 
                         products, product_to_group, 
                         product_locations_2D)
    
    # ... add edges to the graph
    g.add_edges(edges)
    
    return g, stores, products, store_groups, product_groups, store_to_group, product_to_group, type_to_colour