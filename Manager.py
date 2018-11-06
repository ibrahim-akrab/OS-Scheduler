from Scheduler import Scheduler
from ProcessManager import ProcessManager
from Process import Process
from Clock import Clock
from FCFS import FCFS

class Manager:

    def __init__(self, input_file):
        # start scheduler
        self.scheduler = FCFS(0.1)
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
            # run processes if scheduler has any
            # if len(self.scheduler.processes):
            #     self.scheduler.run()


manager = Manager('output.txt')
manager.loop()