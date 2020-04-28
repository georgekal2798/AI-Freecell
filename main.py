import sys

import data
import file_manager


from algorithms.astar import AStar
from algorithms.best import Best
from algorithms.breadth import Breadth
from algorithms.depth import Depth


def print_report():
    switch = {
        'Breadth': Breadth(),
        'Depth': Depth(),
        'Best': Best(),
        'AStar': AStar()
    }

    for key, algorithm in switch.items():
        print('Running: ' + key)
        data.output_path = 'output/out_' + key + '.txt'
        time, moves, checked = algorithm.run()
        if time < data.timeout_threshold:
            print('Time: ' + str(time))
        print('Moves: ' + str(moves))
        print('States checked: ' + str(checked) + '\n')


def main():
    if len(sys.argv) == 1:
        # For when main is called from the IDE
        algorithm_str, input_path, data.output_path = ['best', 'input/test4.txt', 'output/out.txt']
    elif len(sys.argv) == 3:
        algorithm_str, input_path = sys.argv[1:3]
    elif len(sys.argv) == 4:
        algorithm_str, input_path, data.output_path = sys.argv[1:4]
    else:
        print('Wrong number of arguments')

    file_manager.read_file(input_path)

    switch = {
        'breadth': Breadth(),
        'depth': Depth(),
        'best': Best(),
        'astar': AStar(),
        'report': 'report'
    }
    algorithm = switch.get(algorithm_str, None)

    if algorithm:
        if algorithm == 'report':
            print_report()
        else:
            time, moves, checked = algorithm.run()
            if time < data.timeout_threshold:
                print('Time: ' + str(time))
            print('Moves: ' + str(moves))
            print('States checked: ' + str(checked) + '\n')

        print('Solutions can be found in folder \'output\'')
    else:
        # TODO: Move to error handling module
        print('Wrong algorithm name')


if __name__ == '__main__':
    main()
