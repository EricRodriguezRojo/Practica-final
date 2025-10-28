import csv

class RegistroHorario:
    def __init__(self, empleado: str, dia: str, entrada: int, salida: int):
        print(f"Creando registro para {empleado} el {dia} de {entrada}h a {salida}h")
        self.empleado = empleado
        self.dia = dia
        self.entrada = entrada
        self.salida = salida

    def duracion(self) -> int:
        horas = self.salida - self.entrada
        print(f"{self.empleado} trabajó {horas} horas el {self.dia}")
        return horas

registros = []

print("Leyendo archivo 'horarios.csv'...")
with open('horarios.csv', newline='', encoding='utf-8') as f:
    lector = csv.reader(f, delimiter=';', quotechar='"')
    for fila in lector:
        if not fila:
            continue
        nombre, dia, h_entrada, h_salida = fila
        entrada = int(h_entrada)
        salida = int(h_salida)
        registro = RegistroHorario(nombre, dia, entrada, salida)
        registros.append(registro)

print(f"\nSe han leído {len(registros)} registros del archivo.")

empleados_por_dia = {}

for r in registros:
    if r.dia not in empleados_por_dia:
        empleados_por_dia[r.dia] = set()
    empleados_por_dia[r.dia].add(r.empleado)

print("\nEmpleados por día:")
for dia, empleados in empleados_por_dia.items():
    print(f"{dia}: {empleados}")

if "Lunes" in empleados_por_dia and "Viernes" in empleados_por_dia:
    en_dos_dias = empleados_por_dia["Lunes"] & empleados_por_dia["Viernes"]
    print("\nEmpleados que trabajaron Lunes y Viernes:", en_dos_dias)

    with open("en_dos_dias.csv", "w", newline='', encoding='utf-8') as f:
        escritor = csv.writer(f, delimiter=';')
        escritor.writerow(["Empleado"])
        for e in en_dos_dias:
            escritor.writerow([e])
    print("Archivo 'en_dos_dias.csv' generado correctamente.")

horas_totales = {}

for r in registros:
    horas_totales.setdefault(r.empleado, 0)
    horas_totales[r.empleado] += r.duracion()

with open("resumen_horarios.csv", "w", newline='', encoding="utf-8") as f:
    escritor = csv.writer(f, delimiter=';')
    escritor.writerow(["Empleado", "Horas_totales"])
    for emp, total in horas_totales.items():
        escritor.writerow([emp, total])

print("\nArchivo 'resumen_horarios.csv' generado correctamente.")

hora_referencia = 8
madrugadores = {r.empleado for r in registros if r.entrada < hora_referencia}

with open("madrugadores.csv", "w", newline='', encoding='utf-8') as f:
    escritor = csv.writer(f, delimiter=';')
    escritor.writerow(["Empleado", "Hora_entrada"])
    for r in registros:
        if r.empleado in madrugadores and r.entrada < hora_referencia:
            escritor.writerow([r.empleado, r.entrada])

print(f"\nEmpleados madrugadores (antes de las {hora_referencia}h): {madrugadores}")

if "Sábado" in empleados_por_dia and "Domingo" in empleados_por_dia:
    exclusivos = empleados_por_dia["Sábado"] - empleados_por_dia["Domingo"]
    print("\nEmpleados que trabajaron solo el sábado:", exclusivos)

resumen = {}

for r in registros:
    if r.empleado not in resumen:
        resumen[r.empleado] = {"dias": set(), "horas": 0}
    resumen[r.empleado]["dias"].add(r.dia)
    resumen[r.empleado]["horas"] += r.duracion()

with open("resumen_semanal.csv", "w", newline='', encoding="utf-8") as f:
    escritor = csv.writer(f, delimiter=';')
    escritor.writerow(["Empleado", "Dias_trabajados", "Horas_totales"])
    for emp, datos in resumen.items():
        escritor.writerow([emp, len(datos["dias"]), datos["horas"]])

print("\nArchivo 'resumen_semanal.csv' generado correctamente.")

empleados_6h = set()
for emp in {r.empleado for r in registros}:
    registros_emp = [r for r in registros if r.empleado == emp]
    if all(r.duracion() >= 6 for r in registros_emp):
        empleados_6h.add(emp)

print("\nEmpleados que trabajaron al menos 6h en todas sus jornadas:", empleados_6h)
