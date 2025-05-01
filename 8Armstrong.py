input = int(input("Enter a number Here :"))
num = input
sum = 0
while (num > 0):
    r = num%10
    sum = sum + r**3
    num = num//10
if(sum == input):
    print("sum is: " , sum)
    print("ARMSTRONG NUMBER")
else:
    print("sum is: " , sum)
    print("NON ARMSTRONG NUMBER")