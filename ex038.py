s=float(input('qual e seu salario:'))
a1=(s*10/100)+s
a2=(s*15/100)+s
if s>=1250:
    print('seu almento e de 10%, salario atual {:.2f}$'. format(a1))
else:
    print('seu almento e de 15%, salario atusl {:.2f}$'.format(a2))