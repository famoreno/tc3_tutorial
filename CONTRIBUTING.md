# 📖 Guía de Estilo y Convenciones del Tutorial

Para mantener la consistencia visual y técnica en toda la documentación de TwinCAT 3, todos los archivos Markdown deben seguir estas convenciones.

---

## 📐 Arquitectura de Contenidos y Taxonomía de Archivos

### 1. Organización Semántica

El tutorial divide el aprendizaje en cuatro pilares fundamentales:

- **🏛️ Fundamentos (`/fundamentos/`):** Explica el **¿por qué?**. Conceptos teóricos, normativas (IEC 61131-3, IEC 60848) y paradigmas de arquitectura.
- **🛠️️ Procedimientos (`/procedimientos/`):** Explica el **¿cómo?**. Guías metodológicas y de flujo de trabajo (*Workflow*) en la herramienta TwinCAT 3.
- **🔬 Ejemplos (`/ejemplos/`):** Casos prácticos acotados que muestran un problema resuelto (*Aprender haciendo*).
- **📋 Prácticas (`/practicas/`):** Retos y proyectos completos estructurados para consolidar el conocimiento.

---

### 2. Convención de Nombres (`kebab-case`)

- **Nombres de archivos y carpetas:** Utilizar siempre minúsculas y guiones medios.
    - *Correcto:* `contenidos/ejemplos/carro-basico/step-by-step.md`
    - *Incorrecto:* `contenidos/ejemplos/carro_basico/step_by_step.md`
- **Estructura de Ejemplos:** Cada subsección debe organizarse dentro de su propia carpeta:
    - `index.md` ➔ Ficha técnica, descripción y especificación del problema.
    - `step-by-step.md` ➔ Guía de desarrollo e implementación paso a paso.
- **Imágenes:** Guardar en la subcarpeta `./img/` local en minusculas y separadas por guiones.
    - *Ejemplo:* `![Configurar E/S](./img/io-attach-variable.png){ width="400px" }`

---

## 🖱️ Interacciones de Interfaz y Ratón

- **Clic izquierdo:** Usar **negrita** sin recargar con iconos.
    - *Sintaxis:* Hacer clic en **Activate Configuration**.
- **Clic derecho:** Usar el icono `:material-mouse-right-click:` o la acción explícita.
    - *Sintaxis:* Hacer clic derecho en :material-mouse-right-click: **POUs** > **Add** > **POU...**
- **Doble clic:** Indicar explícitamente en **negrita**.
    - *Sintaxis:* Hacer doble clic en **MAIN (PRG)**.
- **Rutas de menús:** Usar el separador `>` con elementos en **negrita**.
    - *Sintaxis:* **TwinCAT** > **Restart TwinCAT (Config Mode)**.

---

## ⌨️ Teclado y Botones

- **Atajos de teclado:** Utilizar exclusivamente la extensión `++tecla++`.
    - *Sintaxis:* Pulsar ++f5++ para iniciar el Runtime o ++ctrl+shift+f2++ para compilar.
- **Botones de la interfaz:** Nombre exacto en **negrita**.
    - *Sintaxis:* Pulsar **OK** o seleccionar **Attach Variable**.

---

## 💻 Nomenclatura Técnica (TwinCAT / IEC 61131-3)

- **Variables y funciones:** Siempre en código en línea `` ` variable ` ``.
    - *Ejemplo:* La variable `bStart` activa el temporizador `tonDelay`.
- **Bloques de código:** Usar identificador `iecst` para código Structured Text.
- **Rutas de árbol del proyecto:** Usar **negrita** y separadores `>`.
    - *Ejemplo:* **PLC** > **[Proyecto]** > **POUs** > **MAIN**.

---

## 🖼️ Imágenes y Capturas de Pantalla

- **Ancho explícito:** Especificar siempre el ancho en píxeles mediante `{ width="400px" }` o unidades % para evitar desproporciones.
- **Texto alternativo:** Incluir siempre un título descriptivo en el `alt` de la imagen.
    - *Sintaxis:* `![Pantalla de enlace de variables](./img/ejemplo.png){ width="500px" }`

---

## 🚧 Archivos en Desarrollo

- Si una página o sección está incompleta, debe incluirse el snippet correspondiente:
    - *Página completa:* `--8<-- "includes/avisos.md:en-construccion"`
    - *Paso puntual:* `--8<-- "includes/avisos.md:paso-incompleto"`

---

## 🔤 Capitalización de Títulos (Title Case)

Todos los títulos del tutorial (`#`, `##`, `###`) deben redactarse en **Title Case** (todas las palabras con mayúscula inicial), con excepción de preposiciones, artículos y conjunciones cortas (a menos que inicien el título).

### Reglas básicas

- **Llevan Mayúscula Inicial:** Sustantivos, verbos, adjetivos, adverbios y pronombres.
- **Se mantienen en minúscula:** Artículos (*el, la, los, un*), preposiciones (*de, en, con, para, por*) y conjunciones (*y, o, e*).
- **Acrónimos y términos de TwinCAT:** Respetar sus mayúsculas/minúsculas oficiales (p. ej., `PLC`, `POU`, `GVL`, `HMI`, `Structured Text`).

### Ejemplos

- ❌ `# pasos para el mapeo de entradas y salidas`
- ❌ `# Pasos Para El Mapeo De Entradas Y Salidas`
- ✅ `# Pasos para el Mapeo de Entradas y Salidas`

- ❌ `## configuración de la comunicación ADS en TwinCAT`
- ✅ `## Configuración de la Comunicación ADS en TwinCAT`

---

---

### 🖼️ Iconos e Imágenes Incrustados en Texto (Inline)

Para insertar pequeños iconos de la interfaz o símbolos de TwinCAT dentro de una frase (por ejemplo, el indicador de enlace de una variable), se debe utilizar la clase CSS `.inline-icon`. Esto garantiza que la imagen se alinee correctamente con el texto y no herede sombras ni bordes del tema.

- **Sintaxis en Markdown:**
  `![Texto alternativo](./img/nombre-icono.png){ .inline-icon }`

- **Ejemplo de uso:**
  En el árbol del proyecto, la variable vinculada mostrará el símbolo ![Indicador de variable enlazada](./img/io-variable-linked-symbol.png){ .inline-icon } justo a la izquierda del nombre.

- **Configuración requerida en `docs/stylesheets/extra.css`:**
    ```css
        img.inline-icon {
            width: 16px;
            height: auto;
            border: none !important;
            background: transparent !important;
            box-shadow: none !important;
            vertical-align: middle;
            margin: 0 2px;
            padding: 0;
        }
    ```

  ---
