from collections import deque
import time
import random

# Завдання 1: Соціальна мережа та BFS (до 2 кроків)
social_graph = {
    "Антон": ["Богдан", "Віка"],
    "Богдан": ["Антон", "Гліб", "Дмитро"],
    "Віка": ["Антон", "Євген"],
    "Гліб": ["Богдан"],
    "Дмитро": ["Богдан", "Жанна"],
    "Євген": ["Віка"],
    "Жанна": ["Дмитро"]
}


def get_connections_within_2_steps(graph, start_node):
    visited = {start_node}
    queue = deque([(start_node, 0)])
    result = set()

    while queue:
        current, dist = queue.popleft()
        if 0 < dist <= 2:
            result.add(current)

        if dist < 2:
            for neighbor in graph.get(current, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, dist + 1))

    return list(result)


print("Завдання 1 (до 2 кроків від 'Антон'):", get_connections_within_2_steps(social_graph, "Антон"))


# Завдання 2: BFS (найкоротший шлях) проти DFS (будь-який шлях)
def bfs_shortest_path(graph, start, goal):
    queue = deque([[start]])
    visited = {start}
    while queue:
        path = queue.popleft()
        node = path[-1]
        if node == goal:
            return path
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(path + [neighbor])
    return None


def dfs_path(graph, start, goal):
    stack = [[start]]
    visited = {start}
    while stack:
        path = stack.pop()
        node = path[-1]
        if node == goal:
            return path
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(path + [neighbor])
    return None


# Генерація тестового графа
def generate_graph(num_nodes, edge_prob):
    g = {i: [] for i in range(num_nodes)}
    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):
            if random.random() < edge_prob:
                g[i].append(j)
                g[j].append(i)
    return g


test_graph = generate_graph(100, 0.05)

t0 = time.perf_counter();
bfs_shortest_path(test_graph, 0, 99);
t1 = time.perf_counter()
t2 = time.perf_counter();
dfs_path(test_graph, 0, 99);
t3 = time.perf_counter()

print(f"Завдання 2 -> BFS час: {t1 - t0:.6f}s | DFS час: {t3 - t2:.6f}s")
print(
    "Висновок: BFS гарантовано знаходить найкоротший шлях в незваженому графі, тоді як DFS може знайти довший обхід і працює неефективно для пошуку найкоротших шляхів у широких графах.")