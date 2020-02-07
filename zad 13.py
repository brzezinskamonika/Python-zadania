def newton(n, k):
    if k == 0 or k == n:
        return 1
    elif k > n:
        return "Nieprawidlowa wartosc (wartość k musi być mniejsza bądź równa wartości n)"
    else:
        return newton(n-1,k-1) + newton(n-1,k)
    
#Przyklad uzycia:
print(newton(23,4))