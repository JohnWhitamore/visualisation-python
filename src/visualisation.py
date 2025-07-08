import igraph as ig
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

import seaborn as sns

class PanelPlot:

    def plot_store_product_grid(self, dates, synth_data, fitted_line):
        
        # Dimensions
        S, P, N = synth_data.shape
    
        # Labels
        store_labels = [f"Store {s+1}" for s in range(S)]
        product_labels = [f"Product {p+1}" for p in range(P)]
    
        # Colours
        synth_data_colour = (90/255, 140/255, 160/255)
        fit_colour = (190/255, 110/255, 60/255)
        error_zone_colour = (190/255, 190/255, 190/255)
    
        # Figure
        fig, axes = plt.subplots(P, S, figsize=(S * 4.5, P * 3), sharex=True, sharey=True)
        sns.set_style("white")
    
        # Handle axes correctly for various values of S and P
        if S == 1 and P == 1:
            axes = np.array([[axes]])
        elif P == 1:
            axes = axes[np.newaxis, :]
        elif S == 1:
            axes = axes[:, np.newaxis]
    
        # Loop through stocking-points
        for s in range(S):
            for p in range(P):
    
                # Data
                ax = axes[p, s]
                obs = synth_data[s, p, :]
                fit = fitted_line[s, p, :]
                lower = np.maximum(fit - np.sqrt(fit), 0)
                upper = fit + np.sqrt(fit)
    
                # Plot the data
                ax.scatter(dates, obs, color=synth_data_colour, s=30, alpha=0.6,
                            edgecolors=(30/255, 30/255, 30/255), linewidth=0.5)
                ax.plot(dates, fit, color=fit_colour, alpha=0.8, linewidth=1.5)
                ax.fill_between(dates, lower, upper, color=error_zone_colour, alpha=0.2)
    
                # Demarcate weeks
                for week in range(0, N, 7):
                    ax.axvline(x=week, color=(90/255, 90/255, 90/255), linewidth=0.8, linestyle="--", alpha=0.6)
                    
                # Align x-axis labels with weeks
                week_ticks = np.arange(0, N, 7)
                ax.set_xticks(week_ticks)
                ax.set_xticklabels([str(w) for w in week_ticks])
    
                # Tufte says to remove unnecessary ink, right?
                for spine in ax.spines.values():
                    spine.set_visible(False)
                ax.tick_params(left=False, bottom=False)
                ax.set_xlabel("")
                ax.set_ylabel("")
    
                # Labels
                if p == 0:
                    ax.set_title(store_labels[s], fontsize=10)
                if s == 0:
                    ax.text(-0.1, 0.5, product_labels[p], va='center', ha='right',
                            transform=ax.transAxes, fontsize=10, rotation=90)
    
        plt.tight_layout()
        plt.show()
        
    def set_visual_parameters(self, grid_size):
        
        if grid_size == 1:
                
            mean_linewidth = 4.0
            mean_alpha = 1.0
            
            obs_s = 300
            obs_linewidth = 2.0
            obs_alpha = 0.8
            
            label_fontsize = 30
            axis_fontsize = 24
            
        elif grid_size == 2:
            
            mean_linewidth = 3.5
            mean_alpha = 0.9
            
            obs_s = 150
            obs_linewidth = 1.5
            obs_alpha = 0.6
            
            label_fontsize = 24
            axis_fontsize = 20
            
        elif grid_size <= 4:
            
            mean_linewidth = 3.25
            mean_alpha = 0.8
            
            obs_s = 100
            obs_linewidth = 1.0
            obs_alpha = 0.4
            
            label_fontsize = 18
            axis_fontsize = 16
            
        else:
            
            mean_linewidth = 3.0
            mean_alpha = 0.7
            
            obs_s = 50
            obs_linewidth = 0.5
            obs_alpha = 0.3
            
            label_fontsize = 12
            axis_fontsize = 12
            
        return mean_linewidth, mean_alpha, obs_s, obs_linewidth, obs_alpha, label_fontsize, axis_fontsize
    
    def plot_store_product_grid_gif(self, dates, synth_data, fitted_line, grid_size, n):
    
        # ... dimensions
        S, P, N = synth_data.shape
        
        # ... labels
        store_labels = [f"Store {s+1}" for s in range(S)]
        product_labels = [f"Product {p+1}" for p in range(P)]
    
        # ... colours
        synth_data_colour = (90/255, 140/255, 160/255)
        fit_colour = (190/255, 110/255, 60/255)
        
        # ... figure and axes
        fig, axes = plt.subplots(grid_size, grid_size, figsize=(S * 4.5, P * 3), sharex=True, sharey=True)
        sns.set_style("white")
        
        # ... handle axes correctly for various values of S and P
        if grid_size == 1:
            axes = np.array([[axes]])
            
        # ... set visual parameters according to grid_size
        visual_params = self.set_visual_parameters(grid_size)
        mean_linewidth, mean_alpha, obs_s, obs_linewidth, obs_alpha, label_fontsize, axis_fontsize = visual_params
    
        # ... loop through stocking-points
        for s in range(grid_size):
            
            for p in range(grid_size):
                
                # ... data
                ax = axes[p, s]
                mean = fitted_line[s, p, :n]
                obs = synth_data[s, p, :n]
                        
                # ... plot the data
                ax.plot(dates[:n], mean, color=fit_colour, alpha=mean_alpha, linewidth=mean_linewidth)
                ax.scatter(dates[:n], obs, color=synth_data_colour, s=obs_s, alpha=obs_alpha,
                           edgecolors=(30/255, 30/255, 30/255), linewidth=obs_linewidth)
                    
                # ... Tufte
                for spine in ax.spines.values():
                    spine.set_visible(False)
                ax.tick_params(left=False, bottom=False)
                ax.set_xlabel("")
                ax.set_ylabel("")
                
                # ... store and product labels
                if p == 0:
                    ax.set_title(store_labels[s], fontsize=label_fontsize)
                if s == 0:
                    ax.text(-0.1, 0.5, product_labels[p], va='center', ha='right',
                            transform=ax.transAxes, fontsize=label_fontsize, rotation=90)
                
                # ... weeks
                
                # - vertical demarcation
                for week in range(0, N, 7):
                    ax.axvline(x=week, color=(90/255, 90/255, 90/255), linewidth=0.8, linestyle="--", alpha=0.6)
                
                # - x-axis labels
                week_ticks = np.arange(0, N, 7)
                ax.set_xticks(week_ticks)
                ax.set_xticklabels([str(w) for w in week_ticks])
                
                ax.tick_params(axis='x', labelsize=axis_fontsize)
                ax.tick_params(axis='y', labelsize=axis_fontsize)
    
                # ... axes
                ax.set_xlim(dates[0], dates[-1])
                ax.set_ylim(0, np.max(synth_data) * 1.1)
                
        plt.tight_layout()
    
        return fig, axes
    
