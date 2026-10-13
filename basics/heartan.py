import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random

# --- Base Heart Function ---
t = np.linspace(0, 2*np.pi, 1000)
hx = 16*np.sin(t)**3
hy = 13*np.cos(t) - 5*np.cos(2*t) - 2*np.cos(3*t) - np.cos(4*t)

# --- Setup ---
fig = plt.figure(figsize=(7,7))
ax = plt.axes()
ax.set_facecolor("black")
ax.axis("off")

# Deep red neon color
neon_red = (0.9, 0.05, 0.05)

# Main heart (neon)
main_heart, = ax.plot(hx, hy, color=neon_red, linewidth=4)

# Glow layers (fixed brightness)
glow_layers = []
for lw in [7, 10, 14]:
    glow = ax.plot(hx * 1.02, hy * 1.02, color=neon_red, linewidth=lw, alpha=0.12)[0]
    glow_layers.append(glow)

# Small flying hearts (very few)
HEART_COUNT = 6
flying = []
fdata = []

for _ in range(HEART_COUNT):
    line, = ax.plot([], [], color=neon_red, linewidth=1.2, alpha=0.9)
    flying.append(line)
    fdata.append({
        "s": random.uniform(0.04, 0.08),
        "x": random.uniform(-5, 5),
        "y": random.uniform(-5, 5),
        "life": random.randint(20, 50),
        "speed": random.uniform(0.10, 0.30)
    })

# Neon title
title = ax.text(0, 23, "ARSENIA <3",
                fontsize=35,
                ha="center",
                color=neon_red,
                fontweight="bold")


# --- Animation ---
def update(frame):

    # Animate small hearts
    for i, h in enumerate(flying):
        fd = fdata[i]

        fd["life"] -= 1

        if fd["life"] <= 0:
            # reset heart
            fd["s"] = random.uniform(0.03, 0.08)
            fd["x"] = random.uniform(-3, 3)
            fd["y"] = random.uniform(-3, 3)
            fd["life"] = random.randint(20, 50)
            fd["speed"] = random.uniform(0.10, 0.30)

        # Heart grows fast then disappears
        fd["s"] += fd["speed"]

        # draw
        xx = hx * fd["s"] + fd["x"]
        yy = hy * fd["s"] + fd["y"]
        h.set_data(xx, yy)

        # disappear fast
        if fd["life"] < 10:
            h.set_alpha(fd["life"] / 10)
        else:
            h.set_alpha(0.9)

    ax.set_xlim(-25, 25)
    ax.set_ylim(-25, 25)

    return flying + glow_layers + [main_heart, title]


anim = FuncAnimation(fig, update, frames=1000, interval=20)
plt.show()