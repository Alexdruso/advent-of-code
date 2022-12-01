if __name__=='__main__':
    with open('data/data.txt') as f:
        data = map(lambda elf: elf.split('\n'), f.read().split('\n\n'))
        data = list(map(lambda elf: list(map(int, elf)), data))

    print(f'The answer to part 1 is {max(map(sum, data))}.')
    print(f'The answer to part 2 is {sum(sorted(list(map(sum, data)))[-3:])}')
