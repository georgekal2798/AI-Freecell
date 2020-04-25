class TreeNode:
    def __init__(self, parent, base_stacks, foundations, freecells, depth):
        self.parent = parent
        self.base_stacks = base_stacks
        self.foundations = foundations
        self.freecells = freecells
        self.depth = depth
        self.number_of_moves = 0
        self.moves_logger = ''

    def __eq__(self, other):
        return (self.base_stacks == other.base_stacks) and \
               (self.foundations == other.foundations) and \
               (self.freecells == other.freecells)

    def __hash__(self):
        return hash(tuple(self.base_stacks + self.foundations + self.freecells))

    def find_possible_moves(self):
        possible_moves = []

        for i, current_stack in enumerate(self.all_stacks()):
            for j, other_stack in enumerate(self.all_stacks()):
                if current_stack != other_stack:
                    if other_stack.can_move(current_stack):
                        possible_moves.append((i, j))

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
