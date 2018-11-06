from Scheduler import Scheduler, SchedulerState


class FCFS(Scheduler):

    def process_arrived(self, process):
        print(self.clock, "arrived", process)
        self.processes.append(process)
        if len(self.processes) is 1:
            self.run()

    def notify(self):
        if self.state is SchedulerState.running:
            process = self.processes.pop(0)
            print(self.clock, "finished running", process)
            self.state = SchedulerState.context_switching
            print(self.clock, "started context switching")
            self.clock.notify_scheduler(self.context_switching)
        elif self.state is SchedulerState.context_switching:
            print(self.clock, "finished context switching")
            if len(self.processes) is not 0:
                self.run()

    def run(self):
        process = self.processes[0]
        print(self.clock, "started running", process)
        self.clock.notify_scheduler(process.burst_time)
        self.state = SchedulerState.running
        process.run(process.burst_time)

