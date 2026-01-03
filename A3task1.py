def fact(num):
    if num == 1:
        return 1
    else:
        factorial = num * fact(num-1)
        return factorial
m = int(input("Enter a number: "))
print(f"Factorial of {m} is : {fact(m)}")