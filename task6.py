#Python list with odd and even numbers
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

#Task to count the number of prime numbers and display it in separate list
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

#Count of happy numbers in the list
numbers = [10, 501, 22, 37, 100, 999, 87, 351]
def is_happy_number(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(digit)**2 for digit in str(n))
    return n == 1
happy_count = sum(is_happy_number(num) for num in numbers)
print("Count of happy numbers:", happy_count)



