def main():
    # Напечатать девять строк, увеличивающихся по длине.
    for count in range(1, 10):
        print('Z' * count)

    # Напечатать девять строк, уменьшающихся по длине.
    for count in range(8, 0, -1):
        print('Z' * count)


if __name__ == '__main__':
    main()