#1. Python list with odd and even numbers
numbers = [10,501,22,37,100,999,87,351]
odd_numbers = []
even_numbers = []
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)
print("Odd numbers:", odd_numbers)
print("Even numbers:", even_numbers)

#2. Task to count the number of prime numbers and display it in separate list
numbers = [10, 501, 22, 37, 100, 999, 87, 351]
def get_primes(num_list):
    prime_numbers = []
    for num in num_list:
        if num > 1:
            is_prime = True
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                prime_numbers.append(num)
    return prime_numbers
prime_numbers = get_primes(numbers)
prime_count = len(prime_numbers)
print("Count of prime numbers:", prime_count)
print("Prime numbers:", prime_numbers)

#3. Count of happy numbers in the list
numbers = [10, 501, 22, 37, 100, 999, 87, 351]
def happy_number(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(digit)**2 for digit in str(n))
    return n == 1
happy_count = sum(happy_number(num) for num in numbers)
print("Count of happy numbers:", happy_count)

#4. Sum of 1st and last digit of an integer
def sum_first_last_digit(number):
    num_str = str(number)
    first_digit = int(num_str[0])
    last_digit = int(num_str[-1])
    sum_digits = first_digit + last_digit 
    return sum_digits
number = int(input("Enter an integer: "))
print("Sum of the first and last digits of", number, "is:", sum_first_last_digit(number))

#5. Mango distribution
def distribute_mangoes(mangoes, students):
    mangoes.sort()
    min_difference = float('inf')
    start_index = 0
    for i in range(len(mangoes) - students + 1):
        difference = mangoes[i + students - 1] - mangoes[i]
        if difference < min_difference:
            min_difference = difference
            start_index = i
    distribution = mangoes[start_index:start_index + students]
    return distribution
# Eg:
mangoes = [10, 7, 15, 20, 5, 22]
students = 7
distribution = distribute_mangoes(mangoes, students)
print("Mango distribution:", distribution)

#6. Find duplicates in 3 lists
list1 = [1, 2, 3, 4, 5, 2, 6, 7, 8]
list2 = [7, 8, 9, 10, 11, 12, 9, 13, 14]
list3 = [15, 16, 17, 18, 19, 20, 16, 21, 22, 23]

def find_duplicates(lst):
    duplicates = []
    unique_elements = set()
    for item in lst:
        if item in unique_elements:
            duplicates.append(item)
        else:
            unique_elements.add(item)
    return duplicates
duplicates1 = find_duplicates(list1)
duplicates2 = find_duplicates(list2)
duplicates3 = find_duplicates(list3)
print("Duplicates in list 1:", duplicates1)
print("Duplicates in list 2:", duplicates2)
print("Duplicates in list 3:", duplicates3)

#7. Find first non repeating element in integer list
def first_non_repeating_element(lst):
    frequency = {}

    for num in lst:
        frequency[num] = frequency.get(num, 0) + 1

    for num in lst:
        if frequency[num] == 1:
            return num

    return None

# Eg:
numbers = [1, 2, 3, 4, 2, 1, 5, 6, 3, 4, 7]
result = first_non_repeating_element(numbers)

if result is not None:
    print("First non-repeating element:", result)
else:
    print("No non-repeating element found.")
    
#8. Find minimum in rated & sorted list
def find_minimum(sorted_list):
    if not sorted_list:
        return None
    return sorted_list[0]

# Eg:
sorted_list = [1, 2, 3, 4, 5, 6, 7]
minimum = find_minimum(sorted_list)
print("Minimum element in the sorted list:", minimum)

#9. Triplet sum equals to 59
def find_triplet_with_sum(nums, target):
    n = len(nums)
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if nums[i] + nums[j] + nums[k] == target:
                    return [nums[i], nums[j], nums[k]]

nums = [10, 20, 30, 9]
target = 59
triplet = find_triplet_with_sum(nums, target)

if triplet is not None:
    print("Triplet with sum", target, ":", triplet)
    
#10. Sub list with sum zero in the given list
def sublist_with_zero_sum(nums):
    prefix_sum = set()
    current_sum = 0
    for num in nums:
        current_sum += num
        if current_sum == 0 or current_sum in prefix_sum:
            return True
        prefix_sum.add(current_sum)
    return False

nums = [4, 2, -3, 1, 6]
if sublist_with_zero_sum(nums):
    print("Yes, there is a sublist with sum zero.")
else:
    print("No, there is no sublist with sum zero.")
    
#END OF TASK SESSION 6