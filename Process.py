class Process:

    def __init__(self, process_number, arrival_time, brust_time, priority):
        self.process_number = process_number
        self.arrival_time = arrival_time
        self.burst_time = brust_time
        self.priority = priority

    def __repr__(self):
        return repr((self.process_number, self.arrival_time, self.burst_time, self.priority))

    def run(self, runtime):
        self.burst_time = 0 if runtime > self.burst_time else self.burst_time - runtime

    def get_remaining_time(self):
        return self.burst_time

    def get_arrival_time(self):
        return self.arrival_time

    def get_process_number(self):
        return self.process_number
