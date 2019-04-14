import json
import re


def cargar_datos():
    with open("response.json", encoding="UTF-8") as file:
        arrayJson = json.load(file)

    return arrayJson


def cargar_datos2():
    with open("vacante.json", encoding="UTF-8") as file:
        arrayJson = json.load(file)

    return arrayJson


def edad(fecha):
    anio=fecha.split("-")[0]
    return int(anio)


def salario(sueldoDes, sueldoOf):
    dinero = [int(str(part.split(',')[0]) + str(part.split(',')[1])) for part in re.findall(r'(\d+,\d+)', sueldoDes)]
    dinero2 = [int(str(part.split(',')[0]) + str(part.split(',')[1])) for part in re.findall(r'(\d+,\d+)', sueldoOf)]

    if dinero[1] > dinero2[1]:
        return int(0)

    if dinero[1] <= dinero2[1] | dinero[0] >= dinero2[0]:
        return int(1)

    if (dinero[1] < dinero2[0]):
        return int(2)


print(salario("12,000 a 19,000", "17,000 a 20,000"))

arrayJson = cargar_datos()
info_plantilla=cargar_datos2()

for json2 in arrayJson:
    for json1 in info_plantilla:
        if json1['region_id'] == json2['region_id']:
            print('Id:', json2['id'])
            print("Region",json2["region_name"])
            print("Salario deseado",json2["current_salary"])
            print("Fecha nacimiento", json2["birthday"])
            print("Experiencia:")
            for trabajo in json2['experiences']:
                print("\t", trabajo['place'], "->", trabajo['job'])
            print()
            pass