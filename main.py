import sys

import data
import file_manager


from astar import AStar
from best import Best
from breadth import Breadth
from depth import Depth


def main():
    # algorithm, input_path, data.output_path = sys.argv[:3]

    # Debugging
    algorithm_str, input_path, data.output_path = ['best', 'test1.txt', 'out.txt']

    file_manager.read_file(input_path)

    switch = {
        'breadth': Breadth(),
        'depth': Depth(),
        'best': Best(),
        'astar': AStar()
    }
    algorithm = switch.get(algorithm_str, None)

    if algorithm:
        algorithm.run()
    else:
        # TODO: Move to error handling module
        print('Wrong algorithm name')


if __name__ == '__main__':
    main()
