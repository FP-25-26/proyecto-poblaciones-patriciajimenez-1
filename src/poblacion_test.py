from poblacion import *

def test_lee_poblaciones(datos):
    print("*** Test lee poblaciones ***")
    print(f"Se han leído {len(datos)} registros.")
    print("Mostrando los tres primeros registros")
    for d in datos[:3]:
        print(d)
    print("Mostrando los tres últimos registros")
    for d in datos[-3:]:
        print(d)


if __name__ == "__main__":
    datos = lee_poblaciones('./data/population.csv')
    test_lee_poblaciones(datos)