from Process import Process
from operator import itemgetter, attrgetter


class ProcessManager:

    def __init__(self):
        self.processes = []
        self.clock = None
        self.scheduler = None

    def load_processes(self, inputfile):
        # inputfile='output.txt'

        # read input file
        with open(inputfile) as input_:
            # get number of processes
            number_of_processes = int(input_.readline())

            for _ in range(number_of_processes):
                process_parameters = [float(x) for x in input_.readline().split()]
                process_number = process_parameters[0]
                arrival_time = process_parameters[1]
                burst_time = process_parameters[2]
                priority = process_parameters[3]
                self._add_process(process_number, arrival_time, burst_time, priority)
        self.processes.sort(key=attrgetter('arrival_time', 'process_number'))

    def _add_process(self, process_number, arrival_time, burst_time, priority):
        self.processes.append(Process(process_number, arrival_time, burst_time, priority))
        
    def attach_clock(self, clock):
        self.clock = clock
        self.clock.process_manager = self
        # set first notification time for the clock
        self.clock.notify_process_manager(self.processes[0].arrival_time)

    def attach_schedular(self, scheduler):
        self.scheduler = scheduler

    def notify(self):
        self.scheduler.process_arrived(self.processes.pop(0))
        if len(self.processes) is not 0:
            self.clock.notify_process_manager(self.processes[0].arrival_time)


# process_manager = ProcessManager()
# process_manager.load_processes('output.txt')
# for process in process_manager.processes:
#     print(process)