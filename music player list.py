stop = True


options = ['play ▶', 'stop ⏸', 'exit', 'stop', 'start', 'play']

while True :

    menu = input('''please choose 
1.play ▶
2.stop ⏸
3.exit 
:   ''')

    if menu.lower() == 'play' or menu.lower() == 'play ▶' :

        if stop == False :

            print('music is already playing ❗❗')

        else :

            print('playing the music ♪ ...')

            stop = False
        

    elif menu.lower() == 'stop' or menu.lower() == 'stop ⏸' :

        if stop :

            print('music is already stopped ❗❗')

        else :

            stop = True

            print('music stopped')

    elif menu.lower() == 'exit' :

        print('exiting the platform')

        break

    else :

        print(' i dont understand this command 🤔')