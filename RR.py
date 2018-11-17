from Scheduler import Scheduler, SchedulerState


class RR(Scheduler):

    def process_arrived(self, processes):
        super(RR, self).process_arrived(processes)
        # check if it had only one process taking the whole cpu before new process arriving
        if len(self.processes) - len(processes) == 1 and self.running_process is not None:
            # check if it is past its original time quantum (it's taking overtime)
            if self.clock.time - self.running_process.started_running_time > self.time_quantum:
                # stop the running process now
                self.notify()
            # stop the running process when its time quantum finishes
            elif self.running_process.burst_time > self.time_quantum:
                self.clock.notify_scheduler(self.running_process.started_running_time + self.time_quantum)
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
        if len(self.processes) == 1:
            # run the process until some other process arrives
            self.clock.notify_scheduler(self.clock.time + self.running_process.burst_time)
        elif self.running_process.burst_time < self.time_quantum:
            self.clock.notify_scheduler(self.clock.time + self.running_process.burst_time)
        else:
            self.clock.notify_scheduler(self.clock.time + self.time_quantum)
