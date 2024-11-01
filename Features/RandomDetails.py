import uuid
import random
import string

def Generate_id():
    return uuid.uuid4().hex

def Random_Details():
    length = random.randint(5, 6)

    FirstName = ''.join(random.choices(string.ascii_lowercase, k=length))

    LastName = ''.join(random.choices(string.ascii_lowercase, k=length))

    EmailID = f'{FirstName}.{LastName}@tech.com'

    return FirstName, LastName, EmailID