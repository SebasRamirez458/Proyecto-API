def obtener_datos_usuario():
    nombre_departamento = input("INGRESE EL NOMBRE DEL DEPARTAMENTO QUE DESEA CONSULTAR: ").upper()
    limite_registros = int(input("INGRESE EL LIMITE DE REGISTROS QUE DESEA CONSULTAR: "))
    datos_ingresados = [limite_registros,nombre_departamento]
    return datos_ingresados

def mostrar_datos(datos):
    print(datos)


    