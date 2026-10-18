# Script de procesamiento de datos basico
def calcular_estadisticas(numeros):
    total = sum(numeros)
    promedio = total / len(numeros)
    return total, promedio

datos = [10, 20, 30, 40, 60]
suma, media = calcular_estadisticas(datos)

print(f"Resultados del analisis:")
print(f"Suma total: {suma}")
print(f"Promedio: {media}")