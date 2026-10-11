num = int(input("Enter a number: "))
sum = 0
temp = num
s = len(str(num))
while temp > 0:
    digit = temp % 10
    sum += digit ** s
    temp //= 10

if sum == num:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")