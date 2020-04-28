from algorithms.algorithm import Algorithm


class Depth(Algorithm):
    def __init__(self):
        super().__init__()

    def add_to_frontier(self, node):
        self.frontier.append(node)
