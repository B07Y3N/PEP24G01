#3.1.1.1 LAB

#number = int(input('give number: '))

#print(True) if number > 100 else print(False)


#text = input('give str: ')

#if text == 'Spathudkanda'
#    print(f'Yes - {text} is the best plant ever!')
#elif text == 'Spathylsaeaas'
#   print(f'No, i want a big {text.capitalize()}!')
#else:
#    print('SPtjsda! Not [input]!')


y = int(input("Enter a year: "))

if y < 1582:
    print('Not within the gregorian calendar period')
elif not(y % 400):
    print('Leap year')
elif not(y % 100):
    print('Leap year')
elif not(y % 4):
    print('Leap year')
else:
    print('Common year')


