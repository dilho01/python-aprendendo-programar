l = []
while True:
    a = int(input('digite um numero:'))
    l.append(a)
    a2 = ' '
    while a2 not in 'NS':
        a2 = str(input('quer continuar?[S/N]')).strip().upper()
    if a2 == 'N':
        break
print(f'a lista copleta e: {l}\nos numeros pares são:', end=' [')
for i, v in enumerate(l):
    if v % 2 == 0:
        print(f'{v},', end='')
print(']', '\nos numeros impares são: [', end='')
for i ,v in enumerate(l):
    if v % 2 != 0:
        print(f'{v},', end='')
print(']')
