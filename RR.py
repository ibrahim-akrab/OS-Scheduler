from Scheduler import Scheduler, SchedulerState


class RR(Scheduler):

    def process_arrived(self, processes):
        super(RR, self).process_arrived(processes)
        # run it if it's the first process
        if len(self.processes) == len(processes) and self.state is None:
            self.run()

    def notify(self):

        if self.state is SchedulerState.running:
            self.running_process.stop(self.clock.time)
            # if got notified because process finished
            if self.running_process.burst_time == 0:
                self.processes.remove(self.running_process)
            else:
                # pass it to the end of the list
                self.processes.append(self.processes.pop(0))
            self.logger.log_runtime(self.running_process, self.clock, starting=False)
            # print(self.clock, "stopped running", self.running_process)
            self.running_process = None
            self.state = SchedulerState.context_switching
            # print(self.clock, "started context switching")
            self.clock.notify_scheduler(self.clock.time + self.context_switching)
        elif self.state is SchedulerState.context_switching:
            self.state = None
            # print(self.clock, "finished context switching")
            if len(self.processes) is not 0:
                self.run()

    def run(self):
        super(RR, self).run()
        if self.running_process.burst_time < self.time_quantum:
            self.clock.notify_scheduler(self.clock.time + self.running_process.burst_time)
        else:
            self.clock.notify_scheduler(self.clock.time + self.time_quantum)
