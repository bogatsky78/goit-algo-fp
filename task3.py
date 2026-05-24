import heapq


def dijkstra(graph: dict, start: str) -> dict:
    distances = {vertex: float("inf") for vertex in graph}
    distances[start] = 0

    # Min-heap: (distance, vertex)
    heap = [(0, start)]

    while heap:
        current_dist, current_vertex = heapq.heappop(heap)

        # Skip stale entries
        if current_dist > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))

    return distances


def print_result(distances: dict, start: str) -> None:
    print(f"Найкоротші шляхи від вершини '{start}':")
    for vertex, dist in sorted(distances.items()):
        label = str(dist) if dist != float("inf") else "недосяжна"
        print(f"  до '{vertex}': {label}")


if __name__ == "__main__":
    # Fбстрактний граф (6 вершин) ---
    print("=== Приклад 1 ===")
    graph1 = {
        "A": {"B": 1, "C": 4},
        "B": {"A": 1, "C": 2, "D": 5},
        "C": {"A": 4, "B": 2, "D": 1, "E": 3},
        "D": {"B": 5, "C": 1, "E": 2, "F": 4},
        "E": {"C": 3, "D": 2, "F": 1},
        "F": {"D": 4, "E": 1},
    }
    print_result(dijkstra(graph1, "A"), "A")

    # --- Приклад 2: карта міст України (відстані в км) ---
    print("\n=== Приклад 2: міста України ===")
    graph2 = {
        "Київ":       {"Харків": 480, "Житомир": 140, "Черкаси": 200, "Полтава": 345},
        "Харків":     {"Київ": 480, "Полтава": 145, "Дніпро": 215, "Суми": 180},
        "Дніпро":     {"Харків": 215, "Запоріжжя": 85, "Черкаси": 280, "Полтава": 180},
        "Запоріжжя":  {"Дніпро": 85, "Херсон": 200, "Маріуполь": 230},
        "Херсон":     {"Запоріжжя": 200, "Миколаїв": 70, "Маріуполь": 300},
        "Миколаїв":   {"Херсон": 70, "Одеса": 130},
        "Одеса":      {"Миколаїв": 130, "Черкаси": 430},
        "Черкаси":    {"Київ": 200, "Дніпро": 280, "Одеса": 430, "Полтава": 260},
        "Полтава":    {"Київ": 345, "Харків": 145, "Дніпро": 180, "Черкаси": 260},
        "Суми":       {"Харків": 180},
        "Маріуполь":  {"Запоріжжя": 230, "Херсон": 300},
        "Житомир":    {"Київ": 140},
    }
    print_result(dijkstra(graph2, "Київ"), "Київ")
