class Book :

    def __init__(self, title, author, year ) :

        self.title = title

        self.author = author

        self.year = year

list = []

while True :

    title_input = input('please enter the book name : ')

    author_input = input('please enter the writer name :')

    year_input = int(input('please enter the year that book has been writen : '))

    my_book = Book(title_input, author_input, year_input)

    list.append(my_book)

    continuing = input("do you want to add more book's to your list : ")

    if continuing.lower() == 'no' :

        print('quiting the program ...')

        break

for i in list :

    print(f'the book name is {i.title} and the writer name is {i.author} and it had been writen in {i.year}')