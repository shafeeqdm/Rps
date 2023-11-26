import random

user_input = input('Select r-Rock,p-Paper,s-Scissors :')
computer_input = random.choice(['r','s','p'])

print(user_input,' ',computer_input)

if user_input == computer_input:
    print('DRAW')
elif (user_input == 'r' and computer_input == 'p') or (user_input == 'p' and computer_input == 's') or (user_input == 's' and computer_input == 'r'):
    print('LOST')
else:
    print('WON')