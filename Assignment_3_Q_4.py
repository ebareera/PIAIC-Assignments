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


    print(line)
