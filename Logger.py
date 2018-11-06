

class Logger:

    def __init__(self):
        # list of the times with the processes running in that time to be plotted
        self.plotting_data = [[0], [0]]
        self.arrival = {}
        self.running = {}
        self.waiting_time = {}
        self.start_running_time = 0

    def log_runtime(self, process, clock, starting=True):

        if clock.time is 0:
            self.plotting_data[1].pop()
        self.plotting_data[0].append(clock.time)
        if starting:
            self.start_running_time = clock.time
            self.arrived(process, clock, arriving=False)
            self.plotting_data[1].append(process.process_number)
        else:
            if process.process_number in self.running:
                self.running[process.process_number] += clock.time - self.start_running_time
            else:
                self.running[process.process_number] = clock.time - self.start_running_time
            self.plotting_data[1].append(0)
            if process.burst_time is not 0:
                self.arrived(process, clock, arriving=True)

    def arrived(self, process, clock, arriving=True):
        if arriving:
            self.arrival[process.process_number] = clock.time
        else:
            if process.process_number in self.waiting_time:
                self.waiting_time[process.process_number] += clock.time - self.arrival[process.process_number]
            else:
                self.waiting_time[process.process_number] = clock.time - self.arrival[process.process_number]
            self.arrival[process.process_number] = 0

    def write_log(self, output_file):
        sorted_waiting = dict(sorted(self.waiting_time.items()))
        sorted_runtime = dict(sorted(self.running.items()))
        turnaround_time = []
        weighted_turnaround_time = []
        with open(output_file, "w") as output:
            for process in sorted_runtime.keys() & sorted_waiting.keys():
                ta = sorted_waiting[process] + sorted_runtime[process]
                wta = ta / sorted_runtime[process]
                output.write("process: " + str(process) + "\tturnaround time:\t" +
                             str(ta) + "\t weighted turnaround time:\t" + str(wta) + "\n")
                turnaround_time.append(ta)
                weighted_turnaround_time.append(wta)
            output.write("scheduler average turnaround time:\t" + str(sum(turnaround_time) / len(turnaround_time)) +
                         "\nscheduler average weighted turnaround time:\t" +
                         str(sum(weighted_turnaround_time) / len(weighted_turnaround_time)))


