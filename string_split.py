def main():

    my_string = 'Один два три четыре'

    word_list = my_string.split()
    print(word_list)

    months = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
    month = ''
    date_string = '31/05/1970'
    date_list = date_string.split('/')
    def choice_month(months, date_list):
        for item in range(0, len(months)):
            if date_list[1] == months[item]:
                return months[item]

    print(f'день: {date_list[0]}, месяц: {choice_month(months, date_list)}, год: {date_list[2]}')


if __name__ == '__main__':
    main()