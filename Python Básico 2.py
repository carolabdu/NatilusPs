n = int(input('Digite um número:'))


def primo(k):
    for x in range(2, int(k ** (1 / 2)) + 1):
        if k % x == 0: return False
    return True


for y in range(n, 1, -1):
    if primo(y) == True and n % y == 0:
        print('Maior divisor primo de', n, 'é', y)
        break
