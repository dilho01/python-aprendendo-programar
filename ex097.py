from datetime import date
a = dict()
a['nome'] = str(input('Nome:'))
a['ano'] = int(input('Ano de nasimneto:'))
a['c'] = int(input('Carteira de trabalho:(0 não tem)'))
if a['c'] != 0:
    a['ca'] = int(input('Ano da contratação:'))
    a['s'] = float(input('Salario:'))
print('=-'*30)
print(f'O seu nome e {a["nome"]}')
c = date.today().year - a['ano']
print(f'Você tem {c} anos')
if a['c'] != 0:
    print(f'ctps e : {a["c"]}')
    print(f'Você foi contrtado {a["ca"]}')
    print(f'Tem o salario {a["s"]}')
    print(f'Você vai se aposentar {c+(a["ca"]+35)-date.today().year}')
