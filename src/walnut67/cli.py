from constants import wal_67


def main():
    while True:
        print(''.join([wal_67[let.lower()] for let in input('Enter text to convert to Walnut67 encoding: ')]))


if __name__ == '__main__':
    main()
