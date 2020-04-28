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
        self.max_node = None
        self.states_checked = 1

    def run(self):
        # Starting timer
        t0 = time.time()
        print('Timeout is set to ' + str(data.timeout_threshold) + ' seconds')

        root_node = TreeNode(
            data.base_stacks
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
                print('Timeout. Node with the maximum depth:')
                solution = self.max_node
                break

            current_node = self.frontier.popleft()

            if current_node.is_solution():
                solution = current_node
                break

            self.find_children(current_node)

        timer = time.time() - t0
        self.stop(solution)
        return timer, solution.depth, self.states_checked

    def find_children(self, node):
        # possible_moves is a set of tuples. The first value of each tuple is the index of the source stack and the
        # second value is the index of the target stack. Indices reference to the list returned by
        # tree_node.all_stacks()
        possible_moves = node.find_possible_moves()

        for move in possible_moves:
            new_node = TreeNode(
                copy.deepcopy(node.base_stacks)
                , copy.deepcopy(node.foundations)
                , copy.deepcopy(node.freecells)
                , node.depth + 1
                , node.moves_logger
            )

            if new_node.depth > self.max_depth:
                self.max_node = new_node
                self.max_depth = new_node.depth
                # Debugging. Used as a kind of progress indicator
                # print("Current maximum depth: %d" % self.max_depth)

            other_stack = new_node.all_stacks()[move[1]]
            current_stack = new_node.all_stacks()[move[0]]

            move_message = other_stack.move(current_stack)
            new_node.log_move(move_message)

            if new_node not in self.visited:
                self.add_to_frontier(new_node)
                self.visited.add(new_node)

            # Deletes node from memory (according to stackoverflow; did not fully test it)
            new_node = None

        return None

    def add_to_frontier(self, node):
        pass

    def stop(self, solution):
        # data.print_stacks(solution)
        file_manager.write_file(solution)
