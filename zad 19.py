def iloscdni(x):
    miesiace = {
        'styczeń': '31',
        'luty': '29',
        'marzec': '31',
        'kwiecień': '30',
        'maj': '31',
        'czerwiec': '30',
        'lipiec': '31',
        'sierpień': '31',
        'wrzesień': '30',
        'październik': '31',
        'listopad': '30',
        'grudzień': '31'
    }
    if x not in miesiace.keys():
     print('Nieprawidłowa nazwa miesiąca')
    else:
     print(miesiace[x])


iloscdni('sierpień')