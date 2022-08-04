def custom_input(input_msg):
    while True:
        try:
            number = int(input(input_msg))
            break
        except:
            print("Try again!")
            continue


    return number

num = custom_input("Enter an integer!\n")
print("***************")
print(f"Table of {num}")
print("***************")

for i in range(1,11):
    print(f"{num} x {i} = {num*i}")

