p2 = p3 = i2 = me = 0
i3 = ' '
print('-='*25)
print('              LOJA SUPER BARATÃO')
print('-='*25)
while True:
    i = str(input('nome do produto:'))
    p = float(input('preço: R$'))
    i2 += 1
    p2 += p
    if p > 1000:
        p3 += 1
    if i2 == 1 or p < me:
        me = p
        i3 = i
    print('-='*25)
    c = ' '
    while c not in 'SN':
        c = str(input('quer continuar? [S/N]')).strip().upper()[0]
    print('-='*25)
    if c == 'N':
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'o total da compra foi {p2}\n temos {p3} compra que curta mais de 1000.00R$')
print(f'o protudu mais barato e {i3} e o preso e {me}')
