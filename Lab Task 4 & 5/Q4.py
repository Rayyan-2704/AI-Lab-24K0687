def uniform_cost_search(graph, start, goal):
    front = [(0, start)]
    cost_so_far = {start: 0}
    parent = {start: None}

    while front:
        front.sort()
        current_cost, current_node = front.pop(0)
        print("Visiting Node:", current_node, "| Cost so far:", current_cost)

        if current_node == goal:
            break

        for neighbor in graph[current_node]:  
            new_cost = current_cost + graph[current_node][neighbor]

            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                
                cost_so_far[neighbor] = new_cost
                parent[neighbor] = current_node
                front.append((new_cost, neighbor))

    path = []
    node = goal

    if goal not in parent:
        print("\nNo path found.")
        return

    while node is not None:
        path.append(node)
        node = parent[node]

    path.reverse()
    print(f"\nLeast Cost Path: {path}")
    print(f"Total Cost: {cost_so_far[goal]}")


def main():
    graph = {
        'S': {'A': 4, 'B': 2},
        'A': {'C': 5, 'D': 10},
        'B': {'E': 3},
        'C': {'G': 4},
        'D': {'G': 1},
        'E': {'D': 4},
        'G': {}
    }

    start_node = 'S'
    goal_node = 'G'

    uniform_cost_search(graph, start_node, goal_node)


main()