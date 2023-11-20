def sum_of_natural_numbers(n):
    if n <= 0:
        return 0
    else:
        return n + sum_of_natural_numbers(n - 1)

number = int(input("Enter a positive integer: "))

if number <= 0:
    print("Please enter a positive integer.")
else:
    result = sum_of_natural_numbers(number)
    print(f"The sum of natural numbers up to {number} is {result}")
