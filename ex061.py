i=0
m=0
mah=0
nv=''
mu=0
for c in range(1,5):
    print('------ {}ª pessoa ------'.format(c))
    a=str(input('Nome:')).strip()
    a2=int(input('Idade:'))
    a3=str(input('Sexo [M/F]:')).strip()
    i += a2
    if c==1 and a3 in 'Mm':
        mah=a2
        nv=a
    if a3 in 'Mm'and a2 > mah:
        mah=a2
        nv=a
    if a3 in 'fF' and a2 < 20:
        mu += 1
m = i /4
print('a media de idade do grupo e {:.2f}'.format(m))
print('O homen mais velho tem {} anos e se chama {}'.format(mah,nv))
print('as mulheres menores de 20 anos de idade são {}'.format(mu))