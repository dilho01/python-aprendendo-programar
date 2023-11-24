l = ('lapis', 1.70,
     'borracha', 2,
     'caedemo', 40.50,
     'estojio', 25,
     'tranfiridor', 32.20,
     'compasso', 9.99,
     'mochila', 120,
     'caneta', 3.20,
     'livros', 39.40)
print('-'*40)
print(f'{"LISTAGEM DE PREÇO":.^40}')
print('-'*40)
for n in range(len(l)):
     if n % 2 == 0:
          print(f'{l[n]:.<30}',end=' ')
     else:
          print(f'R$ {l[n]}')
print('-'*40)
