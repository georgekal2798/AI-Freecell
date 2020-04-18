import data
from algorithm import Algorithm
from foundation import Foundation
from freecell import Freecell


class Breadth(Algorithm):
    def __init__(self):
        super().__init__()

    def run(self):
        # Test
        data.foundations = [Foundation() for i in range(data.F)]
        data.freecels = [Freecell() for i in range(data.F)]

        all_stacks = data.base_stacks + data.foundations + data.freecels
        for current_stack in all_stacks:
            for other_stack in all_stacks:
                if current_stack != other_stack:
                    if other_stack.can_move(current_stack):
                        other_stack.move(current_stack)

        self.stop()
