import math 
def promedio(num):
    """
    Calcula el promedio de una lista de números.
    Verifica y elimina NaNs en los datos.

    Parametros
    ---------
    vals: lista
         lista con los numeros

    Retorna
    -------
    promedio: float
          el promedio de los numeros
    """
    num = [x for x in num if not isnan(x)]
    if not num:
        return float('nan')
    promedio = sum(num) / len(num)
    return promedio

#import estadistica_descriptiva as ed
#num= [1,2,3,4,5,float('nan')]
#p = ed.promedio(num)
#print(p)

def moda(lista):
    categoria_unica = [] #crear una categoria unica
    for i in lista: 
        if i not in categoria_unica:
            categoria_unica.append(i) #parte 1
            
    frecuencia = [] 
    for categoria in categoria_unica:
        contador = 0
        for i in lista:
            if i  == categoria:
                contador = +1
                frecuencia.append(contador) #parte 2
                
    max_frecuencia= 0
    for categoria in frecuencia:
        if frecuencia[categoria]> max_frecuencia:
            max_frecuencia = frecuencia[categoria]
            
    moda= []
    for categoria in frecuencia:
        if frecuencias[categoria] == max_frecuencia:
            modas.append(categoria)
            
    if len(moda) == len(categoria_unica): #si todas las frecuencias son iguales
        return None
    if len(moda) == 1: #SI SOLO HAY UNA
        return moda[0]
        return moda
        
def covarianza(vals_x,vals_y):
    """
    Calcula la covarianza de dos listas de números.
    Detecta y elimina valores NaN

    Parametros
    ---------------
    vals_x, vals_y: lista
               lista con los dos atributos
    Retorna
    -------
    covarianza: float
          covarianza de los atributos(excluyendo NaNs)
    """
    #Revisar que no sean NaNs, eliminar valores Nans
    x = []
    y = []
    for i in range (len(vals_x)):
        if math.isfinite(vals_x[i]) & math.isfinite(vals_y[i]):
            x.append(vals_x[i])
            y.append(vals_y[i])
            
    p_x = promedio(x)
    p_y= promedio(y)

    tt=[]
    for xv, yv in zip(x,y):
        tt.append((xv - p_x) * (yv - py))
        
    covarianza = sum(tt) / len(tt)
    
    return covarianza


def correlacion (vals_x,vals_y):
    """
    Calcula la covarianza de dos listas de números.
    Detecta y elimina valores NaN

    Parametros
    ---------------
    vals_x, vals_y: lista
               lista con los dos atributos
    Retorna
    -------
    covarianza: float
          covarianza de los atributos(excluyendo NaNs)
    """
    #Revisar que no sean NaNs, eliminar valores Nans
    x = []
    y = []
    for i in range (len(vals_x)):
        if math.isfinite(vals_x[i]) & math.isfinite(vals_y[i]):
            x.append(vals_x[i])
            y.append(vals_y[i])
            r_xy = covarianza(x,y) /math.sqrt(varianza(x) * varianza(y)):
            return r_xy 
