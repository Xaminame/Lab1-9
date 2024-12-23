try:
    f = open('exampl.txt','r')
    print(f.read())
except FileNotFoundError:
    print('Такого файла не существует')
