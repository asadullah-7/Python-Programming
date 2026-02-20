num = 54245
orig = num

rev = int(str(num)[::-1])

if orig == rev:
    print("Its Palindrome")
else:
    print("Its NOT Palindrome")
