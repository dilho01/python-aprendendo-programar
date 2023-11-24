a=str(input('digite seu nome:')).strip()
n=a.split()
print('muito prazer em conhecer vc {}\nseu primeiro nome e {}\nseu ultimo e {} '.format(a,n[0],n[len(n)-1]))
