import random

rand_list = []
nums_greater_than_40 = 0
sum_rand_list = 0

for i in range (1, 101):
    num = random.randint(1,100)
    rand_list.append(num)
print ("100 Random numbers = ", rand_list)
#print(len(rand_list))

for j in rand_list:
    if j <= 40:
        continue
    nums_greater_than_40 += 1
print ("\n1) Numbers greater than 40 = ", nums_greater_than_40)

for k in rand_list:
    sum_rand_list += k
#sum_rand_list = sum(rand_list)
print ("2) Sum of all random numbers = ", sum_rand_list)

max_num = rand_list[0]
min_num = rand_list[0]
for l in rand_list:
    if l > max_num:
        max_num = l
    if l < min_num:
        min_num = l

print(f"3) Highest number = {max_num}")
print(f"4) Lowest number = {min_num}")
print(f"5) Mean of the numbers = {sum_rand_list/len(rand_list)}")
