"""
Fase 5 - Evaluación Final POA
Curso: Fundamentos de Programación
Problema 5: Cálculo de horas trabajadas semanalmente y clasificación de jornada.

Autor: Leandro Chará Zambrano
"""

UMBRAL_HORAS = 40

# Matriz de datos:
# [Nombre del recurso, Lunes, Martes, Miércoles, Jueves, Viernes]
equipo_trabajo = [
    ["Ana García", 8, 8, 8, 8, 8],
    ["Luis Pérez", 9, 9, 8, 9, 8],
    ["Marta López", 7, 7, 8, 7, 6],
    ["Carlos Ruiz", 10, 8, 9, 8, 9]
]


def calcular_total_horas(horas_diarias):
    """
    Calcula el total de horas trabajadas en la semana.

    Parámetros:
        horas_diarias (list): Lista con las horas trabajadas de lunes a viernes.

    Retorna:
        int: Total de horas trabajadas durante la semana.
    """
    total = 0

    for hora in horas_diarias:
        total += hora

    return total


def clasificar_jornada(total_horas):
    """
    Clasifica la jornada laboral según el total de horas semanales.

    Parámetros:
        total_horas (int): Total de horas trabajadas en la semana.

    Retorna:
        str: Clasificación de la jornada laboral.
    """
    if total_horas > UMBRAL_HORAS:
        return "Sobretiempo"
    elif total_horas == UMBRAL_HORAS:
        return "Horario Estándar"
    else:
        return "Horario Inferior"


def generar_informe(matriz_recursos):
    """
    Genera el informe final de horas trabajadas por cada recurso.

    Parámetros:
        matriz_recursos (list): Matriz con nombres y horas trabajadas.
    """
    print("=" * 60)
    print("INFORME DE HORAS TRABAJADAS SEMANALMENTE")
    print("=" * 60)
    print(f"{'Recurso':<20}{'Total de horas':<20}{'Clasificación'}")
    print("-" * 60)

    for recurso in matriz_recursos:
        nombre = recurso[0]
        horas_diarias = recurso[1:]

        total_horas = calcular_total_horas(horas_diarias)
        clasificacion = clasificar_jornada(total_horas)

        print(f"{nombre:<20}{total_horas:<20}{clasificacion}")


if __name__ == "__main__":
    generar_informe(equipo_trabajo)