a=str(input('digite um frase:')).lower().strip()
print('a letra A aparece {} vezesga\nprimeira letra A aprecena posiçao {}'.format(a.count('a'),a.find('a')+1))
print('a letra A aparece na ultimo vez na posiçao {}'.format(a.rfind('a')+1))