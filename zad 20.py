def angmiesiace(x):
    miesiace = {
        'styczeń': 'January',
        'luty': 'February',
        'marzec': 'March', 
        'kwiecień': 'April',
        'maj': 'May', 
        'czerwiec': 'June',
        'lipiec': 'July',
        'sierpień': 'August',
        'wrzesień': 'September',
        'październik': 'October',
        'listopad': 'November',
        'grudzień': 'December'
    }
    if x not in miesiace.keys():
     print('Nieprawidłowa nazwa miesiąca')
    else:
     print(miesiace[x])


angmiesiace('sierpień')