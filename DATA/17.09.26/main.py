import json
import sys

sys.setrecursionlimit(200050)


# --- 1. Завантаження графа ---
def load_graph_json(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)


# --- 2. Перевірка зв'язності та компоненти (DFS) ---
def get_connected_components(graph):
    visited = set()
    components = []

    for node in graph:
        if node not in visited:
            component = []
            stack = [node]
            visited.add(node)
            while stack:
                curr = stack.pop()
                component.append(curr)
                for neighbor in graph.get(curr, []):
                    if neighbor not in visited:
                        visited.add(neighbor)
                        stack.append(neighbor)
            components.append(component)
    return components


def check_connectivity(graph):
    comps = get_connected_components(graph)
    if len(comps) == 1:
        print("Граф зв'язний.")
    else:
        print(f"Граф НЕ зв'язний. Знайдено компонент: {len(comps)}")
        for i, comp in enumerate(comps, 1):
            print(f"  Компонента {i}: {comp}")


# --- 3. Пошук циклів за допомогою DFS ---
def find_cycle(graph):
    visited = set()
    rec_stack = set()
    parent = {}

    def dfs(node, p):
        visited.add(node)
        rec_stack.add(node)
        parent[node] = p

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                cycle = dfs(neighbor, node)
                if cycle:
                    return cycle
            elif neighbor in rec_stack:
                # Відновлюємо цикл
                cycle = [neighbor]
                curr = node
                while curr != neighbor:
                    cycle.append(curr)
                    curr = parent[curr]
                cycle.append(neighbor)
                return list(reversed(cycle))

        rec_stack.remove(node)
        return None

    for node in graph:
        if node not in visited:
            res = dfs(node, None)
            if res:
                return res
    return None


def detect_cycles(graph):
    cycle = find_cycle(graph)
    if cycle:
        print("Знайдено цикл:", " -> ".join(map(str, cycle)))
    else:
        print("Циклів немає.")


# --- 4. Алгоритм Тар'яна для компонент сильної зв'язності (SCC) ---
def tarjan_scc(graph):
    index = 0
    stack = []
    indices = {}
    lowlink = {}
    on_stack = set()
    sccs = []

    def strongconnect(v):
        nonlocal index
        indices[v] = index
        lowlink[v] = index
        index += 1
        stack.append(v)
        on_stack.add(v)

        for w in graph.get(v, []):
            if w not in indices:
                strongconnect(w)
                lowlink[v] = min(lowlink[v], lowlink[w])
            elif w in on_stack:
                lowlink[v] = min(lowlink[v], indices[w])

        if lowlink[v] == indices[v]:
            scc = []
            while True:
                w = stack.pop()
                on_stack.remove(w)
                scc.append(w)
                if w == v:
                    break
            sccs.append(scc)

    for node in graph:
        if node not in indices:
            strongconnect(node)

    return sccs


def find_scc(graph):
    sccs = tarjan_scc(graph)
    print(f"Знайдено компонент сильної зв'язності (SCC): {len(sccs)}")
    for i, scc in enumerate(sccs, 1):
        print(f"  SCC {i}: {scc}")


# --- 5. Консольний інтерфейс ---
def main():
    if len(sys.argv) < 2:
        print("Використання: python script.py <path_to_graph.json>")
        return

    graph = load_graph_json(sys.argv[1])

    while True:
        print("\n=== Меню ===")
        print("1. Перевірка зв'язності")
        print("2. Пошук циклів")
        print("3. Визначення SCC (Сильної зв'язності)")
        print("0. Вихід")

        choice = input("Вибери опцію: ").strip()
        if choice == '1':
            check_connectivity(graph)
        elif choice == '2':
            detect_cycles(graph)
        elif choice == '3':
            find_scc(graph)
        elif choice == '0':
            break
        else:
            print("Хибний вибір.")


if __name__ == '__main__':
    main()