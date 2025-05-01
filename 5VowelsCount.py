input = input("Enter  a string : ")
b = input.lower()
list = ["a","e","i","o","u"]
count = 0
for i in b:
    if i in list:
        count = count + 1
print("Number of vowels in " , b ," is: ",count)