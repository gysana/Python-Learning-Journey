
# Factorial of a number using recursion

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


num = int(input("Enter a number: "))

result = factorial(num)

print("Factorial of", num, "is:", result)
# second program:


def sum_even_odd(start, end):
    even_sum = 0
    odd_sum = 0

    for i in range(start, end + 1):
        if i % 2 == 0:
            even_sum += i
        else:
            odd_sum += i

    return even_sum, odd_sum


start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

even_sum, odd_sum = sum_even_odd(start, end)

print("Sum of even numbers:", even_sum)
print("Sum of odd numbers:", odd_sum)
# third program:using function overloading


def calculate_price(original_price, discount=10):
    final_price = original_price - (original_price * discount / 100)
    return final_price


# Only original price is provided
price = float(input("Enter the original price: "))

choice = input("Do you want to enter a discount percentage? (yes/no): ").lower()

if choice == "yes":
    discount = float(input("Enter the discount percentage: "))
    final_price = calculate_price(price, discount)
else:
    final_price = calculate_price(price)

print("Final price after discount:", final_price)
#4th program --- convert a binary number taken as user input into its decimal equivalent:


binary = input("Enter a binary number: ")

decimal = 0
power = 0

for digit in binary[::-1]:
    decimal = decimal + int(digit) * (2 ** power)
    power = power + 1

print("Decimal equivalent:", decimal)
#5th program--- decimal into binary


num = float(input("Enter a floating-point number: "))

integer_part = int(num)
fractional_part = num - integer_part


integer_binary = bin(integer_part)[2:]


fractional_binary = ""

for i in range(10):
    fractional_part = fractional_part * 2

    if fractional_part >= 1:
        fractional_binary = fractional_binary + "1"
        fractional_part = fractional_part - 1
    else:
        fractional_binary = fractional_binary + "0"

print("Binary equivalent:", integer_binary + "." + fractional_binary)