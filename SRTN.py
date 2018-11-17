from Scheduler import Scheduler, SchedulerState
from operator import attrgetter


class SRTN(Scheduler):

    def process_arrived(self, processes):
        super(SRTN, self).process_arrived(processes)
        for process in processes:
            # check if it should interrupt the running process
            if self.running_process is not None:
                if process.burst_time < self.running_process.remaining_time(self.clock.time):
                    # self.clock.notify_scheduler(process.arrival_time)
                    # notif yourself to stop the running process
                    self.notify()
        # run it if it is the first process
        if len(self.processes) == len(processes) and self.state is None:
            # it's as if the scheduler just finished saving last process data and
            # looking to start executing a new one
            self.state = SchedulerState.context_switching_dump
            # notify it to act upon
            self.notify()

    def sort_processes(self):
        self.processes.sort(key=attrgetter('burst_time', 'process_number'))

    def stop_process(self):
        self.running_process.stop(self.clock.time)
        # if got notified because process finished
        if self.running_process.burst_time == 0:
            self.processes.remove(self.running_process)

    def run(self):
        super(SRTN, self).run()
        self.clock.notify_scheduler(self.clock.time + self.running_process.burst_time)
