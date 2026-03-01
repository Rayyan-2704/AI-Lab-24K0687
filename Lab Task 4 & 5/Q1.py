def grid_to_graph(grid, rows, cols):
    graph = {}
    directions = [(-1,0), (1,0), (0,-1), (0,1)]
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                graph[(r,c)] = []
                
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        if grid[nr][nc] == 1:
                            graph[(r,c)].append((nr,nc))
    
    return graph


def bfs(graph, start, goal):
    visited = []
    queue = []
    parent = {}
    traversal_order = []
    
    queue.append(start)
    visited.append(start)
    parent[start] = None
    
    while len(queue) > 0:
        current = queue.pop(0)
        traversal_order.append(current)

        if current == goal:
            break
        
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.append(neighbor)
                parent[neighbor] = current
                queue.append(neighbor)
    
    return traversal_order, parent


def print_shortest_path(parent, end):
    path = []
    current = end
    
    while current is not None:
        path.append(current)
        current = parent[current]
    
    path.reverse()
    
    print("\n\nShortest Path:")
    for node in path:
        print(node, end=" ")
    print()


def main():
    building = [
        [1, 1, 0, 1],
        [0, 1, 1, 1],
        [1, 1, 0, 1],
        [1, 0, 1, 1]
    ]

    rows = len(building)
    cols = len(building[0])
    start = (0, 0)
    exit = (3, 3)

    graph = grid_to_graph(building, rows, cols)

    traversal, parent = bfs(graph, start, exit)

    print("Traversal Order:")
    for node in traversal:
        print(node, end=" ")

    print_shortest_path(parent, exit)


main()