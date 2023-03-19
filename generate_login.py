import login

def main():

    first = input('Введите имя студента: ')
    last = input('Введите фамилию студента: ')
    idnumber = input('Введите ID студента: ')

    print('Получите идентификатор для входа в систему: \n')
    print(login.get_login_name(first, last, idnumber))


if __name__ == '__main__':
    main()