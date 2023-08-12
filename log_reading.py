f = open("Log Analyzer\input.txt", "r")

for line in f:
    linestrip = line.strip().split(" ")
    print(linestrip)
    date = linestrip[0]
    time = linestrip[1]
    message = linestrip[2]
    user = linestrip[-1]
    print(f"{user} ==> Error {message} at {date} - {time}")
    

f.close()