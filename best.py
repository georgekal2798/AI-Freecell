from collections import deque
from itertools import islice

from algorithm import Algorithm


class Best(Algorithm):
    def __init__(self):
        super().__init__()

    def add_to_frontier(self, node):
        node.calculate_heuristic()

        # Find insertion index in the frontier
        n = 0
        for n, frontier_node in enumerate(self.frontier):
            if frontier_node.heuristic_value > node.heuristic_value:
                break

        # Slice frontier in order to insert new node in between
        frontier_slice1 = list(islice(self.frontier, None, n))
        frontier_slice2 = list(islice(self.frontier, n, None))

        temp = frontier_slice1 + [node] + frontier_slice2

        self.frontier = deque(temp)
