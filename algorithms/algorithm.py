import copy
from collections import deque
import time

import data
import file_manager
from model.card import Suit
from model.foundation import Foundation
from model.freecell import Freecell
from tree_node import TreeNode


class Algorithm:
    def __init__(self):
        self.frontier = deque()
        self.visited = set()
        self.max_depth = 0
        self.best_node = None
        self.states_checked = 1

    def run(self):
        t0 = time.time()  # Starting timer
        print('Timeout is set to ' + str(data.timeout_threshold) + ' seconds')

        root_node = TreeNode(
            None
            , data.base_stacks
            , deque([Foundation(Suit(i + 1)) for i in range(data.F)])
            , deque([Freecell() for i in range(data.C)])
            , 0
        )

        self.frontier.append(root_node)
        self.visited.add(root_node)

        solution = None
        while self.frontier:
            self.states_checked += 1
            # Check timer before continuing
            timer = time.time() - t0
            if timer > data.timeout_threshold:
                print('Timeout. Node with the greatest depth:')
                solution = self.best_node
                break

            current_node = self.frontier.popleft()

            if self.is_solution(current_node):
                solution = current_node
                break

            self.find_children(current_node)

        timer = time.time() - t0
        self.stop(solution)
        return timer, solution.depth, self.states_checked

    def find_children(self, node):
        possible_moves = node.find_possible_moves()

        for move in possible_moves:
            new_node = TreeNode(
                node
                , copy.deepcopy(node.base_stacks)
                , copy.deepcopy(node.foundations)
                , copy.deepcopy(node.freecells)
                , node.depth + 1
                , node.moves_logger
            )

            # Debugging. Used as a kind of progress indicator
            if new_node.depth > self.max_depth:
                self.best_node = new_node
                self.max_depth = new_node.depth
                print("Current maximum depth: %d" % self.max_depth)

            other_stack = new_node.all_stacks()[move[1]]
            current_stack = new_node.all_stacks()[move[0]]

            move_message = other_stack.move(current_stack)
            new_node.log_move(move_message)

            if new_node not in self.visited:
                self.add_to_frontier(new_node)
                self.visited.add(new_node)
            new_node = None

        return None

    def add_to_frontier(self, node):
        pass

    def is_solution(self, node):
        for f in node.foundations:
            if f.is_empty() or (f.top().number != data.N):
                return False
        return True

    def stop(self, solution):
        # data.print_stacks(solution)
        file_manager.write_file(solution)
