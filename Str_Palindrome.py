s = "madam"
n = len(s)
ans = ""
for i in range(n-1,-1,-1):
    ans = ans + s[i]
print(ans)
if ans == s:
    print("Palindrome")
else:
    print("non palindrome")