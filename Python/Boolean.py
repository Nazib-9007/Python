# print(bool())
# print(bool(""))
# print(bool(0))
# print(bool("Hi! Python"))
# print(bool(5))
# print(bool(True))

# boolean functions: bool(), all(), any(), isintaence();

# Verify if any input field is empty??
email = ""
phone = "015-342634897"
username = ""

# any()

x = any([email, phone, username]) 
"""
here any() refers to any value is True then entire result will be True; 
"""
print(f'The return type is {x} = For any() here email is ({bool(email)}) + phone is ({bool(phone)}) + username  is ({bool(username)})')

# all()

x = all([email, phone, username]) 
"""
here all() refers to any value is False then entire result will be False; 
"""
print(f'The return type is {x} = For all() here email is ({bool(email)}) + phone is ({bool(phone)}) + username  is ({bool(username)})')

# isintaence()
print(isinstance(12345, int))
print(isinstance("Python", str))
print(isinstance(True, str))
print(isinstance("123", int))
print(isinstance(4.90, float))

# Is age between 18 and 30?
age = 25
print(f'The age is between 18 and 30: {18 <= age <= 30} age is {age}')
age = 15
print(f'The age is between 18 and 30: {18 <= age <= 30} age is {age}')