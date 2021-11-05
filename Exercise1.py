a = int(input("Please enter a positive number: "))
odd_numbers = 0
even_numbers = 0
counter_for_even = 0
for i in range(1, a + 1):
    if i % 2 == 0:
        even_numbers += i
        counter_for_even += 1
    else:
        odd_numbers += i


print("Sum of odd numbers --> {}".format(odd_numbers))
print("Average of even numbers --> {}".format(even_numbers/counter_for_even))
