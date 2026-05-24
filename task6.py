items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350},
}


def greedy_algorithm(items, budget):
    sorted_items = sorted(
        items.items(),
        key=lambda x: x[1]["calories"] / x[1]["cost"],
        reverse=True,
    )

    selected = []
    total_calories = 0
    remaining = budget

    for name, data in sorted_items:
        if data["cost"] <= remaining:
            selected.append(name)
            total_calories += data["calories"]
            remaining -= data["cost"]

    return selected, total_calories


def dynamic_programming(items, budget):
    names = list(items.keys())
    costs = [items[n]["cost"] for n in names]
    calories = [items[n]["calories"] for n in names]
    n = len(names)

    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        cost = costs[i - 1]
        cal = calories[i - 1]
        for b in range(budget + 1):
            dp[i][b] = dp[i - 1][b]
            if cost <= b and dp[i - 1][b - cost] + cal > dp[i][b]:
                dp[i][b] = dp[i - 1][b - cost] + cal

    selected = []
    b = budget
    for i in range(n, 0, -1):
        if dp[i][b] != dp[i - 1][b]:
            selected.append(names[i - 1])
            b -= costs[i - 1]

    total_calories = dp[n][budget]
    return selected, total_calories


if __name__ == "__main__":
    budget = 100

    greedy_items, greedy_cal = greedy_algorithm(items, budget)
    print(f"Greedy algorithm (budget={budget}):")
    print(f"  Selected: {greedy_items}")
    print(f"  Total calories: {greedy_cal}")
    print(f"  Total cost: {sum(items[i]['cost'] for i in greedy_items)}")

    print()

    dp_items, dp_cal = dynamic_programming(items, budget)
    print(f"Dynamic programming (budget={budget}):")
    print(f"  Selected: {dp_items}")
    print(f"  Total calories: {dp_cal}")
    print(f"  Total cost: {sum(items[i]['cost'] for i in dp_items)}")
