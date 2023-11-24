from datetime import date
a=int(input('vou analizar seu ano:'))
if a==0:
    a=date.today().year
if a%4==00 and a%100==0 or a%400==0:
    print('0 ano de {} e bissexto'.format(a))
else:
    print('o ano de {} nao e bissexto'.format(a))