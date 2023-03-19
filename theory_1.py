def main():
    # Поиск и замена
    filename = input('Введите имя файла: ')
    if filename.endswith('.txt'):
        print('Это имя текстового файла.')
    elif filename.endswith('.py'):
        print('Это имя исходного файла Python')
    elif filename.endswith('.doc'):
        print('Это имя текстового редактора.')
    else:
        print('Неизвестный тип файла.')




if __name__ == '__main__':
    main()