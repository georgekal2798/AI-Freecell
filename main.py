import sys

import data
import file_manager


from astar import AStar
from best import Best
from breadth import Breadth
from depth import Depth


class Report:
    def run(self):
        switch = {
            'BFS': Breadth(),
            'DFS': Depth(),
            'Best': Best(),
            'A*': AStar()
        }

        for key, algorithm in switch.items():
            print('Running: ' + key)
            time, moves = algorithm.run()
            if time < data.timeout_threshold:
                print('Time: ' + str(time))
            print('Moves: ' + str(moves))


def main():
    # algorithm, input_path, data.output_path = sys.argv[:3]

    # Debugging
    algorithm_str, input_path, data.output_path = ['best', 'test6.txt', 'out.txt']

    file_manager.read_file(input_path)

    switch = {
        'breadth': Breadth(),
        'depth': Depth(),
        'best': Best(),
        'astar': AStar(),
        'report': Report()
    }
    algorithm = switch.get(algorithm_str, None)

    if algorithm:
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
