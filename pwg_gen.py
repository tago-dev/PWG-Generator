import random

lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWZYZ'
numbers = '0123456789'
symbols = '!@#$%&_-()=*:/!?+.'

string = lower + upper + numbers + symbols
length = int(input('How many characters do you want in your password? '))
password = "".join(random.sample(string, length))

print('Your generated password is: ', password)