from collections import deque
from itertools import islice

from algorithms.algorithm import Algorithm


class AStar(Algorithm):
    def __init__(self):
        super().__init__()

    def add_to_frontier(self, node):
        node.calculate_heuristic(node.depth)

        # Find insertion index in the frontier
        n = 0
        for n, frontier_node in enumerate(self.frontier):
            if frontier_node.heuristic_value > node.heuristic_value:
                break

        self.frontier.insert(n, node)
