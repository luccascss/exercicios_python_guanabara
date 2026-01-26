# soma de números ímpares e múltiplos de três
s = 0
for c in range(0 + 1, 500 + 1):
    if c % 3 == 0 and c % 2 != 0:
        s = s + c
        print(c)
print('A soma desses números é {}'.format(s))



