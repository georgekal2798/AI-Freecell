import data
from card import Suit, Card
from solitaire_stack import SolitaireStack


def log_move(message):
    data.number_of_moves += 1
    data.moves_logger += '\n' + message


def write_file():
    # Replace placeholder with number of moves
    data.moves_logger = data.moves_logger.replace('%NUM_OF_MOVES%', str(data.number_of_moves))

    file = open(data.output_path, 'w')
    file.write(data.moves_logger)

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
        data.base_stacks.append(SolitaireStack())
        for card_str in line.split(' '):
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
    data.print_stacks()
