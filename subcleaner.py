import sys, re

L = 10 # Maximum accepted length for a line

if __name__ == "__main__":

    # Reading argument file
    file = open(str(sys.argv[1]),"r")
    lines = file.readlines()
    
    # Storing line number indices
    indices = []
    for line in lines:
        if line[0:-1].isnumeric():
            indices.append(lines.index(line))
    N = len(indices)
    sentences = [""] * N
    delete = [False] * N

    # Extracting strings for each line
    for i in range(N-1):
        ind = indices[i]
        while ind < indices[i+1]:
            if (ind - indices[i] > 1) and (indices[i+1] - ind) > 1:
                sentences[i] = sentences[i]+lines[ind][0:-1]
            ind += 1

    # Filtering the useless lines
    for i in range(N-1):
        if re.match(".{1,30}）.{0,"+str(L)+"}$|^.{1,"+str(L)+"}$", sentences[i]):
            delete[i] = True
    
    # Creating the filtered output
    output = []
    for i in range(N-1):
        ind = indices[i]
        while ind < indices[i+1]:
            if not delete[i]:
                output.append(lines[ind])
            ind += 1
    
    # Counting how many lines were deleted
    count = 0 
    for i in range(N-1):
        if (delete[i]):
            count += 1
    
    # Modifying the argument file
    print("Successfully deleted "+str(count)+" useless lines.")
    file = open(str(sys.argv[1]),"w+")
    file.writelines(output)
    file.close()
