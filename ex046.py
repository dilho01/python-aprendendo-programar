from datetime import date
print(10*'\033[40m-','confederaação nacional de natação','-'*10,'\033[m')
a=int(input('quale o ano q vc nasceu?'))
c=date.today().year-a
if c<=9:
    print('vc tem {} anos e mirim '.format(c))
elif c<=14 and c>9:
    print('vc tem {} anos e infantil'.format(c))
elif c<=19 and c>14:
    print(' vc tem {} anos e junior'.format(c))
elif c<=25 and c>19:
    print('vc tem {} anos e sênio'.format(c))
else:
    print('vc tem {} anos e maste'.format(c))
