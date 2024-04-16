#Expected result is [10,501,22,37,100,999,87,351] since all are greater than 4. 

#Check if integer or string
data = [10, "lamda", 501, "list", 22, "task",37,100]
result = map(lambda x: "integer" if isinstance(x, int) else "string", data)
print(list(result))

#Fibonacci series fro 1 to 50
from functools import reduce
fib_series = lambda n: reduce(lambda x, _: x+[x[-1]+x[-2]], range(n-2), [0, 1])
result = list(filter(lambda x: x <= 50, fib_series(50)))
print(result)

#Validate email, bangladesh mob numbers, USA telephone numbers and password
import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))
def validate_bangladesh_mobile(mobile):
    pattern = r'^01[3-9]\d{8}$'
    return bool(re.match(pattern, mobile))
def validate_usa_telephone(telephone):
    pattern = r'^\(?(\d{3})\)?[-.\s]?(\d{3})[-.\s]?(\d{4})$'
    return bool(re.match(pattern, telephone))
def validate_password(password):
    pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{16}$'
    return bool(re.match(pattern, password))

#END OF TASK SESSION9 