from ProcessManager import  ProcessManager
from Clock import Clock
from operator import itemgetter, attrgetter
from bisect import insort
from enum import Enum
from Logger import Logger


class Scheduler:

    def __init__(self, context_switching):
        self.context_switching = context_switching
        self.state = None
        self.clock = None
        self.logger = Logger()
        # the processes that are currently running or waiting in queue
        self.processes = []
        self.running_process = None

    def process_arrived(self, processes):
        for process in processes:
            # print(self.clock, "arrived", process)
            self.processes.append(process)
            self.logger.arrived(processes, self.clock, arriving=True)

    def attach_clock(self, clock):
        self.clock = clock
        self.clock.attach_scheduler(self)

    def notify(self):
        pass

    def run(self):
        process = self.processes[0]
        self.logger.log_runtime(process, self.clock, starting=True)
        # print(self.clock, "started running", process)
        self.state = SchedulerState.running
        self.running_process = process
        process.run(self.clock.time)


class SchedulerState(Enum):
    running, context_switching = range(2)
