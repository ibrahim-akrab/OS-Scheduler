from Scheduler import Scheduler, SchedulerState


class RR(Scheduler):

    def process_arrived(self, processes):
        super(RR, self).process_arrived(processes)
        # run it if it is the first process
        if len(self.processes) == len(processes) and self.state is None:
            # it's as if the scheduler just finished saving last process data and
            # looking to start executing a new one
            self.state = SchedulerState.context_switching_dump
            # notify it to act upon
            self.notify()

    # no need for sorting, they are already sorted
    def sort_processes(self):
        pass

    def stop_process(self):
        self.running_process.stop(self.clock.time)
        # if got notified because process finished
        if self.running_process.burst_time == 0:
            self.processes.remove(self.running_process)
        else:
            # pass it to the end of the list
            self.processes.append(self.processes.pop(0))

    def run(self):
        super(RR, self).run()
        if self.running_process.burst_time < self.time_quantum:
            self.clock.notify_scheduler(self.clock.time + self.running_process.burst_time)
        else:
            self.clock.notify_scheduler(self.clock.time + self.time_quantum)
