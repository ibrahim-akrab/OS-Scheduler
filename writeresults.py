
def writeResults(arrival, wt, tat, wtat, avg_tat, avg_wtat, number_of_processes):

    # print output file
    outputfile = 'op.txt'
    with open(outputfile, "w") as output:
        output.write("arrival" + "   " + "wt" + "   " + "tat" + "   " + "wtat" + "\n")
        for i in range(number_of_processes):
            output.write(str(arrival[i]) + "   " + str(wt[i]) + "   " + str(tat[i]) + "   " + str(wtat[i]) + "\n")

