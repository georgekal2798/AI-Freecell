import sys

import data
import file_manager
from algorithm import Algorithm


def main():
    # algorithm, input_path, data.output_path = sys.argv[:3]
    # Debugging
    algorithm_str, input_path, data.output_path = ['breadth', 'test1.txt', 'out.txt']

    file_manager.read_file(input_path)

    switch = {
        'breadth': Algorithm(),
        'width': Algorithm(),
        'best': Algorithm(),
        'astar': Algorithm()
    }
    algorithm = switch.get(algorithm_str, None)
    algorithm.run()


if __name__ == '__main__':
    main()
