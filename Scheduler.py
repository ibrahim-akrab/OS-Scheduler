from ProcessManager import  ProcessManager
from Clock import Clock
from operator import itemgetter, attrgetter
from bisect import insort
from enum import Enum
from Logger import Logger


class Scheduler:

    def __init__(self, context_switching, time_quantum=0):
        self.context_switching = context_switching
        self.state = None
        self.clock = None
        self.logger = Logger()
        # the processes that are currently running or waiting in queue
        self.processes = []
        self.running_process = None
        self.time_quantum = time_quantum

    def process_arrived(self, processes):
        processes.sort(key=attrgetter('process_number'))
        for process in processes:
            # print(self.clock, "arrived", process)
            self.processes.append(process)
            self.logger.arrived(process, self.clock, arriving=True)

    def attach_clock(self, clock):
        self.clock = clock
        self.clock.attach_scheduler(self)

    def notify(self):
        # if it was running before being notified
        if self.state is SchedulerState.running:
            # start context switching to save process data
            self.state = SchedulerState.context_switching_dump
            self.stop_process()
            self.logger.log_runtime(self.running_process, self.clock, starting=False)
            # print(self.clock, "finished running", self.running_process)
            self.running_process = None
            # print(self.clock, "started context switching")
            self.clock.notify_scheduler(self.clock.time + self.context_switching)
        # else if it was saving process data doing context switching
        elif self.state is SchedulerState.context_switching_dump:
            # start context switching to get new process data
            self.state = SchedulerState.context_switching_prepare
            self.sort_processes()
            self.clock.notify_scheduler(self.clock.time + self.context_switching)
        # else if it was done preparing data for the new process
        elif self.state is SchedulerState.context_switching_prepare:
            self.state = None
            # run the first process
            # print(self.clock, "finished context switching")
            if len(self.processes) is not 0:
                self.run()

    # defines what you want to happen when you stop process execution
    def stop_process(self):
        pass

    # defines how you prioritize processes
    def sort_processes(self):
        pass

    def run(self):
        process = self.processes[0]
        self.logger.log_runtime(process, self.clock, starting=True)
        # print(self.clock, "started running", process)
        self.state = SchedulerState.running
        self.running_process = process
        process.run(self.clock.time)


class SchedulerState(Enum):
    running, context_switching_dump, context_switching_prepare = range(3)
