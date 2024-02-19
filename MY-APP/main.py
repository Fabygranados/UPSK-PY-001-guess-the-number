import random

welcome_text = ' O(∩_∩)O Welcome to my Numbers Game!!!   '
print(welcome_text)
text_start = '°°° Start °°°'
print(text_start)

guess = False
while not guess:
    random_number = random.randint(1, 10)
    number_user = int(input('Enter a number 1 to 10: '))

    if number_user == random_number:
        print('*** You Win!! ***')
        guess = True

    else:    
        print('Your Number:', number_user)
        print('Random Number:', random_number)