from ProcessManager import  ProcessManager
from Clock import Clock
from operator import itemgetter, attrgetter
from bisect import insort
from enum import Enum


class Scheduler:

    def __init__(self, context_switching):
        self.context_switching = context_switching
        self.state = None
        self.clock = None
        # the processes that are currently running or waiting in queue
        self.processes = []

    def process_arrived(self, process):
        pass

    def attach_clock(self, clock):
        self.clock = clock
        self.clock.scheduler = self

    def notify(self):
        pass

    def run(self):
        pass


class SchedulerState(Enum):
    running, context_switching = range(2)
