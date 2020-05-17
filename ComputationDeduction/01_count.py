lines = open("01_results.txt").readlines()

count = 0
for line in lines:
    if line[0] == "-":
        if count > 0:
            print(count) 
        count = 0
        #print(line)
    else:
        count += line.count("s")  
