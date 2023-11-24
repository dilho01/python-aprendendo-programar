i2 = s2 = s3 = 0
print('-'*28)
print(' CADASTRE UMA NOVA PESSOA')
print('-'*28)
while True:
    i = int(input('Idade:'))
    if i >= 18:
        i2 += 1
    s = ' '
    while s not in 'MF':
        s = str(input('Sexo[M/F]:')).strip().upper()[0]
    if s == 'M':
        s2 += 1
    elif s == 'F':
        if i < 20:
            s3 += 1
    print('-'*28)
    c = ' '
    while c not in 'NS':
        c = str(input(' quer continuar [N/S]:')).strip().upper()[0]
    print('-'*28)
    if c == 'N':
        break
print(f'o total de pessoas com 18 anos {i2}\nao todo temos {s2} homens cadastrados\ne temos {s3} mulheres menor 20')
