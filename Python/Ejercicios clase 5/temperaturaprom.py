sumtemp = 0
for dia in range(1,8):
    temp = float(input('ingrese la temperatura del dia: '))
    sumtemp = sumtemp + temp   
promedio = sumtemp / 7 
print (promedio)