class GraphStructure: 
    
    def create_layout(self, stores, products, 
                      store_groups, product_groups,
                      store_to_group, product_to_group):

        # ... initialise the layout as a list
        layout = []
        
        # ... build lookup dictionaries
        store_x = {s: i for i, s in enumerate(stores)}
        product_y = {p: i for i, p in enumerate(products)}
        
        # ... store groups (above stores in the hierarchy)
        for sg in store_groups:
            
            # ... place above the average x-coordinate of its stores
            child_stores = [s for s in stores if store_to_group[s] == sg]
            x = sum(store_x[s] for s in child_stores) / len(child_stores)
            layout.append((x, len(products) + 2))
        
        # ... stores (above product_locations in the hierarchy)
        for s in stores:
            
            layout.append((store_x[s], len(products) + 1))
        
        # ... product groups (left of products)
        for pg in product_groups:
            
            # ... place to the left of the average y-coordinate of its products
            child_products = [p for p in products if product_to_group[p] == pg]
            y = sum(product_y[p] for p in child_products) / len(child_products)
            layout.append((-2, y))  
        
        # ... products (left of product_locations)
        for p in products:
            layout.append((-1, product_y[p]))
        
        # ... product-Locations (grid interior)
        for s in stores:
            for p in products:
                layout.append((store_x[s], product_y[p]))
                
        return layout
        

    def create_figure(self, g, layout, colours, type_to_colour):
        
        # ... plot size
        fig, ax = plt.subplots(figsize=(14, 10))

        # ... igraph plot() function
        ig.plot(
            g,
            layout=layout,
            target=ax,
            vertex_label = g.vs["name"],
            vertex_color=colours,
            vertex_size=20,
            edge_arrow_size=0.5,
            edge_color="gray"
        )

        ax.axis("off")
        
        # ... legend
        legend_handles = [
            mpatches.Patch(color=colour, label=label.replace("_", " ").title())
            for label, colour in type_to_colour.items()
        ]
        
        ax.legend(handles=legend_handles, loc="upper left", frameon=False, fontsize=10)
        
        return fig, ax