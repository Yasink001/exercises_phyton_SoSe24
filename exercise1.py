def cagr_berechnung(AK,EK,t):
    i = (EK/AK)**(1/t)-1
    return i

print(cagr_berechnung(100, 700, 30))

def cagr_berechnung(AK, EK, t):
    AK_abs = abs(AK)
    t_abs = abs(t)
    cagr = ((EK/AK_abs)**(1/t)-1)
    return cagr

    print(cagr_berechnung(100, 700, 30))
    
    AK = 120
    cagr = cagr_berechnung(100, 700, 30)
    
    AK = 100
    t = 30
    cagr = cagr_berechnung(100, 700, 30)
    EK = AK * (1 + cagr)**t
    
    print(EK)
  
