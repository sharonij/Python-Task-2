First_name = input(' What is your First name?  ')
Last_name = input('What is your Last name?  ')
Email_address = input('What is your Email address?  ')

print( First_name + Last_name + Email_address)

import random, string
firstname = input("Enter First name: ")

lastname = input("Enter Last name: ")

email = input("Enter E-mail: ")

pass1 = firstname[:2]
# String slicing i.e to select the first 2 letters in the first name

pass2 = lastname[-2:]
# String slicing i.e to select the last 2 letters in the last name

pass3 = ''.join(random.sample(string.ascii_lowercase,5))
# code to select a random lowercase letter 5 times and join them together
password = pass1+pass2+pass3

print(password)

password_satisfied = True
password_satisfied = False

if password_satisfied:
    print('user details')

else:
    print('choose a password')

(user_password) = "abcdefghij"

if len(user_password) < 7:
    print('Name must be at least 7 characters')

elif len(user_password) > 10:
    print(' Name must be a maximum of 10 characters')

else:
    print('user details')

>>>














