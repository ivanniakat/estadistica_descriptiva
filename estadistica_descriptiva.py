import math

def promedios(vals):
    """
    Calcula el promedio de una lista.
    Filtra los datos para asegurar que sean números y no sean NaN.
    """
    num = [x for x in vals if isinstance(x, (int, float)) and not math.isnan(x)]
    if not num:
        return float('nan')
    return sum(num) / len(num)

def mediana(vals):
    """
    Encuentra el valor central de una lista de datos.
    Ordena los datos de menor a mayor y maneja casos pares e impares.
    """
    num = sorted([x for x in vals if isinstance(x, (int, float)) and not math.isnan(x)])
    n = len(num)
    if n == 0:
        return float('nan')
    
    mitad = n // 2
    if n % 2 == 0:
        return (num[mitad - 1] + num[mitad]) / 2
    else:
        return num[mitad]

def varianza(vals):
    """
    Calcula la varianza poblacional.
    Mide qué tan alejados están los datos del promedio al cuadrado.
    """
    mu = promedios(vals)
    num = [x for x in vals if isinstance(x, (int, float)) and not math.isnan(x)]
    if not num:
        return float('nan')
    
    suma_cuadrados = sum((x - mu)**2 for x in num)
    return suma_cuadrados / len(num)

def desviacion_estandar(vals):
    """
    Calcula la desviación estándar poblacional.
    Es la raíz cuadrada de la varianza y usa la misma unidad que los datos.
    """
    var = varianza(vals)
    if math.isnan(var):
        return float('nan')
    return math.sqrt(var)

def moda(lista):
    """
    Identifica el valor (numérico o texto) que más se repite en una lista.
    Si hay empate, devuelve una lista con las modas.
    """
    if not lista:
        return None
    
    conteo = {}
    for item in lista:
        conteo[item] = conteo.get(item, 0) + 1
    
    max_frecuencia = max(conteo.values())
    modas = [k for k, v in conteo.items() if v == max_frecuencia]
    
    return modas[0] if len(modas) == 1 else modas

def percentil(vals, p):
    """
    Calcula el percentil p (entre 0 y 100).
    Utiliza interpolación lineal para encontrar valores entre posiciones.
    """
    num = sorted([x for x in vals if isinstance(x, (int, float)) and not math.isnan(x)])
    if not num:
        return float('nan')
    
    n = len(num)
    pos = (n - 1) * (p / 100)
    idx_bajo = int(math.floor(pos))
    idx_alto = int(math.ceil(pos))
    
    if idx_bajo == idx_alto:
        return num[idx_bajo]
    
    # Interpolación
    d0 = num[idx_bajo] * (idx_alto - pos)
    d1 = num[idx_alto] * (pos - idx_bajo)
    return d0 + d1

def rango(vals):
    """
    Calcula la diferencia entre el valor máximo y el mínimo de la lista.
    """
    num = [x for x in vals if isinstance(x, (int, float)) and not math.isnan(x)]
    if not num:
        return float('nan')
    return max(num) - min(num)

def rango_intercuartil(vals):
    """
    Calcula el IQR (Rango Intercuartílico).
    Es la diferencia entre el percentil 75 (Q3) y el 25 (Q1).
    """
    q1 = percentil(vals, 25)
    q3 = percentil(vals, 75)
    return q3 - q1

def mad(vals):
    """
    Calcula la Desviación Absoluta Mediana (MAD).
    Es una medida de dispersión robusta frente a valores atípicos.
    """
    med = mediana(vals)
    num = [abs(x - med) for x in vals if isinstance(x, (int, float)) and not math.isnan(x)]
    return mediana(num)

def covarianza(vals_x, vals_y):
    """
    Mide la relación lineal entre dos variables X e Y.
    Filtra pares de datos donde ambos sean números válidos.
    """
    num_x = []
    num_y = []
    for x, y in zip(vals_x, vals_y):
        if (isinstance(x, (int, float)) and not math.isnan(x) and 
            isinstance(y, (int, float)) and not math.isnan(y)):
            num_x.append(x)
            num_y.append(y)
            
    if not num_x:
        return float('nan')
    
    mu_x = promedios(num_x)
    mu_y = promedios(num_y)
    
    suma = sum((xi - mu_x) * (yi - mu_y) for xi, yi in zip(num_x, num_y))
    return suma / len(num_x)

def correlacion(vals_x, vals_y):
    """
    Calcula el coeficiente de correlación de Pearson.
    Varía entre -1 y 1, indicando la fuerza de la relación lineal.
    """
    cov = covarianza(vals_x, vals_y)
    std_x = desviacion_estandar(vals_x)
    std_y = desviacion_estandar(vals_y)
    
    if math.isnan(cov) or std_x == 0 or std_y == 0:
        return float('nan')
        
    return cov / (std_x * std_y)
