# find total no of vowels and consonant from string
x = input("Enter String : ")
vowels_count = 0
cons_count = 0
for char in x:
    if (char>='a' and char<='z') and (char>='a' and char<='z' ): 
        if char in "aeiouAEIOU":
            vowels_count += 1
        else:
            cons_count+=1

print("Vowels Count = ",vowels_count)
print("Consonant Count = ",cons_count)