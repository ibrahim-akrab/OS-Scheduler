import numpy as np
import sys, getopt

def main(argv):
    inputfile = 'input.txt'
    outputfile = 'output.txt'
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print('Process\ Generator.py -i <inputfile> -o <outputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('Process\ Generator.py -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg


    # read input file
    with open(inputfile) as input:
        # get number of processes
        number_of_processes = int(input.readline())
        # get arrival distribution
        arrival_dist = [float(x) for x in input.readline().split()]
        # get burst distribution
        burst_dist = [float(x) for x in input.readline().split()]
        # get priority dist
        priority_dist = float(input.readline().split()[0])

    # prepare arrival times
    arrival_time = [str(np.abs(np.random.normal(arrival_dist[0], arrival_dist[1]))) for i in range(number_of_processes)]
    # prepare burst times
    burst_time = [str(np.abs(np.random.normal(burst_dist[0], burst_dist[1]))) for i in range(number_of_processes)]
    # prepare priority times
    priority = [str(np.abs(np.random.poisson(priority_dist))) for i in range(number_of_processes)]

    # print output file
    with open(outputfile, "w") as output:
        output.write(str(number_of_processes)+"\n")
        for i in range(number_of_processes):
            output.write(str(i+1) + " " + arrival_time[i] + " " + burst_time[i] + " " + priority[i] + "\n")




if __name__ == "__main__":
    main(sys.argv[1:])