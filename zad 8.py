x = int(input('wpisz ilosc uzyskanych punktow:'))
procent = x/40*100 

if 0 <= procent <= 39:
    print('ndst')
elif 40 <= procent <= 49:
    print('dop')
elif 50 <= procent <= 69:
    print('dst')
elif 70 <= procent <= 84:
    print('db')
elif 85 <= procent <= 99:
    print('bdb')
elif procent == 100:
    print('cel')
else:
    print('wpisz poprawna liczbe punktow (0-40)')
