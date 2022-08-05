#Check if input is palindrome or not

statement = input("Enter a word. ")
#statement = "civic"
palindrome = False

# for i in statement:
#     for j in (-1,-(len(statement)+1)):
#         if i==j:
if len(statement)%2:      #odd
    upper_range = int((len(statement)-1)/2)
#    print (upper_range, "in %2 True")
else:                     #even
    upper_range = int(len(statement)/2)
#    print(upper_range)

for i in range(0,upper_range):
    if statement[i] == statement[-(i+1)]:
        palindrome = True
    else:
        palindrome = False
        break

if palindrome:
    print("Input is a palindrome.")
else:
    print ("Not a palindrome.")

