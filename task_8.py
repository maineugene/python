def task(s):
    for i in range(len(s) // 2):
        temp1 = s[i]
        temp2 = s[len(s) - 1 - i]
        if (temp1 != temp2):
            return False
    return True
s = input("Enter string: ")
if(task(s)):
    print("Palindrome")
else:
    print("Not Palindrome")