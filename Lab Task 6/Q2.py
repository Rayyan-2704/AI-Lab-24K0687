import heapq

def heuristic(x):
    return abs(20 - x)


def beam_search(start, goal, width = 2):
    beam = [(heuristic(start), [start])]
    level = 0

    while beam:
        print(f"Level {level}")
        candidates = []

        for h, path in beam:
            x = path[-1]
            print(f"Number explored: {x}")

            if x == goal:
                print("\nGoal has been reached!")
                return path

            for neighbour in [x + 2, x + 3, x * 2]:
                new_path = path + [neighbour]
                candidates.append((heuristic(neighbour), new_path))

        beam = heapq.nsmallest(width, candidates, key=lambda x: x[0])

        print("Beam states:")
        for h, p in beam:
            print(f"{p[-1]} heuristic: {h}")

        print("-----------------------------\n")
        level += 1


def main():
    result = beam_search(1, 20)
    print("Final path:", result)


main()