from Scheduler import Scheduler
from ProcessManager import ProcessManager
from Process import Process
from Clock import Clock
from FCFS import FCFS
from SRTN import SRTN
from HPF import HPF
from RR import RR


def _create_scheduler(algorithm, context_switching_time, time_quantum):
    if algorithm == "HPF":
        return HPF(context_switching=context_switching_time)
    elif algorithm == "FCFS":
        return FCFS(context_switching=context_switching_time)
    elif algorithm == "RR":
        return RR(context_switching=context_switching_time, time_quantum=float(time_quantum))
    else:
        return SRTN(context_switching=context_switching_time)


class Manager:

    def __init__(self, input_file, context_switching_time, algorithm, time_quantum):
        # start scheduler
        self.scheduler = _create_scheduler(algorithm, context_switching_time, time_quantum)
        # start process manager
        self.process_manager = ProcessManager()
        # load it with processes from the output file
        self.process_manager.load_processes(input_file)
        # attach scheduler to it
        self.process_manager.attach_schedular(scheduler=self.scheduler)
        # create shared clock between scheduler and process manager
        self.clock = Clock()
        # attach it to both of them
        self.scheduler.attach_clock(clock=self.clock)
        self.process_manager.attach_clock(clock=self.clock)

    def loop(self):
        while len(self.process_manager.processes) is not 0 or len(self.scheduler.processes) is not 0:
            self.clock.notify()
        # self.scheduler.logger.write_log("results.txt")
        return self.scheduler.logger.plotting_data[0], self.scheduler.logger.plotting_data[1]
