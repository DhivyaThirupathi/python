def is_perfect_number(num):
    sum_of_divisors = 0
    for i in range(1, num):
        if num % i == 0:
            sum_of_divisors += i
    return sum_of_divisors == num

# Get the range from the user
start = int(input("Enter the starting number of the range: "))
end = int(input("Enter the ending number of the range: "))

print(f"Perfect numbers between {start} and {end} are:")

for num in range(start, end + 1):
    if is_perfect_number(num):
        print(num)
