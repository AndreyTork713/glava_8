import login


def main():

    # Получить от пользователя пароль
    password = input('Введите свой пароль: ')
    while not login.valid_password(password):
        print('Этот пароль недопустим!')
        password = input('Введите свой пароль: ')
    print('Это допустимый пароль.')


if __name__ == '__main__':
    main()

