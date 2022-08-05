#Input a statement and count each character, vowels and consonants

statement = input("Enter a sentence or word. ")
num_of_occurrences = {}
vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O','U')
num_of_vowels = 0
num_of_consonants = 0


# statement = "I am bareera"

for i in statement:
    try:
        num_of_occurrences["occurrences_of_character_" + i] += 1

    except:
        num_of_occurrences["occurrences_of_character_" + i] = 1

    no_vowel = True
    for j in vowels:
        if i == j:
            num_of_vowels += 1
            no_vowel = False
            break
    try:
        temp = int(i)
    except:
        if no_vowel and i != " " and i!=".":
            num_of_consonants += 1

if num_of_vowels == 0 and num_of_consonants ==0:
    print("Not a valid input")
else:
    print ("Number of occurrences of each character = ", num_of_occurrences)
    print ("Number of vowels = ", num_of_vowels)
    print ("Number of consonants = ", num_of_consonants)
