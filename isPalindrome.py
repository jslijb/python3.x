def isPalindrome(a):
    b = str(a)
    if len(b) % 2 != 0:
        i = 0
        while i <= len(b) / 2:
            if b[i] != b[len(b) - i - 1]:
                print a, 'is not Palindrome'
                break
            i += 1
        else:
            print a, 'is Palindrome'
    else:
        j = 0
        while j < len(b) / 2:
            if b[j] != b[len(b) - j - 1]:
                print a, 'is not Palindrome'
                break
            j += 1
        else:
            print a, 'is Palindrome'

isPalindrome(123456654321)