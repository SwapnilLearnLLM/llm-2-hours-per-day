# Verify if a digit is od or Even

num = input("Enter a number: ")
num_int = int(num)
if num_int % 2 == 0: #Even number is cleanly divisible by 2
    print(f"{num} is Even")
else:
    print(f"{num} is Odd")  