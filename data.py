N = 13  # Number of cards per suit
S = 8  # Number of base stacks
C = 4  # Number of freecells
F = 4  # Number of foundations

output_path = 'out.txt'

moves_logger = ''
number_of_moves = 0

base_stacks = []
foundations = []
freecels = []


def print_stacks():
    def print_stack(n, g):
        print(n)
        for stack in g:
            temp = ''
            for card in stack.cards:
                temp += '{:4}'.format(card.name())
            print(temp)

    stack_map = {
        'Base Stacks': base_stacks,
        'Foundations': foundations,
        'Freecells': freecels
    }

    for name, stack_group in stack_map.items():
        print_stack(name, stack_group)
