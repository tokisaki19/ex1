def Palindrome(str):
    left = 0
    right = len(str)-1
    check = 0
    while (right > left):
        if str[left] != str[right]:
            check = 1
            break
        left = left + 1
        right = right - 1
    if check == 0:
            print (str, "is a palindrome")
    elif check == 1:
            print (str, "is not a palindrome")

Palindrome("DADD")