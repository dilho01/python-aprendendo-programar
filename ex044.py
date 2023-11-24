from datetime import date
print('''\033[31;40m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\033[m
\033[31;40m    alistamento militar!          \033[m
\033[31;40m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\033[m''')
i=int(input('qual o ani que vc nasceu?'))
c=date.today().year-i
c2=(18-c)+date.today().year
c3=date.today().year-i-18
if c>18:
    print('vc tem {} anos era para vc ter se alistado a {} anos atras'.format(c,c3))
elif c<18:
    print('vc tem {} anos e vai se alistaar no {} ano'.format(c,c2))
else:
    print('vc tem {} anos e precisa se alistar esse ano'.format(c))
