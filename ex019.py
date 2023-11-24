'''co=float(input('comprimento do catedo oposto:'))
ca=float(input('compirmento do cadeto adijasente:'))
hi=(co**2+ca**2)**(1/2)
print('a hipotenusa vai medi {:.2f}'.format(hi))'''
from math import hypot
co=float(input('comprimento do catedo oposto:'))
ca=float(input('comprimento do catedo adiasente:'))
print('a hipotenusa vai ser {;.2f}'.format(hypot(co,ca)))