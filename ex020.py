import math
a=float(input('digite o angulo:'))
se=math.sin(math.radians(a))
co=math.cos(math.radians(a))
ta=math.tan(math.radians(a))
print('o angulo e {:.2f} o seno e {:.2f} o cosno e {:.2f} e a tangemte e {:.2f}'.format(a,se,co,ta))