a = str(input('digite um expreção:'))
l = []
for s in a:
    if s == '(':
        l.append('(')
    elif s == ')':
        if len(l) > 0:
            l.pop()
        else:
            l.append(')')
            break
if len(l) == 0:
    print('sua expreção estar valida')
else:
    print('sua expreção estar erada')
