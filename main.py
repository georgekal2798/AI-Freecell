import sys

import data
import file_manager


from algorithms.astar import AStar
from algorithms.best import Best
from algorithms.breadth import Breadth
from algorithms.depth import Depth


def print_report():
    switch = {
        'BFS': Breadth(),
        'DFS': Depth(),
        'Best': Best(),
        'A*': AStar()
    }

    for key, algorithm in switch.items():
        print('Running: ' + key)
        time, moves, checked = algorithm.run()
        if time < data.timeout_threshold:
            print('Time: ' + str(time))
        print('Moves: ' + str(moves))
        print('States checked: ' + str(checked))


def main():
    if len(sys.argv) == 1:
        # Debugging. For when main is called from the IDE
        algorithm_str, input_path, data.output_path = ['best', 'input/test1.txt', 'out.txt']
    else:
        algorithm_str, input_path, data.output_path = sys.argv[1:4]

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
            print('States checked: ' + str(checked))
    else:
        # TODO: Move to error handling module
        print('Wrong algorithm name')


if __name__ == '__main__':
    main()
