import random
import string

user_data[]

firstname = input('First name : ')
lastname = input('Last Name : ')
email = input('Email : ')

details = [firstname, lastname, email]

def get_password(details):
    letters = string.ascii_letters
    rand = ''.join(random.choice(letters) for i in range(5))
    password = str(details[0][0:2] + details[1][-2:] + rand)

    return password

pwd = get_password(details)
print(pwd)

while True:
is_satisfied = input(f"Are you satisfied with this password. if yes enter Yes if no, enter No: ")

if is_satisfied == 'Yes':
    user_details = {
        'First name'= firstname
        'Last name'= lastname
        'Email'= email
        'password' = pwd
    }

    print(f"user{user_details}")
    break
else:
    print("enter your preferred password")
    preferred_password = input('my password: ')
    print(f"new_password:{preferred_password}")

if len(preferred_password) >= 7:
    user_details = {
        'First name'= firstname
        'Last name'= lastname
        'Email'= email
        'password' = preferred_password
    }

    print(f"user{user_details}")
else:
    print("password must be more than 7 characters")
    preferred_password = input('my password: ')
    print("password is ok")
    user_details = {
        'First name'= firstname
        'Last name'= lastname
        'Email'= email
        'password' = preferred_password
    }

user_data.append(user_details)








