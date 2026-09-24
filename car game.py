l = '' 

started = False

breaking_string = 'quit'

commands = ['help' , 'start' , 'stop' , 'quit']

while l.lower() != breaking_string :

    l = input('... ')

    if l.lower() == 'help' :

        print('''start ------> starting the car
stop ------> stoping the car 
quit ------> quiting the game ''')

    if l.lower() == 'start' :

        if started :

            print('car is already started !')

        else :

            started = True

            print('you are turning the car on ...')

    if l.lower() == 'stop':

        if not started :

            print('car is already stopped !')

        else :

            started = False

            print('you are turning the car of ...')

    if l.lower() not in commands :

        print("i don't under stand this command !")

    if l.lower() == 'quit' :

        print('quiting the game ...')

        break