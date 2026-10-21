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