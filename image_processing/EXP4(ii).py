import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors

def show_college_patterns_uniform():
    # 1. Define the 3x3 Spatial Masks (1=Active, 0=Background)
    
    # Pattern (i): Point / Impulse
    p1 = np.array([[0, 0, 0],
                   [0, 1, 0],
                   [0, 0, 0]])
    
    # Pattern (ii): Corners
    p2 = np.array([[1, 0, 1],
                   [0, 0, 0],
                   [1, 0, 1]])
    
    # Pattern (iii): Cross / X-Junction
    p3 = np.array([[1, 0, 1],
                   [0, 1, 0],
                   [1, 0, 1]])

    patterns = [p1, p2, p3]
    titles = ["(i) Point", "(ii) Corners", "(iii) Cross/X"]

    # 2. Setup Figure
    fig, axes = plt.subplots(2, 3, figsize=(10, 7))
    plt.subplots_adjust(hspace=0.4) # Add space between rows
    
    # 3. Define Colors
    # Row 1: Standard Binary (0=White, 1=Black)
    cmap_bw = colors.ListedColormap(['white', 'black'])
    
    # Row 2: Uniform Color Mask (0=Light Gray, 1=Cyan/Blue)
    # "All three bottom cases have the same color"
    uniform_color = '#00BCD4' # Cyan
    cmap_color = colors.ListedColormap(['#F5F5F5', uniform_color])

    # 4. Plotting Loop
    for i in range(3):
        # --- TOP ROW: Type i (Black & White) ---
        ax_top = axes[0, i]
        ax_top.imshow(patterns[i], cmap=cmap_bw, vmin=0, vmax=1)
        
        # Grid settings for Top Row
        ax_top.set_xticks(np.arange(-0.5, 3, 1), minor=True)
        ax_top.set_yticks(np.arange(-0.5, 3, 1), minor=True)
        ax_top.grid(which='minor', color='gray', linestyle='-', linewidth=1)
        ax_top.tick_params(which='minor', bottom=False, left=False)
        
        ax_top.set_title(f"Type i (Binary)\n{titles[i]}")
        ax_top.set_xticks([])
        ax_top.set_yticks([])

        # --- BOTTOM ROW: Type ii (Uniform Color) ---
        ax_bot = axes[1, i]
        ax_bot.imshow(patterns[i], cmap=cmap_color, vmin=0, vmax=1)
        
        # Grid settings for Bottom Row
        ax_bot.set_xticks(np.arange(-0.5, 3, 1), minor=True)
        ax_bot.set_yticks(np.arange(-0.5, 3, 1), minor=True)
        ax_bot.grid(which='minor', color='white', linestyle='-', linewidth=2)
        ax_bot.tick_params(which='minor', bottom=False, left=False)
        
        ax_bot.set_title(f"Type ii (Color Mask)\n{titles[i]}")
        ax_bot.set_xticks([])
        ax_bot.set_yticks([])

    plt.suptitle("3x3 Structuring Elements (Binary vs. Color Mask)", fontsize=14)
    plt.show()
    plt.savefig("college_patterns_uniform.png")

if __name__ == "__main__":
    show_college_patterns_uniform()