options =  [ 'red 🔴', 'blue🔵', 'green🟢', 'red', 'blue', 'green']

while True :

    color = input('please choose between these colors (red 🔴, blue🔵, green🟢) : ')

    if color.lower() == 'green' or color.lower() == 'green🟢' :

        print('you won 🥳')

        break 

    if color.lower() not in options :

        print('you can just choose between red 🔴, blue🔵, green🟢 !')


    else :

        print(''' you choose the wrong color 😕 
try again🙃''')
