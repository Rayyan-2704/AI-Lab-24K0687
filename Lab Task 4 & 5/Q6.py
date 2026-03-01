import random

graph = {
    'A': {'B': 4, 'C': 3},
    'B': {'E': 12, 'F': 5},
    'C': {'D': 7, 'E': 10},
    'D': {'E': 2},
    'E': {'G': 5},
    'F': {'G': 16},
    'G': {}
}

heuristic = {
    'A': 14, 'B': 12, 'C': 11,
    'D': 6, 'E': 4, 'F': 11, 'G': 0
}


def reconstruct_path(parent, goal):
    path = []
    node = goal
    while node:
        path.append(node)
        node = parent[node]
    path.reverse()
    return path


def a_star(start, goal):
    open_list = [start]
    closed_list = []

    g_cost = {node: float('inf') for node in graph}
    f_cost = {node: float('inf') for node in graph}
    parent = {}

    g_cost[start] = 0
    f_cost[start] = heuristic[start]
    parent[start] = None

    while open_list:
        open_list.sort(key=lambda node: f_cost[node])
        current = open_list.pop(0)

        print(f"Visiting: {current}")

        if current == goal:
            print("Goal reached!")
            return reconstruct_path(parent, goal), g_cost[goal]

        closed_list.append(current)

        if random.randint(1, 4) == 1:
            change_random_edge()

        for neighbor in graph[current]:
            if neighbor in closed_list:
                continue

            tentative_g = g_cost[current] + graph[current][neighbor]

            if tentative_g < g_cost[neighbor]:
                parent[neighbor] = current
                g_cost[neighbor] = tentative_g
                f_cost[neighbor] = g_cost[neighbor] + heuristic[neighbor]

                if neighbor not in open_list:
                    open_list.append(neighbor)

    return None, None


def change_random_edge():
    nodes = list(graph.keys())
    from_node = random.choice(nodes)

    if graph[from_node]:
        to_node = random.choice(list(graph[from_node].keys()))
        old_cost = graph[from_node][to_node]

        change = random.randint(-5, 5)
        new_cost = max(1, old_cost + change)

        graph[from_node][to_node] = new_cost

        print("\nEdge cost changed!")
        print(f"{from_node} → {to_node}: {old_cost} → {new_cost}\n")


def main():
    start = 'A'
    goal = 'G'

    print("------------- Starting Dynamic A* Search -------------\n")

    path, cost = a_star(start, goal)

    print("\nFinal Result")
    print(f"Optimal Path: {path}")
    print(f"Total Cost: {cost}")


main()