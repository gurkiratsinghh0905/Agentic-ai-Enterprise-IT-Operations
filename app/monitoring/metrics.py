import time


class Metrics:
    """Tracks execution timing for workflow performance measurement."""

    def __init__(self):
        self.start_time = time.time()

    def latency(self) -> float:
        """Return elapsed time in seconds since initialization."""
        return round(time.time() - self.start_time, 2)
