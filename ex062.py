c=str(input('Informe seu sexo: [F/M]:')).strip().upper()[0]
while c not in 'MmfF':
    c=str(input('Dados invalidos.por favor, Informe seu sexo: [F/M]:')).strip().upper()[0]
print('sexo {} registrado com sucesso'.format(c))