import matplotlib.pyplot as plt 
import matplotlib.patches as patches

A = (0, 0) B = (4, -0.5) C = (2, 3)

fig, ax = plt.subplots(figsize=(8, 8))

x = [A[0], B[0], C[0], A[0]] y = [A[1], B[1], C[1], A[1]]
ax.plot(x, y, color='black', linewidth=2)

r = 0.85

circle1 = patches.Circle(A, r, fill=False, edgecolor='black', linewidth=2)
circle2 = patches.Circle(B, r, fill=False, edgecolor='black', linewidth=2)
circle3 = patches.Circle(C, r, fill=False, edgecolor='black', linewidth=2)

ax.add_patch(circle1) ax.add_patch(circle2) ax.add_patch(circle3)

ax.set_aspect('equal') ax.set_xlim(-1.2, 5.2) ax.set_ylim(-1.5, 4.2) ax.axis('off')
plt.title("Triangle and Three Circles") plt.show()