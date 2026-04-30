## 💻 Interfaz de TwinCAT 3

La imagen muestra el entorno de desarrollo **TwinCAT 3 (TcXaeShell)** integrado en Visual Studio. A continuación se describen las principales zonas de la interfaz:

![Imagen](../images/01_conceptos/tc3_interfaz.png){width=800px}

---

### Resumen estructural

La interfaz de TC3 se divide conceptualmente en:

| Zona | Función |
|------|--------|
| Barra superior | Control del proyecto y del runtime |
| Solution Explorer | Organización estructural del proyecto |
| Editor central | Declaración de variables (superior) y código (inferior) |
| Panel de propiedades | Configuración detallada |
| Ventana inferior | Diagnóstico y mensajes |

---

### 1. Menús y barra de herramientas

En la zona superior encontramos:

#### Barra de menús

Incluye los menús clásicos:

- **File**
- **Edit**
- **View**
- **Project**
- **Build**
- **Debug**
- **TwinCAT**
- etc.

Desde aquí se gestionan acciones globales como compilar, activar configuración, depurar o configurar el runtime.

#### Barra de herramientas

Debajo del menú aparecen accesos rápidos a:

- Selección de configuración (*Debug / Release*)
- Selección del controlador (por ejemplo <Local>)
- Botones de **Activar configuración**, **Run Mode**, **Config Mode**, **Login**, **Start**, **Stop**
- Selección del proyecto activo
- Acceso rápido a escritura y forzado de variables, reset del controlador, etc.

---

### 2. Solution Explorer

Es el árbol estructural del proyecto.

Aquí se organizan:

- **Solution**
    - Proyecto PLC
    - POUs (Program Organization Units)
    - DUTs (Tipos de datos)
    - GVLs (Variables globales)
    - Visualizaciones
    - Referencias
    - I/O
    - Tasks

Permite:

- Crear nuevos bloques (FB, PRG, etc.)
- Añadir tipos de datos
- Configurar hardware
- Gestionar instancias

Es el centro de navegación del proyecto.

---

### 3. Editor central

Zona central del trabajo. Es el área donde se edita el código y los diagramas.

Puede mostrar distintos tipos de editores:

- **Structured Text (ST)**
- **Ladder (LD)**
- **FBD**
- **SFC**
- Visualizaciones

En la imagen se observan dos zonas diferenciadas dentro del mismo bloque:

#### Declaración de variables (parte superior)

Aquí se **definen**:

- `VAR_INPUT`
- `VAR_OUTPUT`
- `VAR`
- Enumeraciones
- Instancias de bloques
- Variables mapeadas a entradas/salidas físicas

Es la zona donde se define la interfaz y memoria del bloque.

---

#### Zona de código (parte inferior)

Aquí se **implementa** el código del bloque. En el ejemplo se visualiza un **diagrama SFC** con:

- Pasos (`S0`, `S1`, `S2`...)
- Transiciones
- Acciones asociadas
- Condiciones lógicas

Pero se puede programar en cualquier lenguaje de la norma IEC-61131-3.

---

### 4. Ventana de Propiedades

Muestra las propiedades del elemento seleccionado:

- Nombre
- Comentario
- Paso inicial
- Acciones asociadas
- Tiempos mínimos o máximos
- Configuración específica del objeto

Es contextual: cambia según lo que esté seleccionado (paso SFC, variable, bloque, etc.).

---

### 5. Zona inferior (Output / Error List)

En la parte inferior aparecen pestañas como:

- **Error List**
- **Output**
- Estado de compilación

Sirve para:

- Ver errores de compilación
- Advertencias
- Mensajes del sistema
- Información de activación
