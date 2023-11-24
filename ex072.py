while True:
    a = int(input('qual tabuada você quer ver?'))
    if a < 0:
        break
    print('-'*20)
    print(f"{a}x1={a*1}\n{a}x2={a*2}\n{a}x3={a*3}\n{a}x4={a*4}\n{a}x5={a*5}\n{a}x6={a*6}\n"
      f"{a}x7={a*7}\n{a}x8={a*8}\n{a}x9={a*9}\n{a}x10={a*10}")
    print('-'*20)