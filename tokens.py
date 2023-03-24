def main():


    # Строковые литералы подлежащие лексемизации
    str1 = 'one two three four'
    str2 = '10:20:30:40'
    str3 = 'a/b/c/d/e/f'

    # Вывести на экран лексемы в каждом строковом литерале
    display_tokens(str1, ' ')
    display_tokens(str2, ':')
    display_tokens(str3, '/')


def display_tokens(data, delimiter):
    tokens = data.split(delimiter)
    for item in tokens:
        print(f'Лексема: {item}')


if __name__ == '__main__':
    main()
