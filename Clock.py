class Clock:

    def __init__(self):
        self.time = 0
        # self.time_step = 0.1
        self.scheduler = None
        self.process_manager = None
        self.process_notification = 0
        self.scheduler_notification = 0

    def __repr__(self):
        return repr((self.time, self.process_notification, self.scheduler_notification))

    def attach_scheduler(self, scheduler):
        self.scheduler = scheduler

    def attach_process_manager(self, process_manager):
        self.process_manager = process_manager

    def notify(self):
        if self.scheduler_notification == self.process_notification:
            if self.scheduler_notification > self.time:
                self.time = self.scheduler_notification
                self.scheduler.notify()
                self.process_manager.notify()
        elif self.scheduler_notification < self.process_notification:
            if self.scheduler_notification > self.time:
                self.time = self.scheduler_notification
                self.scheduler.notify()
            elif self.process_notification > self.time:
                self.time = self.process_notification
                self.process_manager.notify()
        else:
            if self.process_notification > self.time:
                self.time = self.process_notification
                self.process_manager.notify()
            elif self.scheduler_notification > self.time:
                self.time = self.scheduler_notification
                self.scheduler.notify()

    # notify scheduler with time relative to current one
    def notify_scheduler(self, time):
        self.scheduler_notification = time

    # notify process manager with absolute time
    def notify_process_manager(self, time):
        self.process_notification = time
