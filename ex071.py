a = c = s = 0
while True:
    a = int(input('digite um numero:'))
    if a == 999:
        break
    s += a
    c += 1
print(f'você digitou {c} e a soma dos valores são {s}')
