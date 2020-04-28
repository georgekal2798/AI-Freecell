import sys

import data
import file_manager


from algorithms.astar import AStar
from algorithms.best import Best
from algorithms.breadth import Breadth
from algorithms.depth import Depth


def main():
    if len(sys.argv) == 1:
        # For when main is called from the IDE or no arguments are selected
        algorithm_str, input_path, data.output_path = ['best', 'input/medium1.txt', 'output/out.txt']
        print('Running with default arguments: {}, {}, {}'.format(algorithm_str, input_path, data.output_path))
    elif len(sys.argv) == 4:
        algorithm_str, input_path, data.output_path = sys.argv[1:4]
    else:
        print('Wrong number of arguments')
        sys.exit()

    file_manager.read_file(input_path)

    switch = {
        'breadth': Breadth(),
        'depth': Depth(),
        'best': Best(),
        'astar': AStar()
    }
    algorithm = switch.get(algorithm_str, None)

    if algorithm:
        time, moves, checked = algorithm.run()
        if time < data.timeout_threshold:
            print('Time: ' + str(time))
        print('Moves: ' + str(moves))
        print('States checked: ' + str(checked) + '\n')

        print('Solutions can be found in folder \'output\'')
    else:
        print('Wrong algorithm name')


if __name__ == '__main__':
    main()
