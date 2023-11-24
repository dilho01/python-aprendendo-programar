from time import sleep
print('''\033[40m==================================\033[m
\033[40m              MÉDIA               \033[m
\033[40m==================================\033[m''')
n1=float(input('primeira nota:'))
n2=float(input('segunda nota:'))
c=(n1+n2)/2
print('calculando....')
sleep(2)
print('seu nota no primeiro bimestre foi {:.1f} e no segundo {:.1f}, sua média e {:.1f}'.format(n1,n2,c))
if c<5:
    print('\033[31mreprovado!\033[m')
elif 7>c>=5:
    print('\033[33mrecuperação\033[m')
else:
    print('\033[32maprovado\033[m')