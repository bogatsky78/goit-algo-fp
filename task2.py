import math
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection


def collect_segments(x, y, angle, length, depth, max_depth, segments):
    if depth == 0:
        return

    x2 = x + length * math.cos(math.radians(angle))
    y2 = y + length * math.sin(math.radians(angle))

    segments[depth].append(((x, y), (x2, y2)))

    new_length = length * math.sqrt(2) / 2
    collect_segments(x2, y2, angle + 45, new_length, depth - 1, max_depth, segments)
    collect_segments(x2, y2, angle - 45, new_length, depth - 1, max_depth, segments)


def main():
    depth = int(input("Введіть рівень рекурсії (1-15): "))
    depth = max(1, min(depth, 15))

    segments = {d: [] for d in range(1, depth + 1)}
    collect_segments(0, 0, 90, 100, depth, depth, segments)

    fig, ax = plt.subplots(figsize=(10, 10))
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_facecolor("#f0ede0")
    fig.patch.set_facecolor("#f0ede0")
    ax.set_title(f"Дерево Піфагора — рівень рекурсії: {depth}", fontsize=14)

    for d, segs in segments.items():
        # d == depth → trunk (darkest); d == 1 → tips (lightest)
        t = (d - 1) / max(depth - 1, 1)  # 0.0 at tips, 1.0 at trunk
        color = (0.3 - 0.1 * t, 0.4 + 0.35 * t, 0.1 + 0.1 * t)
        lw = max(0.4, d * 0.5)
        lc = LineCollection(segs, colors=[color], linewidths=lw)
        ax.add_collection(lc)

    ax.autoscale()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
