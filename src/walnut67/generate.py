from random import choice


def generate_wal_67() -> None:
    lets = [chr(o) for o in range(ord('a'), ord('z') + 1)]
    wal_67 = {}
    start = ord('a')
    while len(lets) > 0:
        let = choice(lets)
        wal_67[chr(start)] = let
        lets.remove(let)
        start += 1
    wal_67[' '] = ' '
    wal_67['.'] = '.'
    wal_67['!'] = '!'
    wal_67['?'] = '?'
    print(wal_67)


if __name__ == '__main__':
    generate_wal_67()
