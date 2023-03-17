def main():
    name = 'Кармен'
    print('Имя:', name)
    name += ' Браун'
    print('Теперь имя:', name)
    try:
        name[1] = 'p'
    except:
        print('Так делать нельзя! Строка НЕМУТИРУЕМЫЙ тип данных.')



if __name__ == '__main__':
    main()