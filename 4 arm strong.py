num = 153
orig = num
digits = len(str(num))
total = 0

while num > 0:
    digit = num % 10
    total += digit ** digits
    num //= 10

if total == orig:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")
