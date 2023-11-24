l = []
while True:
    n = int(input('digite um valor:'))
    if n not in l:
        l.append(n)
        print('valor digitado com sucesso...')
    else:
        print(f'o numero {n} foi digitado')
    a = ' '
    while a not in 'NS':
        a = str(input('quer continuar?[S/N]')).strip().upper()[0]
    print('='*25)
    if a == 'N':
        break
l.sort()
print(f'a lista digita foi {l}')
