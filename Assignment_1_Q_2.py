def custom_input(input_msg):
    while True:
        try:
            number = int(input(input_msg))
            if number>0 and number<101 and not(input_msg=="Please enter your Islamiat marks: "):
                break
            elif number>0 and number<51 and input_msg=="Please enter your Islamiat marks: ":
                break
                
            else:
                if input_msg=="Please enter your Islamiat marks: ":
                    print("Enter an integer between 0 and 50.")
                else:
                    print("Enter an integer between 0 and 100.")
                continue
        except:
            if input_msg=="Please enter your Islamiat marks: ":
                print("Enter an integer between 0 and 50.")
            else:
                print("Enter an integer between 0 and 100.")
    return number



name = input("Enter your name: ")

physics_marks = custom_input("Please enter your Physics marks: ")
chemistry_marks = custom_input("Please enter your Chemistry marks: ")
maths_marks = custom_input("Please enter your Maths marks: ")
english_marks = custom_input("Please enter your English marks: ")
urdu_marks = custom_input("Please enter your Urdu marks: ")
islamiat_marks = custom_input("Please enter your Islamiat marks: ")


total_marks = 100+100+100+100+100+50

obtained_marks=physics_marks + chemistry_marks + maths_marks + english_marks + urdu_marks + islamiat_marks
percentage = obtained_marks/total_marks
print("-------------------------------------------------")
print("\nDetailed Mark Certificate HSSC-I")
print("-------------------------------------------------")

print("Name: ", name)
print("Subject\t\t Obtained Marks\t\tTotal Marks")
print("Physics\t\t\t ",physics_marks, "\t\t 100")
print("Chemistry\t\t ",chemistry_marks,"\t\t 100")
print("Maths\t\t\t ", maths_marks, "\t\t 100")
print("English\t\t\t ", english_marks,"\t\t 100")
print("Urdu\t\t\t ",urdu_marks,"\t\t 100")
print("Islamiat\t\t ",islamiat_marks,"\t\t 50")
print("Total Marks\t\t",obtained_marks,"\t\t",total_marks)
print("\nPercentage: ",percentage)