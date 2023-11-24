from datetime import date
me=0
ma=0
for c in range(1,8):
    a2=int(input('em que ano {} nasceu:'.format(c)))
    a=date.today().year-a2
    if a >18 :
        me += 1
    else:
        ma += 1
print('tem {} pessoas menores de idade\ne tem {} pessoas maiores de idade'.format(me,ma))
