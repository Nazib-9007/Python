date = "2026-10-18"
x = date[5:7]
print(f'The month is: {x}')
print(f'The day is: {date[8:]}')
print(f'From right side the day is: {date[-2:]}')

text = 'I love Javascript. Javascript is great!'
print(text)
new_text = text.replace('Javascript', 'Python')
print(new_text)
text_index = text.replace('Javascript', 'Python', 1)
print(text_index)

fruit = 'apple, banana, organe'
bucket = fruit.split(',')
print(bucket)

phrase = 'Hello coders. Learn python for future build Ai models!'
new_phrase = phrase.split(' ');
print(new_phrase)

data = 'orange, banana, mango; graps'
print(f'Before use replace() and split(): {data}')
print(f'After use reeplace(): {data.replace(';', ',')} and after use split(): {data.split(',')}')