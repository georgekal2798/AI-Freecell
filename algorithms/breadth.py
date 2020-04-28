from algorithms.algorithm import Algorithm


class Breadth(Algorithm):
    def __init__(self):
        super().__init__()

    def add_to_frontier(self, node):
        self.frontier.appendleft(node)
