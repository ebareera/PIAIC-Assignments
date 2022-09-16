#Read a text file and save different paragraphs in different text files.

with open("mytextfile.txt", "r") as thefile:
    paras = thefile.readlines()

# for line in paras:
#     if line == "\n":
#         paras.remove(line)

while(True):
    try:
        paras.remove("\n")
    except:
        break

# print (len(paras))
for i in range(0, len(paras)):
    filename = "para" + str(i+1)
    # print (filename)
    with open(filename, 'w') as thefiles:
        thefiles.write(paras[i])
