class Logger:

    def __init__(self):
        # list of the times with the processes running in that time
        self.runtime = [[0], [0]]
        self.arrival = [[], []]
        self.waiting = [[], []]

    def log_runtime(self, process, clock, starting=True):
        if clock.time is 0:
            self.runtime[1].pop()
        self.runtime[0].append(clock.time)
        if starting:
            self.runtime[1].append(process.process_number)
        else:
            self.runtime[1].append(0)

