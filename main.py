import sys

import data
import file_manager
from algorithm import Method, Algorithm


# from astar import AStar
# from best import Best
# from breadth import Breadth
# from depth import Depth


def main():
    # algorithm, input_path, data.output_path = sys.argv[:3]

    # Debugging
    algorithm_str, input_path, data.output_path = ['breadth', 'test2.txt', 'out.txt']

    # sys.setrecursionlimit(3000)

    file_manager.read_file(input_path)

    switch = {
        'breadth': Method.BREADTH,
        'depth': Method.DEPTH,
        'best': Method.BEST,
        'astar': Method.A_STAR
    }
    method = switch.get(algorithm_str, None)
    algorithm = Algorithm()

    if method:
        data.method = method
        algorithm.run()
    else:
        # TODO: Move to error handling module
        print('Wrong algorithm name')


if __name__ == '__main__':
    main()
