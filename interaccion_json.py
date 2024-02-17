import json

def cargar_datos(archivo):
    with open(archivo, 'r') as f:
        datos = json.load(f)
    return datos

def guardar_datos(archivo, datos):
    with open(archivo, 'w') as f:
        json.dump(datos, f, indent=4)

def main():
    archivo = 'datos.json'

    try:
        datos = cargar_datos(archivo)
        print("Datos cargados exitosamente:")
        print(datos)
    except FileNotFoundError:
        print(f"No se encontró el archivo {archivo}. Se creará uno nuevo.")
        datos = {}

    # Interacción con los datos
    print("\nInteractúa con los datos:")
    accion = input("¿Qué acción deseas realizar? (leer/escribir/salir): ").lower()

    while accion != 'salir':
        if accion == 'leer':
            clave = input("Ingresa la clave que deseas leer: ")
            valor = datos.get(clave, "La clave no existe")
            print(f"Valor: {valor}")
        elif accion == 'escribir':
            clave = input("Ingresa la clave: ")
            valor = input("Ingresa el valor: ")
            datos[clave] = valor
            guardar_datos(archivo, datos)
            print("Datos guardados exitosamente.")
        else:
            print("Acción no válida.")

        accion = input("\n¿Qué acción deseas realizar? (leer/escribir/salir): ").lower()

    print("¡Hasta luego!")

if __name__ == "__main__":
    main()
