correct_password = '1234'

while True :

    password = input('please enter the password : ')

    if password == correct_password :

        print('access granted ')

        break

    else :

        print('please try again ...')