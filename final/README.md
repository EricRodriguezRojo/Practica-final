# MINI-CRM DE EVENTOS

## 1. DESCRIPCIÓN
Aplicación de consola en Python para **gestionar clientes, eventos y ventas** mediante archivos CSV.  
Permite:

- Cargar y listar datos de clientes, eventos y ventas.
- Dar de alta nuevos clientes.
- Filtrar ventas por rango de fechas.
- Generar métricas y estadísticas.
- Exportar informes resumidos.

La aplicación utiliza **Programación Orientada a Objetos (POO)**, **datetime** y colecciones (`list`, `dict`, `set`, `tuple`) para un manejo eficiente de datos.

---

## 2. FUNCIONALIDADES PRINCIPALES

### Menú interactivo
| Opción | Descripción |
|--------|-------------|
| Cargar CSV | Leer `clientes.csv`, `eventos.csv` y `ventas.csv` |
| Listar tablas | Mostrar datos cargados en formato legible |
| Alta de cliente | Añadir un nuevo cliente con validación de datos |
| Filtrar ventas | Consultar ventas dentro de un rango de fechas |
| Métricas y estadísticas | Ver ingresos, categorías y precios |
| Exportar informe | Generar informe resumido en CSV |
| Salir | Cierra la aplicación |

### Gestión de datos
- Lectura y escritura de CSV con manejo de errores (`FileNotFoundError`).
- Guardado incremental al añadir clientes.
- Exportación de informe resumen (`informe_resumen.csv`).

### Programación orientada a objetos
| Clase | Métodos destacados |
|-------|------------------|
| Cliente | `antiguedad_dias()`, `__str__`, `__repr__` |
| Evento | `dias_hasta_evento()`, `__str__`, `__repr__` |
| Venta | `__str__`, `__repr__` |

### Fechas y métricas
- Parseo de fechas con `datetime.strptime`.
- Cálculo de diferencias de días con `date.today()`.
- Estadísticas:
  - Ingresos totales.
  - Ingresos por evento (dict).
  - Categorías existentes (set).
  - Días hasta el próximo evento.
  - Tupla de precios `(min, max, media)`.

### Validaciones
- Formato de fecha (`YYYY-MM-DD`).
- Validación básica de email.
- Gestión de IDs para evitar colisiones.

---

## 3. USO DE LA APLICACIÓN

1. Clonar o descargar el repositorio.
2. Tener instalado Python 3.x.
3. Ejecutar desde la terminal:

```bash
python main.py
