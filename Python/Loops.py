files = ['Report.csv', 'StudentInfo.csv', 'TotalIncome.TXT']
for file in files:
    file = file.strip().lower().replace('txt', 'csv')
    print(f'The list of files are: {file}')

fruits = ['apple', 'banana', 'orangge']
for x in fruits:
    print(x)
    if x == 'apple':
        break

for i in range(5):
    print(f'Count: {i}')

for id in range(101, 126):
    print(f'Student id: {id}')

#Challange time...
for pattern in range(1,7):
    print('*' * pattern)