def zmienskale(value, scale):
 temp = float(value)

 if scale == 'C':
  x=(temp*9/5)+32
  print("Ta wartosc w skali Fahrenheita wynosi " + str(x) + " stopni")
 elif scale == 'F':
  z=(temp-32)*(5/9)
  print("Ta wartosc w skali Celsjusza wynosi " + str(z) + " stopni")
 else:
  print("Nieprawidlowa wartosc lub nieobslugiwana skala, wprowadź skalę C lub F")
     

#Przykład zastosowania - sprawdzamy ile to jest 90 stopni Farenhaita w skali Celsjusza:         
zmienskale(90,'F')
#A teraz ile to jest 0 stopni Celsjusza w skali Farenhaita: 
zmienskale(0,'C')
#A teraz sprawdzamy co się dzieje, kiedy spróbujemy wprowadzić wartosc w skali Kelwina :)
zmienskale(115,'K')
