import data


class TreeNode:
    def __init__(self, parent, base_stacks, foundations, freecells, depth):
        self.parent = parent
        self.base_stacks = base_stacks
        self.foundations = foundations
        self.freecells = freecells
        self.depth = depth
        self.heuristic_value = 0
        self.number_of_moves = 0
        self.moves_logger = ''

    def __eq__(self, other):
        return (self.base_stacks == other.base_stacks) and \
               (self.foundations == other.foundations) and \
               (self.freecells == other.freecells)

    def __hash__(self):
        return hash(tuple(self.base_stacks + self.foundations + self.freecells))

    def find_possible_moves(self):
        # possible_moves is a set of tuples. The first value of each tuple is the index of the source stack and the
        # second value is the index of the target stack. Indices reference to the list returned by self.all_stacks()
        possible_moves = set()

        # self.all_stacks() returns a list of SolitaireStack objects that contains:
        # positions 0 - S-1: Base stacks
        # positions S - S+F-1: Foundations
        # positions S+F - S+F+C-1: Freecells
        #
        # Values of S, F, C are defined in data.py

        freecells_range = range(data.S + data.F, data.S + data.F + data.C)

        for i, current_stack in enumerate(self.all_stacks()):
            i_to_freecell = False
            for j, other_stack in enumerate(self.all_stacks()):
                if current_stack != other_stack and other_stack.can_move(current_stack):
                    if i_to_freecell and j in freecells_range:
                        continue
                    possible_moves.add((i, j))
                    if j in freecells_range:
                        i_to_freecell = True

        # Variable i_to_freecell is used to filter possible_moves: if a card from stack i is already set to move to a
        # freecell, a move from i to another freecell will not be added to possible_moves again

        return possible_moves

    # def has_loop(self, node):
    #     if self == node:
    #         # print('equal')
    #         return True
    #     elif self.parent:
    #         # print('not equal')
    #         self.parent.has_loop(node)
    #     else:
    #         # print('reached root. no loop')
    #         return False

    def all_stacks(self):
        return self.base_stacks + self.foundations + self.freecells

    def log_move(self, message):
        self.number_of_moves += 1
        self.moves_logger += '\n' + message

    # def equals(self, node):
    #     return (self.base_stacks == node.base_stacks) and \
    #            (self.foundations == node.foundations) and \
    #            (self.freecells == node.freecells)

    def calculate_heuristic(self):
        # Heuristic value is calculated by how many cards are left to go to the foundations to win the game
        value = 4 * data.N
        for f in self.foundations:
            value -= len(f.cards)

        return value
