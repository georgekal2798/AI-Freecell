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
    print('Base stacks')
    for stack in base_stacks:
        temp = ''
        for card in stack.cards:
            temp += '{:4}'.format(card.name())
        print(temp)
