name = input("Enter your name: ")

i_physics_marks = input("Enter your Physics marks: ")
i_chemistry_marks = input("Enter your Chemistry marks: ")
i_maths_marks = input("Enter your Maths marks: ")
i_english_marks = input("Enter your English marks: ")
i_urdu_marks = input("Enter your Urdu marks: ")
i_islamiat_marks = input("Enter your Islamiat marks: ")

physics_marks = int(i_physics_marks)
chemistry_marks = int(i_chemistry_marks)
maths_marks = int(i_maths_marks)
english_marks = int(i_english_marks)
urdu_marks =int(i_urdu_marks)
islamiat_marks = int(i_islamiat_marks)

total_marks = 100+100+100+100+100+50
obtained_marks=physics_marks + chemistry_marks + maths_marks + english_marks + urdu_marks + islamiat_marks
percentage = obtained_marks/total_marks
print("-------------------------------------------------")
print("\nDetailed Mark Certificate HSSC-I")
print("-------------------------------------------------")

print("Name: ", name)
print("Subject\t\tObtained Marks\t\tTotal Marks")
print("Physics\t\t",physics_marks, "\t\t100")
print("Chemistry\t",chemistry_marks,"\t\t100")
print("Maths\t\t", maths_marks, "\t\t100")
print("English\t\t", english_marks,"\t\t100")
print("Urdu\t\t",urdu_marks,"\t\t100")
print("Islamiat\t",islamiat_marks,"\t\t100")
print("Total Marks\t",obtained_marks,"\t\t",total_marks)
print("\nPercentage: ",percentage)