# Make a diamond
#     5
#    4 4
#   3   3
#  2     2
# 1       1
#  2     2
#   3   3
#    4 4
#     5

for i in range(5, 0, -1):
    line = ""
    for j in range(i):
        line +=" "
    line += str(i)
    
    if (i<5):
        for z in range (1, 10-2*i, 1):
            line +=" "
        line += str(i)


    print(line)

for i in range(2, 6):
    line = ""
    for j in range(i):
        line +=" "
    line += str(i)
    
    if (i<5):
        for z in range (1, 10-2*i, 1):
            line +=" "
        line += str(i)


    print(line)