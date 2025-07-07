import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def plot_store_product_grid(dates, synth_data, fitted_line):
    
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
