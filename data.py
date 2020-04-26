from collections import deque
from tree_node import TreeNode

N = 13  # Number of cards per suit
S = 8  # Number of base stacks
C = 4  # Number of freecells
F = 4  # Number of foundations

output_path = 'out.txt'

timeout_threshold = 3

base_stacks = deque()


def print_stacks(node):
    def print_stack(n, g):
        print(n)
        for stack in g:
            temp = ''
            for card in stack.cards:
                temp += '{:4}'.format(card.name())
            print(temp)

    if node:
        stack_map = {
            'Base Stacks': node.base_stacks,
            'Foundations': node.foundations,
            'Freecells': node.freecells
        }

        for name, stack_group in stack_map.items():
            print_stack(name, stack_group)
    else:
        print('No solution')
