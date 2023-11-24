l = []
for a in range(0,5):
    a2 = int(input('digite um valor:'))
    if a == 0 or a2 > l[-1]:
        l.append(a2)
        print('foi adisonado no final da lista')
    else:
        p = 0
        while p < len(l):
            if a2 <= l[p]:
                l.insert(p,a2)
                print(f'foi adisonado na posição {p}')
                break
            p += 1
print(l)
