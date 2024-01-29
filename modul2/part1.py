str1 = 'hello world'
print(type(str1))
int1 = 100
print(type(int1))
none = None
print(type(none))

new = result = str1.capitalize()
print(type(result))

print('Returned type:', type(result))

str1 = 'hello world {} {}'
result = str1.format('test', 'test2')
print('Formatted String:', result)


str1 = 'hello world'
result = str1.center(30, '#')
print('Center String:', result)

# Print triangle using center method

print("/\\".center(10))
print("/  \\".center(10))
print("/____\\".center(10))