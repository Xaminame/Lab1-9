user = input('Введите текст: ')
with open('user_input.txt', 'a+') as file:
    z = file.write(user + '\n')
    c = file.read()
print(c)
