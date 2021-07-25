def maior_primo(n):
    teste1 = 2
    while True:
        while (not n % teste1 == 0) and teste1 <= 11:
            teste1 += 1
            if teste1 == 11:
                return n
        n -=1
