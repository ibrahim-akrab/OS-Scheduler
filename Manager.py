from Scheduler import Scheduler
from ProcessManager import ProcessManager
from Process import Process
from Clock import Clock
from FCFS import FCFS
from SRTN import SRTN


class Manager:

    def __init__(self, input_file, context_switching_time, algorithm, time_quantum=0):
        # start scheduler
        self.scheduler = self._create_scheduler(algorithm, context_switching_time, time_quantum)
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
        self.scheduler.logger.write_log("results.txt")
        return self.scheduler.logger.plotting_data[0], self.scheduler.logger.plotting_data[1]

    def _create_scheduler(self, algorithm, context_switching_time, time_quantum=0):
        # TODO: uncommenet for each algorithm implemented
        return {
            # "HPF" : HPF(context_switching=context_switching_time),
            "FCFS" : FCFS(context_switching=context_switching_time),
            # "RR" : RR(context_switching=context_switching_time, quantum=float(time_quantum)),
            "SRTN" : SRTN(context_switching=context_switching_time)
        }[algorithm]
