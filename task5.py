import heapq
import uuid
from collections import deque

import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root, title=""):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]["color"] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]["label"] for node in tree.nodes(data=True)}

    plt.figure(figsize=(9, 5))
    plt.title(title, fontsize=14, pad=12)
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()


def heap_to_tree(heap: list, index: int = 0) -> Node | None:
    if index >= len(heap):
        return None
    node = Node(heap[index])
    node.left = heap_to_tree(heap, 2 * index + 1)
    node.right = heap_to_tree(heap, 2 * index + 2)
    return node


def build_heap_tree(data: list) -> Node | None:
    heap = data[:]
    heapq.heapify(heap)
    return heap_to_tree(heap)


def _gradient_color(step: int, total: int) -> str:
    """Dark blue → light blue gradient based on visitation order."""
    dark = (18, 30, 120)
    light = (173, 216, 255)
    t = step / max(total - 1, 1)
    r = int(dark[0] + t * (light[0] - dark[0]))
    g = int(dark[1] + t * (light[1] - dark[1]))
    b = int(dark[2] + t * (light[2] - dark[2]))
    return f"#{r:02X}{g:02X}{b:02X}"


def dfs(root: Node) -> list[Node]:
    """Iterative DFS using an explicit stack."""
    if root is None:
        return []
    result = []
    stack = [root]
    while stack:
        node = stack.pop()
        result.append(node)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return result


def bfs(root: Node) -> list[Node]:
    """Iterative BFS using a queue."""
    if root is None:
        return []
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        result.append(node)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result


def visualize_traversal(root: Node, traversal_fn, title: str) -> None:
    order = traversal_fn(root)
    total = len(order)
    for step, node in enumerate(order):
        node.color = _gradient_color(step, total)
    draw_tree(root, title=title)


if __name__ == "__main__":
    data = [15, 3, 22, 8, 17, 5, 11, 1, 9]

    root = build_heap_tree(data)
    visualize_traversal(root, dfs, "DFS — обхід у глибину (стек)")

    root = build_heap_tree(data)
    visualize_traversal(root, bfs, "BFS — обхід у ширину (черга)")
