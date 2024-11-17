# This module is used to return all type of dummy details like first_name, last_name, credit_card, phone_number, etc..
import string
import random
import os

def Random_names():
    
    length = random.randint(5, 6)
    company_legth = random.randint(5, 8)
    first_name = ''.join(random.choices(string.ascii_lowercase, k=length))
    last_name = ''.join(random.choices(string.ascii_lowercase, k=length))
    email_id = f'{first_name}.{last_name}@gmail.com'
    CreditCard_number = ''.join(str(random.randint(0, 9)) for _ in range(15))
    ZipCode = ''.join(str(random.randint(1, 9)) for _ in range(5))
    phone_number = ''.join(str(random.randint(1, 9)) for _ in range(10))
    AreCode = ''.join(str(random.randint(1, 9)) for _ in range(5))
    company_name = ''.join(random.choices(string.ascii_lowercase, k=company_legth))


    return first_name, last_name, email_id, CreditCard_number, ZipCode, phone_number, AreCode, company_name


