import login

def main():

    first = input('Введите имя студента: ')
    last = input('Введите фамилию студента: ')
    idnumber = input('Введите ID студента: ')

    print('Получите идентификатор для входа в систему: \n')
    user_login = login.get_login_name(first, last, idnumber)
    print(f'Пароль пользователя для входа в систему: {user_login}')
    if login.valid_password(user_login):
        print('Пароль прошел валидацию и пригоден к использованию.')
    else:
        print('Пароль не прошел валидацию и не соответствует требованиям.')


if __name__ == '__main__':
    main()