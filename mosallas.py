import random
import matplotlib.pyplot as plt


vertices = [(0, 0), (1, 0), (0.5, 0.866)]
colors = ["red", "green", "blue"]

x, y = random.random(), random.random()

xs, ys, cs = [], [], []
for _ in range(50000):
    i = random.randrange(3) 
    vx, vy = vertices[i]
    x, y = (x + vx) / 2, (y + vy) / 2
    xs.append(x)
    ys.append(y)
    cs.append(colors[i])

plt.figure(figsize=(8, 8))
plt.scatter(xs, ys, s=0.1, c=cs)
plt.axis("equal")
plt.axis("off")
plt.show()