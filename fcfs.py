import numpy as np
from readProcessesFile import readProcessesFile
from writeresults import writeResults

def FCFS(): #suppose to take inputfile from the GUI
    #intialize list to gethe data from the file in
    arrival = []
    burst = []
    priority = []
    number_of_processes = 0
    inputfile='output.txt' #just for now
    number_of_processes = readProcessesFile(inputfile,arrival,burst,priority,number_of_processes)

    #print(number_of_processes)
    #print(arrival)
    #print(burst)
    #print(priority)


    wt=[] #list of waiting time for each process
    tat=[] #list of turnaround time for each process
    wtat=[] #list of weighted turnaround time for each process

    #calculate waiting time for each processe
    wt.append(0)
    for i in range(1,number_of_processes):
        w = 0
        for j in range(i):
            w += burst[j]
        wt.append(w)

    #calculate turnaround time for each processe, avg turnaround and avg weighted turn around
    avg_tat = 0
    avg_wtat = 0
    for i in range(number_of_processes):
        tat.append(burst[i] + wt[i])
        wtat.append(tat[i]/burst[i]) #not sure
        avg_tat += tat[i]
        avg_wtat += wtat[i]

    avg_tat /= number_of_processes
    avg_wtat /= number_of_processes

    writeResults(arrival, wt, tat, wtat, avg_tat, avg_wtat, number_of_processes)


FCFS()
