from time import sleep
nu=int(input('digite um numero:'))
print('''escolha sua opiçao:
[1] converte para \033[4:36mBINARIO\033[m
[2] converter para \033[4:36mOCTAL\033[m
[3] converte para \033[4:36mHEXADECIAL\033[m''')
o=int(input('qual e sua opiçao?'))
print('\033[1:36mcalculando....\033[m')
sleep(2)
if o==1:
    print('seu numero foi convertido para \033[4:36mBINARIO\033[m \033[32m{}'.format(bin(nu)[2:]))
elif o==2:
    print('seu numero foi convertido para \033[4:36mOCTAL\033[m \033[32m{}'.format(oct(nu)[2:]))
elif o==3:
    print('seu numero foi convertido para \033[4:36mHEXADECIAL\033[m \033[32m{}'.format(hex(nu)[2:]))
else:
    print(' \033[31mnao foi possivel fazer a converçao\033[m')