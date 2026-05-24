import random
from collections import Counter
import matplotlib.pyplot as plt

ROLLS = 1_000_000

ANALYTICAL = {
    2: 1, 3: 2, 4: 3, 5: 4, 6: 5,
    7: 6, 8: 5, 9: 4, 10: 3, 11: 2, 12: 1,
}


def simulate(rolls: int) -> dict[int, float]:
    counts = Counter(
        random.randint(1, 6) + random.randint(1, 6)
        for _ in range(rolls)
    )
    return {s: counts[s] / rolls for s in range(2, 13)}


def print_table(mc: dict[int, float]) -> None:
    print(f"{'Sum':>4} | {'Monte Carlo':>11} | {'Analytical':>10} | {'Δ':>7}")
    print("-" * 42)
    for s in range(2, 13):
        exact = ANALYTICAL[s] / 36
        diff = mc[s] - exact
        print(f"{s:>4} | {mc[s]:>10.2%} | {exact:>9.2%} | {diff:>+7.4f}")


def plot(mc: dict[int, float]) -> None:
    sums = list(range(2, 13))
    mc_vals = [mc[s] * 100 for s in sums]
    an_vals = [ANALYTICAL[s] / 36 * 100 for s in sums]

    x = range(len(sums))
    width = 0.4

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar([i - width / 2 for i in x], mc_vals, width, label="Monte Carlo", color="#4C72B0")
    ax.bar([i + width / 2 for i in x], an_vals, width, label="Analytical", color="#DD8452", alpha=0.8)

    ax.set_xticks(list(x))
    ax.set_xticklabels(sums)
    ax.set_xlabel("Sum of two dice")
    ax.set_ylabel("Probability (%)")
    ax.set_title(f"Dice roll probability — Monte Carlo ({ROLLS:,} rolls) vs Analytical")
    ax.legend()
    ax.grid(axis="y", linestyle="--", alpha=0.5)

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    print(f"Simulating {ROLLS:,} rolls...\n")
    mc = simulate(ROLLS)
    print_table(mc)
    plot(mc)
