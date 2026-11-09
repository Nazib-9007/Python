# def greet():
#     print("Hello Python")
#     print("Welcome to python world!")
# greet()

# def check_weather():
#     temp = 25
#     if temp > 30:
#         print("It's hot weather");
#     else:
#         print("Cold weather!");
# check_weather()

# def calculate_price():
#     price = 100
#     tax = price * 0.1
#     print(f"Total: {price + tax}");
# calculate_price()

# discount_rate = 0.15 # global variable..
# def apply_discout(price):
#     discount = price * discount_rate
#     return discount
# print(apply_discout(1000))

# count = 0
# def modify_count():
#     global count
#     count += 1
# modify_count()
# modify_count()
# print(count)

# def introduce(name, age):
#     print(f"My name is {name} and age is {age}")
# introduce("John Doe", 25)

#parameters...

def greet(name):
    print(f"Hello, {name}");
greet("Alice")

def calculate_total(price, tax_rate, discount):
    tax = price * tax_rate
    total = price + tax - discount
    print(f"Total: {total}");
calculate_total(100, 0.08, 10)

def greet(name, greetings="Hello"):
    print(f"{greetings}, {name}")
greet("John Doe")
greet("John Doe", "Python khor") # override default parameter!

def create_profile(name, age, city):
    print(f"{name}, {age} from {city}");
create_profile("Alice", 25, "Washington D.C.") #positional arguments

create_profile(city="Belarush", name="Bob", age=22) # keyword arguments..
