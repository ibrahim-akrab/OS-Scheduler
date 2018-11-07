from Scheduler import Scheduler, SchedulerState
from operator import attrgetter


class SRTN(Scheduler):

    def process_arrived(self, processes):
        super(SRTN, self).process_arrived(processes)
        # prepare processes for the next round
        self.processes.sort(key=attrgetter('burst_time', 'process_number'))
        for process in processes:
            # check if it should interrupt the running process
            if self.running_process is not None:
                if process.burst_time < self.running_process.remaining_time(self.clock.time):
                    # self.clock.notify_scheduler(process.arrival_time)
                    # notif yourself to stop the running process
                    self.notify()
        # run it if it's the first process
        if len(self.processes) == len(processes) and self.state is None:
            self.run()

    def notify(self):

        if self.state is SchedulerState.running:
            self.running_process.stop(self.clock.time)
            # if got notified because process finished
            if self.running_process.burst_time == 0:
                self.processes.remove(self.running_process)
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
        super(SRTN, self).run()
        self.clock.notify_scheduler(self.clock.time + self.running_process.burst_time)
