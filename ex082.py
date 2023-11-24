a = ('gosto', 'lindo', 'foda', 'mais pika',
     'o melhor de todos', 'lutador', 'vencerdor')
for n in a:
    print(f'\n{n.upper():-^15}',end='  nas palavas temos as vogas ')
    for t in n:
        if t.lower() in 'aeiou':
            print(f'{t}',end=' ')