n = int(input("Enter a number Here"))
n1 = 0
n2 = 1
count = 2
if(n == 0):
    print("Please Enter Valid Number Only ")
elif (n==1):
    print("Fibonacci of ", n , " series is")
    print(n1)
else:
    print("Fibonacci of ", n , " series  is")
    print(n1)
    print(n2)
    while(count<n): 
        n3 = n1 + n2
        print(n3)
        count = count + 1
        n1 = n2
        n2 = n3
    
