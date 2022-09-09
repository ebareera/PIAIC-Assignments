list1 = [4, 6, "Karachi", "blue", 9, 8, "8", 11, "car", "Islamabad", "Lahore"]
list2 = ["parrot", "9", 8, "red", 11, "6", 7, 4, "Karachi", 8, 11]

common_elements = []

for e1 in list1:
    for e2 in list2:
        if e1 == e2:
            common_elements.append(e1)
            break

print ("Common elements are = ", common_elements)
