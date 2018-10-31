from tkinter import Tk, Label, Button, BOTTOM, filedialog, OptionMenu, StringVar, Entry, messagebox


class Gui:
    def __init__(self, master):
        self.master = master
        self.time_quantum_label = None
        self.time_quantum = None
        self.time_quantum_textbox = None
        self.context_switching = None
        self.algorithms = ["HPF", "FCFS", "RR", "SRTN"]
        self.current_algorithm = None
        self.input_file_name = ''
        self.init_gui()

    def init_gui(self):
        self.master.title("Os scheduler")

        self.time_quantum_label = Label(self.master, text="Specify time quantum:")

        var = StringVar(self.master)

        def validate_quantum(var):
            new_value = var.get()
            try:
                new_value == '' or float(new_value)
                self.time_quantum = new_value
            except:
                var.set(self.time_quantum)

        self.time_quantum = ''
        var.trace('w', lambda nm, idx, mode, var=var: validate_quantum(var))
        self.time_quantum_textbox = Entry(root, textvariable=var)

        button = Button(self.master, text = "Select input file" , command = self.select_file)
        button.pack()

        label = Label(self.master, text="Select scheduling algorithm:")
        label.pack()
        self.current_algorithm = StringVar(self.master)
        self.current_algorithm.set(self.algorithms[0])
        menu = OptionMenu(self.master, self.current_algorithm, self.algorithms[0], self.algorithms[1],
                       self.algorithms[2], self.algorithms[3], command=self.on_value_change)

        menu.pack()
        label = Label(self.master, text="context switching time:")

        label.pack()

        var = StringVar(self.master)

        def validate_context(var):
            new_value = var.get()
            try:
                new_value == '' or float(new_value)
                self.context_switching = new_value
            except:
                var.set(self.context_switching)

        self.context_switching = ''
        var.trace('w', lambda nm, idx, mode, var=var: validate_context(var))
        entry = Entry(root, textvariable=var)
        entry.pack()

        close_button = Button(self.master, text="Close", command=self.master.quit)
        close_button.pack(side=BOTTOM)

        close_button = Button(self.master, text="run", command=self.run)
        close_button.pack(side=BOTTOM)

    def validate_for_run(self):
        try:
            if len(self.input_file_name) == 0:
                raise IOError("You have to choose an input file to operate on!")
            if len(self.context_switching) == 0:
                raise ValueError("Context Switching time must be entered correctly!")
            if self.current_algorithm.get() == self.algorithms[2] and len(self.time_quantum) == 0:
                raise ValueError("Time Quantum must be entered correctly!")
        except Exception as error:
            messagebox.showerror("Error", repr(error))
        # pass

    def run(self):
        self.validate_for_run()
        # TODO : start the scheduler
        pass

    def select_file(self):
        self.input_file_name = filedialog.askopenfilename(title="Select input file",
                                       filetypes=(("text files", "*.txt"), ("all files", "*.*")))

    def on_value_change(self, event):
        if self.current_algorithm.get() != self.algorithms[2]:
            self.time_quantum_label.pack_forget()
            self.time_quantum_textbox.pack_forget()
        else:
            self.time_quantum_label.pack()
            self.time_quantum_textbox.pack()


root = Tk()
root.geometry("400x300")
my_gui = Gui(root)
root.mainloop()
