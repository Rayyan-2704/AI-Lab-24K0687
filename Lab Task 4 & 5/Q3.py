def dls(graph, current, goal, depth_limit, path, visited):
    visited.append(current)
    path.append(current)

    if current == goal:
        return True

    if depth_limit == 0:
        path.pop()
        return False

    for neighbor in graph[current]:
        if dls(graph, neighbor, goal, depth_limit - 1, path, visited):
            return True

    path.pop()
    return False


def iterative_deepening_search(graph, start, goal, max_depth):
    for depth in range(max_depth + 1):

        print(f"\nSearching at depth level: {depth}")
        visited_nodes = []
        current_path = []

        found = dls(graph, start, goal, depth, current_path, visited_nodes)
        print("Visited Nodes:", visited_nodes)

        if found:
            print(f"Goal found at depth {depth}")
            print(f"Final Path: {current_path}")
            return

    print("\nGoal not found within max depth.")


def main():
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': ['G'],
        'E': [],
        'F': ['H'],
        'G': [],
        'H': []
    }

    start_node = 'A'
    goal_node = 'G'

    iterative_deepening_search(graph, start_node, goal_node, 5)


main()