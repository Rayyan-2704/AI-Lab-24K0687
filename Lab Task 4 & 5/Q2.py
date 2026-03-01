def dls(graph, current, goal, depth_limit, visited_nodes, current_path):
    visited_nodes.append(current)
    current_path.append(current)

    if current == goal:
        return True

    if depth_limit == 0:
        current_path.pop()
        return False

    for neighbor in graph[current]:
        found = dls(graph, neighbor, goal, depth_limit - 1, visited_nodes, current_path)
        if found:
            return True

    current_path.pop()
    return False


def run_dls(graph, start_node, goal_node, limit):

    visited = []
    path = []

    print(f"\n------------ Depth-Limited Search with depth = {limit} ------------")
    result = dls(graph, start_node, goal_node, limit, visited, path)
    print("Visited Nodes:", visited)

    if result:
        print("Goal found!")
        print(f"Path: {path}")
    else:
        print("Goal not found within depth limit.")


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

    start = 'A'
    goal = 'H'

    run_dls(graph, start, goal, 2)
    run_dls(graph, start, goal, 3)


main()