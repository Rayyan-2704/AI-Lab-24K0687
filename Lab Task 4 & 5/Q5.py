heuristic = {
    'S': 7, 'A': 6, 'B': 4, 'C': 5,
    'D': 9, 'E': 8, 'F': 12, 'G': 0,
    'H': 7, 'I': 3, 'J': 0, 'K': 1,
    'L': 2, 'M': 2
}

graph = {
    'S': [('A', 3), ('B', 6), ('C', 5)],
    'A': [('D', 9), ('E', 8)],
    'B': [('F', 12), ('G', 14)],
    'C': [('H', 7)],
    'H': [('I', 5), ('J', 6)],
    'I': [('K', 1), ('L', 10), ('M', 2)],
    'D': [], 'E': [], 'F': [], 'G': [],
    'J': [], 'K': [], 'L': [], 'M': []
}


def best_first_search(start, goal):
    front = [start]
    visited = []
    parent = {start: None}
    cost_so_far = {start: 0}

    while front:
        front.sort(key=lambda node: heuristic[node])
        current = front.pop(0)

        print(f"Visiting: {current}")

        if current == goal:
            print(f"Found goal {goal}")
            break

        visited.append(current)

        for neighbor, cost in graph[current]:
            if neighbor not in visited and neighbor not in front:
                parent[neighbor] = current
                cost_so_far[neighbor] = cost_so_far[current] + cost
                front.append(neighbor)

    if goal not in parent:
        return None, None, None

    path = []
    node = goal
    while node is not None:
        path.append(node)
        node = parent[node]

    path.reverse()
    total_cost = cost_so_far[goal]

    return path, total_cost, goal


def multi_goal_best_first(start, goals):
    remaining_goals = goals[:]
    current_start = start
    full_path = []
    total_cost = 0
    found_goals = []

    print(f"-------------- Searching for goals: {goals} --------------")

    while remaining_goals:
        path, cost, reached_goal = best_first_search(current_start, remaining_goals[0])

        if path is None:
            print("Cannot find remaining goals")
            break

        found_goals.append(reached_goal)

        if full_path:
            path = path[1:]

        full_path.extend(path)
        total_cost += cost

        remaining_goals.remove(reached_goal)

        if remaining_goals:
            print(f"\n-------------- Searching for remaining goals: {remaining_goals} --------------")

        current_start = reached_goal

    return full_path, total_cost, found_goals


def main():
    start_node = 'S'
    goal_nodes = ['C', 'I']

    path, cost, found = multi_goal_best_first(start_node, goal_nodes)

    print("\n-------------- Final Result --------------")
    print(f"Goals found: {found}")
    print(f"Cost to reach goals: {cost}")
    print(f"Path: {path}")


main()