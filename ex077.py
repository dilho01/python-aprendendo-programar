a = ('zero', 'um', 'dois', 'três', ' quatro', 'cinco',
     'seis', 'sete', ' oito', 'nove', 'dez', ' onze', 'doze',
     'treze', 'cartoze', 'quinze', 'dezesseis', ' dezessete',
     'dezoito', 'dezenove', 'vinte')

while True:
    c = int(input('digite um numero entre 20 e 0:'))
    if 0 < c > 20:
        print('tente novamnete.',end=' ')
    else:
        print(f'vc digitou o numero {a[c]}')
        f = ' '
        while f not in 'SN':
            f = str(input('quer continuar [S/N]')).strip().upper()[0]
        if f == 'N':
            break
