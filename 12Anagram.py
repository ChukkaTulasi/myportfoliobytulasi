str1 = input("Enter string 1 Here :")
str2 = input("Enter String 2 Here :")
if(len(str1) == len(str2)):
    print("ANAGRAM STRINGS")
else:
    if (sorted(str1) == sorted(str2)) :
         print("ANAGRAM STRINGS")
    else:
         print("NON-ANAGRAM STRINGS")
print("Code Ended Here")