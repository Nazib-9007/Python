print(4 > 3 and 5 == 6)

cpu_usage = 75
memory_usage = 90
print(cpu_usage > 90 or memory_usage > 85)

email = True
password = False
print(f'Your access: {email and password}')

# Challange...
# Allow access only if the user is logged in or they are guest but they must not banned!
user = True
guset = False
is_banned = False
print((user or guset) and not is_banned)

#Challange...
#Security check: ensure the domain is not banned 
domain = "yahoo.com"
check = ['gamil.com', 'spam.com', 'hammail.com']
print(domain in check)
print(domain not in check)

#Challange...
# Make sure the email exists, and it's not empty
email = ""
empty = ""
print(email != "")
email = None
print(email is not None and email !="")

print(email is empty)

#1. Check is the user's name is not empty and the age is greater than or equal to 18;

user_name = 'John Doe'
age = 21
print(user_name != "" and age > 18)

#2. Check if the password is at least 8 characters long and does not contain spaces;

password = "123456 "
print(len(password) > 8 and " " not in password)

#3. Check if a user's email is not empty, contain '@' and ends with '.com'

user_mail = "@gmail.com"
print(user_mail !="" and "@" in user_mail and user_mail.endswith('.com'))

#4. Check is a username is a string is not None, and is longer than 5 characters;

print(type(user_name) == str and user_name is not None and len(user_name) > 5)

#5. Check if the user is either an admin or a moderator, and either they're not banned or they've verified their email;

is_banned = False
is_verified = True
print((user_name == 'admin' or user_name == 'moderator') and (not is_banned or is_verified))
