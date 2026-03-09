import numpy as np
import matplotlib.pyplot as plt

# scale matrix to make it visible
scale = 60

def plot_save(matrix, title, filename, cmap='gray'):
    
    img = np.kron(matrix, np.ones((scale, scale)))
    
    plt.figure()
    plt.imshow(img, cmap=cmap, vmin=0, vmax=1)
    plt.title(title)
    plt.axis('off')
    
    plt.savefig(filename, bbox_inches='tight', pad_inches=0)
    plt.show()


# --------------------
# Case 1: Center white square
# --------------------
p1 = np.array([
[0,0,0,0,0],
[0,0,0,0,0],
[0,0,1,0,0], 
[0,0,0,0,0],
[0,0,0,0,0]
])

plot_save(p1, "Case 1: Center White Square", "case1.png")


# --------------------
# Case 2: Four corners black
# --------------------
p2 = np.array([
[0,1,1,1,0],
[1,1,1,1,1],
[1,1,1,1,1],
[1,1,1,1,1],
[0,1,1,1,0]
])

plot_save(p2, "Case 2: Four Black Corners", "case2.png")


# --------------------
# Case 3: 5×5 white blocks separated by black lines
# --------------------
p3 = np.array([
[0,0,0,0,0,0,0,0,0,0,0],
[0,1,0,1,0,1,0,1,0,1,0],
[0,0,0,0,0,0,0,0,0,0,0],
[0,1,0,1,0,1,0,1,0,1,0],
[0,0,0,0,0,0,0,0,0,0,0],
[0,1,0,1,0,1,0,1,0,1,0],
[0,0,0,0,0,0,0,0,0,0,0],
[0,1,0,1,0,1,0,1,0,1,0],
[0,0,0,0,0,0,0,0,0,0,0],
[0,1,0,1,0,1,0,1,0,1,0],
[0,0,0,0,0,0,0,0,0,0,0]
])

plot_save(p3, "Case 3: 5x5 Grid", "case3.png")


# --------------------
# Case 4: Color corners
# --------------------
p4 = np.ones((5,5,3))

# white background already 1,1,1

p4[0,0] = [0,0,0]     # black
p4[0,4] = [0,0,1]     # blue
p4[4,0] = [0,1,0]     # green
p4[4,4] = [1,0,0]     # red

img4 = np.kron(p4, np.ones((scale, scale,1)))

plt.figure()
plt.imshow(img4)
plt.title("Case 4: Color Corners")
plt.axis('off')

plt.savefig("case4.png", bbox_inches='tight', pad_inches=0)
plt.show()