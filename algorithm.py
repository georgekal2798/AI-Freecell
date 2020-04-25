import copy
from enum import Enum

import data
import file_manager
from base_stack import BaseStack
from foundation import Foundation
from freecell import Freecell
from tree_node import TreeNode


class Method(Enum):
    BREADTH = 0
    DEPTH = 1
    BEST = 2
    A_STAR = 3


class Algorithm:
    def __init__(self):
        self.frontier = None
        self.visited = None
        # Testing
        self.max_depth = 0

    def run(self):
        root_node = TreeNode(
            None
            , data.base_stacks
            , [Foundation() for i in range(data.F)]
            , [Freecell() for i in range(data.C)]
            , 0
        )

        self.frontier = [root_node]
        self.visited = {root_node}

        solution = None
        while self.frontier:
            current_node = self.frontier.pop(0)

            if self.is_solution(current_node):
                solution = current_node
                break

            self.find_children(current_node)

        self.stop(solution)

    def find_children(self, node):
        possible_moves = node.find_possible_moves()

        for move in possible_moves:
            new_node = TreeNode(
                node
                , copy.deepcopy(node.base_stacks)
                , copy.deepcopy(node.foundations)
                , copy.deepcopy(node.freecells)
                , node.depth + 1
            )

            # Testing
            if new_node.depth > self.max_depth:
                self.max_depth = new_node.depth
                print(self.max_depth)

            other_stack = new_node.all_stacks()[move[1]]
            current_stack = new_node.all_stacks()[move[0]]

            move_message = other_stack.move(current_stack)
            node.log_move(move_message)

            if new_node in self.visited:
                new_node = None
            else:
                self.frontier.append(new_node)
                self.visited.add(new_node)

        return None

    def is_solution(self, node):
        for f in node.foundations:
            if f.is_empty() or (f.top().number != data.N):
                return False
        return True

    def stop(self, node):
        data.print_stacks(node)
        file_manager.write_file(node)
