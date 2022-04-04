while True:
    number = int(input('Entre um número:'))
    if number == 0:
        break
    if number % 2 == 0:
        print('O número', number, 'está correto')
    else:
        print('O número', number, 'está errado')