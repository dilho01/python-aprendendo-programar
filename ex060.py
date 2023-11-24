b = 0
b2 = 0
for c in range(1, 6):
    a = float(input('peso da {}ª pessoa:'.format(c)))
    if c == 1:
        b = a
        b2 = a
    else:
        if a > b:
            b = a
        if a < b2:
            b2 = a
print('o maior peso e {:.2f}kg\no menor peso e {:.2f}Kg'.format(b, b2))
