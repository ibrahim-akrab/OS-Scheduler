class Process:

    def __init__(self, process_number, arrival_time, brust_time, priority):
        self.process_number = process_number
        self.arrival_time = arrival_time
        self.burst_time = brust_time
        self.priority = priority
        self.started_running_time = 0

    def __repr__(self):
        return repr((self.process_number, self.arrival_time, self.burst_time, self.priority))

    def run(self, time):
            self.started_running_time = time

    def stop(self, time):
        runtime = time - self.started_running_time
        self.burst_time = 0 if abs(runtime - self.burst_time) < 0.0000000000001 else self.burst_time - runtime

    def remaining_time(self, time):
        return self.burst_time - (time - self.started_running_time)

    def get_arrival_time(self):
        return self.arrival_time

    def get_process_number(self):
        return self.process_number
