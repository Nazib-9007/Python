print("Hello Python developer!")

x = input("Take a number: ")
print(type(x))

#type conversion--> python input function always takes anything as a string..
x = int(input("Enter first number: "))
y = int(input("ENter second number: "))
print(x + y)
print(type(x));

# Transform replace() method..
phone = "+49 (176) 123-4567"
print(phone)
convert = phone.replace("+", "00").replace(" ", "").replace("(", "").replace(")", "").replace("-", "")
print(convert)