import data
from model.base_stack import BaseStack
from model.card import Suit, Card


def write_file(node):
    file = open(data.output_path, 'w')

    if node:
        # Replace placeholder with number of moves
        node.moves_logger = node.moves_logger.replace('%NUM_OF_MOVES%', str(node.depth))
        file.write(node.moves_logger)
    else:
        file.write('0')

    file.close()


def read_file(input_path):
    # Initialize the log string with moves counter placeholder
    data.moves_logger = '%NUM_OF_MOVES%'

    # Map used to match characters with Suit values
    switch = {
        'S': Suit.SPADES,
        'D': Suit.DIAMONDS,
        'H': Suit.HEARTS,
        'C': Suit.CLUBS
    }

    file = open(input_path, 'r')

    for s, line in enumerate(file):
        # Initiate new stack before adding cards for each line
        data.base_stacks.append(BaseStack())
        for card_str in line.split(' '):
            # Ignores spaces at the end of each line --> card_str == None
            if not card_str:
                continue

            suit_str = card_str[0]  # First character is the suit
            number_str = card_str[1:]  # The rest digits is the number

            # Turn string to values for number and suit
            suit = switch.get(suit_str, None)
            number = int(number_str)

            card = Card(number, suit)

            # Add new cards to each stack
            data.base_stacks[s].add(card)

    file.close()

    # Debugging
    # data.print_stacks()
