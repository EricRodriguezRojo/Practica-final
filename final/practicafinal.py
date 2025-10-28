import csv
from datetime import datetime, date
import os

CARPETA_DATOS = "data"  # Carpeta donde están los CSVs

class Cliente:
    def __init__(self, id, nombre, email, fecha_alta):
        self.id = int(id)
        self.nombre = nombre
        self.email = email
        self.fecha_alta = datetime.strptime(fecha_alta, "%Y-%m-%d").date()

    def antiguedad_dias(self):
        print(f"Días desde alta de {self.nombre}: {(date.today() - self.fecha_alta).days}")
        return (date.today() - self.fecha_alta).days

    def __str__(self):
        return f"[{self.id}] {self.nombre} - {self.email} (alta: {self.fecha_alta})"


class Evento:
    def __init__(self, id, nombre, categoria, fecha, precio):
        self.id = int(id)
        self.nombre = nombre
        self.categoria = categoria
        self.fecha = datetime.strptime(fecha, "%Y-%m-%d").date()
        self.precio = float(precio)

    def dias_hasta_evento(self):
        dias = (self.fecha - date.today()).days
        print(f"Días hasta el evento {self.nombre}: {dias}")
        return dias

    def __str__(self):
        return f"[{self.id}] {self.nombre} ({self.categoria}) - {self.fecha} - {self.precio}€"


class Venta:
    def __init__(self, id_cliente, id_evento, fecha_venta):
        self.id_cliente = int(id_cliente)
        self.id_evento = int(id_evento)
        self.fecha_venta = datetime.strptime(fecha_venta, "%Y-%m-%d").date()

    def __str__(self):
        return f"Cliente {self.id_cliente} compró evento {self.id_evento} el {self.fecha_venta}"


def cargar_csv(ruta):
    datos = []
    try:
        with open(ruta, newline='', encoding="utf-8") as f:
            lector = csv.reader(f, delimiter=';')
            next(lector)
            for fila in lector:
                if fila:
                    datos.append(fila)
    except FileNotFoundError:
        print(f"No se encontró el archivo {ruta}")
    return datos


def guardar_cliente(cliente, ruta):
    os.makedirs(os.path.dirname(ruta), exist_ok=True)
    with open(ruta, 'a', newline='', encoding='utf-8') as f:
        escritor = csv.writer(f, delimiter=';')
        escritor.writerow([cliente.id, cliente.nombre, cliente.email, cliente.fecha_alta])
    print(f"Cliente '{cliente.nombre}' guardado en {ruta}")


def cargar_datos():
    clientes_data = cargar_csv(f"{CARPETA_DATOS}/clientes.csv")
    eventos_data = cargar_csv(f"{CARPETA_DATOS}/eventos.csv")
    ventas_data = cargar_csv(f"{CARPETA_DATOS}/ventas.csv")

    clientes = {int(c[0]): Cliente(*c) for c in clientes_data}
    eventos = {int(e[0]): Evento(*e) for e in eventos_data}
    ventas = [Venta(*v) for v in ventas_data]

    print("Datos cargados correctamente.")
    return clientes, eventos, ventas


def listar(tabla):
    print("\n=== LISTADO ===")
    if isinstance(tabla, dict):
        for obj in tabla.values():
            print(obj)
    else:
        for obj in tabla:
            print(obj)


def alta_cliente(clientes):
    print("\n--- Alta de nuevo cliente ---")
    nombre = input("Nombre: ")
    email = input("Email: ")
    fecha_alta = input("Fecha de alta (YYYY-MM-DD): ")

    try:
        datetime.strptime(fecha_alta, "%Y-%m-%d")
    except ValueError:
        print("Fecha inválida.")
        return

    nuevo_id = max(clientes.keys(), default=0) + 1
    nuevo_cliente = Cliente(nuevo_id, nombre, email, fecha_alta)
    clientes[nuevo_id] = nuevo_cliente

    guardar_cliente(nuevo_cliente, f"{CARPETA_DATOS}/clientes.csv")
    print(f"Cliente '{nombre}' añadido correctamente.")


def filtrar_ventas_por_rango(ventas):
    print("\n--- Filtrar ventas por rango de fechas ---")
    inicio = input("Fecha inicio (YYYY-MM-DD): ")
    fin = input("Fecha fin (YYYY-MM-DD): ")

    try:
        f1 = datetime.strptime(inicio, "%Y-%m-%d").date()
        f2 = datetime.strptime(fin, "%Y-%m-%d").date()
    except ValueError:
        print("Fechas inválidas.")
        return

    filtradas = [v for v in ventas if f1 <= v.fecha_venta <= f2]

    if not filtradas:
        print("No hay ventas en ese rango.")
    else:
        for v in filtradas:
            print(v)


def estadisticas(eventos, ventas):
    print("\n--- Estadísticas ---")
    ingresos_totales = 0
    ingresos_por_evento = {}
    categorias = set()

    for v in ventas:
        ev = eventos.get(v.id_evento)
        if ev:
            ingresos_totales += ev.precio
            ingresos_por_evento.setdefault(ev.nombre, 0)
            ingresos_por_evento[ev.nombre] += ev.precio
            categorias.add(ev.categoria)

    print(f"Ingresos totales: {ingresos_totales} €")
    print("Ingresos por evento:")
    for e, total in ingresos_por_evento.items():
        print(f" - {e}: {total} €")

    print("Categorías existentes:", categorias)

    proximos = [ev.dias_hasta_evento() for ev in eventos.values() if ev.dias_hasta_evento() >= 0]
    if proximos:
        print("Días hasta el evento más próximo:", min(proximos))

    precios = [ev.precio for ev in eventos.values()]
    if precios:
        print("Precios (min, max, media):", (min(precios), max(precios), sum(precios)/len(precios)))


def exportar_informe(eventos, ventas):
    print("\n--- Exportando informe ---")
    resumen = {}

    for v in ventas:
        ev = eventos.get(v.id_evento)
        if ev:
            resumen.setdefault(ev.nombre, {"cantidad": 0, "total": 0})
            resumen[ev.nombre]["cantidad"] += 1
            resumen[ev.nombre]["total"] += ev.precio

    os.makedirs(CARPETA_DATOS, exist_ok=True)
    with open(f"{CARPETA_DATOS}/informe_resumen.csv", "w", newline='', encoding='utf-8') as f:
        escritor = csv.writer(f, delimiter=';')
        escritor.writerow(["Evento", "Ventas", "Total (€)"])
        for nombre, datos in resumen.items():
            escritor.writerow([nombre, datos["cantidad"], datos["total"]])

    print(f"Informe generado en {CARPETA_DATOS}/informe_resumen.csv")


def menu():
    clientes, eventos, ventas = {}, {}, []

    while True:
        print(f"""
======== MINI CRM DE EVENTOS ========
1. Cargar datos CSV
2. Listar clientes
3. Listar eventos
4. Listar ventas
5. Alta de cliente
6. Filtrar ventas por rango de fechas
7. Estadísticas
8. Exportar informe
0. Salir
""")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            clientes, eventos, ventas = cargar_datos()
        elif opcion == "2":
            listar(clientes)
        elif opcion == "3":
            listar(eventos)
        elif opcion == "4":
            listar(ventas)
        elif opcion == "5":
            alta_cliente(clientes)
        elif opcion == "6":
            filtrar_ventas_por_rango(ventas)
        elif opcion == "7":
            estadisticas(eventos, ventas)
        elif opcion == "8":
            exportar_informe(eventos, ventas)
        elif opcion == "0":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    menu()
