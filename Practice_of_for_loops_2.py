# Make an output like this
# 1 2 3 4 5 6
# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1

for i in range(7,0,-1):
    line = ""
    for j in range(1,i):
        line += str(j)
        line += " "
    print(line)
