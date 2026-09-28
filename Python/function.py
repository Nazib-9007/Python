def my_function():
    print('Hello developer!');
my_function();

def temperature(temp):
    return (temp - 32) * 5 / 9
print(temperature(77));

# pass def means just ignore the function...
def myFunction():
    pass;
#Function Arguments..
def myFunction(fname):
    print(f'His/her name is {fname}');
myFunction('Rabbi bro')

# Arbitrary Arguments - *args...
def my_function(*kids):
    print("The youngest child is: " + kids[4]); #here kids[] try to check the index from the call function...
my_function('Emil', 'Tobias', 'Linus', 'John', 'Doe');