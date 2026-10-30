# # List Syntax....
# thislist = ['apple', 'banana', 'cherry']
# print(thislist);

# my_list = ['apple', 'banana', 'cherry', 'apple', 'cherry']
# print(my_list);

# print(len(my_list))

# list1 = ['apple', 'banana', 'cherry']
# list2 = [1, 5, 7, 9, 3]
# list3 = [True, False, False]
# print(list1, list2, list3)

# list1 = ["abc", 34, True, 40, "male"]
# print(list1)

# # List Constructor...
# my_list = list(('apple', 'banana', 'cherry', 'lemon'))
# print(my_list)

# # List Accessing Items..
# this_list = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(this_list[2:5])
# print(this_list[:4])
# print(this_list[2:])
# print(this_list[-4:-1])

# if 'apple' in this_list:
#     print(f'Yes, {this_list[0]} is the fruits list');

# add_list = ['apple', 'banana', 'cherry']
# add_list[1:2] = ['blackcurrant', 'watermelon']
# print(add_list)

# # Loop in list...
# new_list = ['apple', 'banana', 'cherry']
# for i in range(len(new_list)):
#     print(new_list[i]);

# # using while loop...
# new_list = ['Can', 'Truck', 'Bus', 'Rickshaw']
# i = 0
# while i < len(new_list):
#     print(new_list[i])
#     i = i + 1;

# # Sort lists...
# this_List = [100, 50, 65, 82, 33]
# print(this_List)
# this_List.sort();
# print(this_List)

# this_List.sort(reverse=True)
# print(this_List);


# def myFunction(n):
#     return abs(n-50); #Sort the list based on how close the number is to 50:

# this_List = [100, 50, 65, 82, 33]
# this_List.sort(key=myFunction)
# print(this_List)

# this_List = ["banana", "Orange", "Kiwi", "cherry"]
# this_List.sort(key=str.lower)
# print(this_List)

# list1 = ["a", "b" , "c"]
# list2 = [1, 2, 3]
# for x in list2:
#   list1.append(x)
# print(list1)

# # Palindrome Solve...

# listP = [1,2,3,2,1]
# list2 = listP.copy()
# list2.reverse()
# if listP == new_list :
#     print('Yse this is palindrome');
# else:
#     print('Sorry! this is note palindrome.');

# matrix = [
#     ['a', 'b', 'c'],
#     ['d', 'e', 'f'],
#     ['g', 'h', 'i']
# ]
# print(matrix[2])
# print(matrix[0][0])
# print(matrix[1][1])
# print(matrix[-1][-1])

# slice
# print(matrix[0:2])
# print(matrix[0:])
# print(matrix[:2])
# print(matrix[:])
# print(matrix[2][:2])

#Unpacking List
stdInfo = ['John Doe', 9007, 'Student', 'city', 100010, 'Bangladesh']
name, id, role,city, code, country = stdInfo
print(id)
print(name)

# Asterisk using in List to find the unnecessary info
name, *details= stdInfo 
print(name)
print(details)
print(country)

# user = input('Enter std name: ')
# if user:
#     print(details)
# else:
#     print('Not a  student!');

#Skiping the gurbage data:
name, *_, country = stdInfo
print(name)
print(*_)
print(f'The gurbage items: {_}')
print(country)