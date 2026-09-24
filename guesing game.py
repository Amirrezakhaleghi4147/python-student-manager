Golden_number = 7

while True:

    guessed_number = int(input('please enter your number : '))

    if guessed_number > Golden_number:

        print('''you guessed the wrong number 🙃
and it's higher the golden number ''')

    if guessed_number < Golden_number:

        print('''you guessed the wrong number 🙃
and it's lower than golden number ''')

    else :

        print('you won 🥳')

        break