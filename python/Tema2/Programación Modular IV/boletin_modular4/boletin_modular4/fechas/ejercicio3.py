'''
3. Write a Python program to convert seconds to day, hour, minutes and seconds.
'''

'''
((h1*60)+(m1*3600)+(s1*216000))
'''

def pasar_tiempo(s):
    tf=0
    opcion = input("Intraduce a que tipo de dato quieres convertir los segundos: d(dias),h(horas),m(minutos),s(segundos):")
    
    if opcion == "d":
        tf = s/(24*60**2)
    elif opcion == "h":
        tf =s/60**2
    elif opcion == "m":
        tf =s/60
    elif opcion == "s":
        tf = s
        
    return tf

print(pasar_tiempo(455423545454545456878))