from Scheduler import Scheduler, SchedulerState
from operator import attrgetter

class HPF(Scheduler):

    def process_arrived(self, processes):
        super(HPF, self).process_arrived(processes)
        if len(self.processes) > 1:
            temp = self.processes[1:len(self.processes)]
            temp2 = [self.processes[0]]
            temp.sort(key=attrgetter('priority'),reverse = True)
            self.processes = temp2 + temp
         # if len(self.processes) > '3':
             # a7a = 0
        self.logger.arrived(processes, self.clock, arriving=True)
        # run it if it is the first process
        if len(self.processes) is 1 and self.state is None:
            self.run()

    def notify(self):
        if self.state is SchedulerState.running:
            self.running_process.stop(self.clock.time)
            process = self.processes.pop(0)
            # process.stop(self.clock.time)
            self.logger.log_runtime(process, self.clock, starting=False)
            print(self.clock, "finished running", process)
            self.state = SchedulerState.context_switching
            print(self.clock, "started context switching")
            self.clock.notify_scheduler(self.clock.time + self.context_switching)
        elif self.state is SchedulerState.context_switching:
            self.state = None
            print(self.clock, "finished context switching")
            if len(self.processes) is not 0:
                self.run()

    def run(self):
        process = self.processes[0]
        self.logger.log_runtime(process, self.clock, starting=True)
        print(self.clock, "started running", process)
        self.clock.notify_scheduler(self.clock.time + process.burst_time)
        self.state = SchedulerState.running
        self.running_process = process
        process.run(self.clock.time)

