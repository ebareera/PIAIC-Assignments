
def custom_input(input_msg):
    while True:
        try:
            number = int(input(input_msg))
            if number > 0 and number < 11:
                break

            if number < 1 or number > 10:
                print("Hint: The number is between 1 and 10. Both 1 and 10 are included. Try again!")
                continue

        except:
            print("Enter an integer only!")
            continue


    return number


import random

num = random.randint(1,10)
num2 = custom_input("Guess the number!   ")

for tries in range (1,4):
    if num == num2:
        print("You guessed right! The number is ", num)
        break
    else:
        tries_left = 3-tries
        print(f"Wrong Answer! You have {tries_left} try(s) left.")
        if tries_left != 0:
            num2 = custom_input("Try again!   ")
            continue
    print("You have Lost! The number is ", num)


