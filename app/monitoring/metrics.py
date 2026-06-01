import time


class Metrics:

    def __init__(self):
        self.start_time = time.time()

    def latency(self):

        return (
            time.time()
            - self.start_time
        )