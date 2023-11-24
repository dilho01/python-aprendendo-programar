s=0
c=0
for a in range(1,501,2):
    if  a %3==0:
     s+=a
     c+=1
print('a soma de todos os valores {} solicitados e {}'. format(c,s))
