def main():
   text = 'Это было сто семь лет назад'

   if 'семь' in text:
       print('"Семь" найдено в тексте')
   else:
       print('"Семь" НЕнайдено в тексте')

   if 'семь' not in text:
       print('"Семь" НЕТ в тексте')
   else:
       print('"Семь" ЕСТЬ в тексте')

   user_string = input('Введите значение строковой переменной: ')
   print('Вот что обнаружено в отношении введенного строкового значения: ')
   if user_string.isalnum():
       print(f'{user_string} содержит буквы или цифры')
   if user_string.isdigit():
       print(f'{user_string} содержит только цифры')
   if user_string.isalpha():
       print(f'{user_string} содержит только буквы алфавита')
   if user_string.isspace():
       print(f'{user_string} содержит только пробельные символы')
   if user_string.islower():
       print(f'{user_string} содержит символы только нижнего регистра')
   if user_string.isupper():
       print(f'{user_string} содержит содержит символы только ВЕРХНЕГО регистра')


if __name__ == '__main__':
    main()