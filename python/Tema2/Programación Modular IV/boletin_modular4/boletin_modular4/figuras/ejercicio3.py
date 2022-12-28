'''
3. Función tal que dadas las coordenadas de dos puntos en el plano devuelve su
distancia euclídea. Un punto en el plano tiene dos coordenadas (abscisa y
ordenada), por lo tanto, la entrada a esta función son cuatro valores reales.
'''

def calcula_euclidea(xp,yp,xq,yq):
    distancia = ((xq-xp)**2+(yq-yp)**2)**0.5
    return distancia

print(calcula_euclidea(4,7,8,2))