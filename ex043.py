from time import sleep
print('\033[33m='*15)
print('vamos brincar')
print('='*15)
n=int(input('\033[mprimeiro numero:'))
n2=int(input('segundo numero:'))
print('\033[32mcalculando...\033[m')
sleep(2)
if n>n2:
    print('o primero numero e maior')
elif n2>n:
    print('o segundo numero e maior')
elif n==n2:
    print('os dois numero sao iguais')
