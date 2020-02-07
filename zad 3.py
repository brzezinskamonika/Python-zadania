def kmmile(value, unit):
 odleglosc = float(value)

 if unit == 'km':
  x=odleglosc/1.609
  print("Ta wartosc w milach wynosi " + str(x) + " mi")
 elif unit == 'mi':
  z=odleglosc*1.609
  print("Ta wartosc w kilometrach wynosi " + str(z) + " km")
 else:
  print("Nieprawidlowa wartosc lub nieobslugiwana jednostka, wprowadź jednostke km lub mi")
     

#Przykład zastosowania - sprawdzamy ile to jest 100 km w milach:         
kmmile(100,'km')
#A teraz ile jedna mila ma kilometrów 
kmmile(1,'mi')
