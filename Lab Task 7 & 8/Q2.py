import math

class Node:
    def __init__(self, value=None):
        self.value = value
        self.children = []
        self.minmax_value = None


class Environment:
    def __init__(self):
        self.computed_nodes = []
        self.pruned_nodes = []

    def alpha_beta(self, node, depth, alpha, beta, maximizing_player = True):
        self.computed_nodes.append(node.value)

        if depth == 0 or not node.children:
            return node.value

        if maximizing_player:
            value = -math.inf
            for i, child in enumerate(node.children):
                value = max(value, self.alpha_beta(child, depth - 1, alpha, beta, False))
                alpha = max(alpha, value)
                if beta <= alpha:
                    for skipped in node.children[i + 1:]:   # siblings not yet visited
                        self.pruned_nodes.append(skipped.value)
                    break
        else:
            value = math.inf
            for i, child in enumerate(node.children):
                value = min(value, self.alpha_beta(child, depth - 1, alpha, beta, True))
                beta = min(beta, value)
                if beta <= alpha:
                    for skipped in node.children[i + 1:]:
                        self.pruned_nodes.append(skipped.value)
                    break

        node.minmax_value = value
        return value


def main():
    root = Node('Root')
    n1 = Node('N1')
    n2 = Node('N2')
    n3 = Node('N3')
    n4 = Node('N4')
    n5 = Node('N5')
    n6 = Node('N6')

    root.children = [n1, n2]
    n1.children = [n3, n4]
    n2.children = [n5, n6]
    n3.children = [Node(4), Node(7)]
    n4.children = [Node(2), Node(5)]
    n5.children = [Node(1), Node(8)]
    n6.children = [Node(3), Node(6)]

    env = Environment()
    env.alpha_beta(root, 3, -math.inf, math.inf, True)

    print("-------------- Minimax Values --------------")
    print(f"Root: {root.minmax_value}")
    print(f"N1: {n1.minmax_value}")
    print(f"N2: {n2.minmax_value}")
    print(f"N3: {n3.minmax_value}")
    print(f"N4: {n4.minmax_value}")
    print(f"N5: {n5.minmax_value}")
    print(f"N6: {n6.minmax_value}")
    print(f"\nVisited Nodes: {env.computed_nodes}")
    print(f"Pruned Nodes: {env.pruned_nodes}")

main()
# Alpha-Beta pruning boosts performance by skipping branches that do not affect the final choice.
# By skipping nodes that are inferior to previously explored options, it prevents unnecessary recursion.