
def readProcessesFile(inputfile,arrival,burst,priority):
   # arrival=[]
    #burst=[]
   # priority=[]
    #number_of_processes = 0
    #inputfile='output.txt'

    # read input file
    with open(inputfile) as input:
        # get number of processes
        number_of_processes = int(input.readline())

        for i in range(number_of_processes):
            z = [float(x) for x in input.readline().split()]
            arrival.append(z[0])
            burst.append(z[1])
            priority.append(z[2])


    return number_of_processes