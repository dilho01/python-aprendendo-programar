a=str(input('digite um frase:')).strip().upper()
p=a.split()
j=''.join(a)
i=''
for c in range(len(j),-1,-1-1):
    i += j
print('o inverso de {} e {}'.format(j,i))
if i==j:
    print('essa frase e um palindromo')
else:
    print(' essa frase não e um palindromo')