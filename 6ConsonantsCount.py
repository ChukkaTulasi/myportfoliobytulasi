input = input("Enter string here : ")
b = input.lower()
list = ["a","e","i","o","u"]
count = 0
for i in b:
    if i not in list:
        count = count + 1
print("Consonants in ", b , " is ",count)