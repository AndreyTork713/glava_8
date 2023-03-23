# функция получает от пользователя данные
# и возвращает имя для входа в систему
def get_login_name(first, last, idnumber):

    # берем первые три буквы имени
    set1 = first[0:3]

    # берем первые три буквы фамилии
    set2 = last[0:3]

    # берем последние три цифры ID
    set3 = idnumber[-3:]

    # собираем воедино набор символов
    login_name = set1 + set2 + set3

    # возвращаем
    return login_name


def valid_password(password):
    # Назначить булевым переменным начальное значение False
    correct_length = False
    has_uppercase = False
    has_lowercase = False
    has_digit = False
    is_valid = False

    # Приступить к валидации.
    if len(password) >= 7:
        correct_length = True

    # Проанализировать каждый символ и установить
    # соответствующий флаг
    for ch in password:
        if ch.isupper():
            has_uppercase = True
        if ch.islower():
            has_lowercase = True
        if ch.isdigit():
            has_digit = True

    if correct_length and has_digit and has_uppercase and has_lowercase:
        is_valid = True
    else:
        is_valid = False

    return is_valid