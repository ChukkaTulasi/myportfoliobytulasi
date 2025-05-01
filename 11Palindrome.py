input = int(input("Enter a number : "))
num = input
rev = 0
while num >0:
    r = num%10
    rev = rev * 10 +r
    num = num//10

if(rev == input):
    print("reverse is ",rev)
    print("input is " , input)
 
    print("PALINDROME")
else:
     print("reverse is ",rev)
     print("input is " , input)
     print("NON PALINDROME")