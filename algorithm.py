import file_manager


class Algorithm:
    def __init__(self):
        pass

    def run(self):
        # TODO: replace with pass. implement each algorithm separately
        # Test
        file_manager.log_move('This is a test move, but it counts')

        self.stop()

    def stop(self):
        file_manager.write_file()
