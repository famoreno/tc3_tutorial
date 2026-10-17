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
- **Estructura de Contenidos:**
    - `docs/index.md` ➔ Índice general del tutorial; sus secciones deben seguir la estructura y los nombres de `nav` en `mkdocs.yml`.
    - `docs/contenidos/{fundamentos,procedimientos,ejemplos,practicas}/index.md` ➔ Portada e introducción de cada sección principal.
    - `index.md` dentro de un tema o ejemplo ➔ Descripción, especificación y recursos del tema.
    - `step-by-step.md` ➔ Guía de implementación paso a paso, cuando corresponda.
    - `includes/` ➔ Fragmentos compartidos o incluidos en otras páginas; no son páginas independientes del sitio.
- **Navegación:** Con `navigation.indexes`, la portada `index.md` debe ser el primer elemento de su sección en `mkdocs.yml`. El título del grupo enlaza a esa portada y no se debe repetir como hijo.
- **Imágenes:** Guardar en la subcarpeta `./img/` local en minúsculas y separar las palabras con guiones.
    - **Capturas de pantalla:** usar la clase `.screenshot`; conserva el tamaño original si cabe y reduce proporcionalmente la imagen cuando supera el 90 % del contenedor.
    - **Otras imágenes:** usar `.image-centered` para centrarlas y mantener el ancho en píxeles indicado mediante `attr_list`.
    - **Iconos inline:** usar `.inline-icon`, que mantiene un tamaño fijo adecuado para el texto.
    - *Captura:* `![Ventana principal de TwinCAT XAE](./img/tc3-xae-main-window.png){ .screenshot }`
    - *Otra imagen:* `![Esquema del proyecto](./img/esquema.png){ width="400px" .image-centered }`

---

## 🖱️ Interacciones de Interfaz y Ratón

- **Clic izquierdo:** Usar el imperativo «haz clic» y poner el control en **negrita**. Se entiende que es clic izquierdo salvo que se indique lo contrario; no añadir icono.
    - *Sintaxis:* Haz clic en **Activate Configuration**.
- **Clic derecho:** Indicar explícitamente la acción y acompañarla, cuando ayude, con `:material-mouse-right-click:`.
    - *Sintaxis:* Haz clic derecho en :material-mouse-right-click: **POUs** > **Add** > **POU...**
- **Doble clic:** Usar el imperativo «haz doble clic» y poner el elemento en **negrita**. No hay un icono específico de doble clic en la colección Material configurada.
    - *Sintaxis:* Haz doble clic en **MAIN (PRG)**.
- **Rutas de menús:** Usar el separador `>` con elementos en **negrita**.
    - *Sintaxis:* **TwinCAT** > **Restart TwinCAT (Config Mode)**.

---

## ⌨️ Teclado y Botones

- **Atajos de teclado:** Utilizar exclusivamente la extensión `++tecla++`.
    - *Sintaxis:* Pulsar ++f5++ para iniciar el Runtime o ++ctrl+shift+f2++ para compilar.
- **Botones de la interfaz:** Nombre exacto en **negrita**.
    - *Sintaxis:* Pulsar **OK** o seleccionar **Attach Variable**.

---

## 🗣️ Voz y Tratamiento

- **Instrucciones directas:** dirigirse al lector de tú y usar el imperativo: *Haz clic*, *selecciona*, *comprueba*. Evitar el tratamiento de usted (*haga clic*, *seleccione*).
- **Explicaciones:** preferir la forma impersonal (*Para declarar una variable, se utiliza...*) o la primera persona del plural (*En esta sección configuramos...*), según el contexto.
- Mantener el mismo tratamiento dentro de cada sección y conservar sin cambios los nombres oficiales de controles y comandos.

---

## Ejemplos y Guías Paso a Paso

- **Índice de ejemplo (`index.md`):** presentar brevemente el objetivo y el funcionamiento del ejemplo, e incluir especificaciones, código o recursos cuando aporten contexto. Enlazar la guía de implementación en lugar de duplicar sus pasos.
- **Guía de implementación (`step-by-step.md`):** introducir el entorno y los objetivos antes del procedimiento. Organizar recorridos alternativos —por ejemplo, simulador, controlador o hardware externo— en secciones `###` y numerar sus pasos de forma independiente.
- **Pasos:** redactar las acciones en imperativo de tú, preferiblemente una acción principal por paso. Añadir junto al paso las advertencias, explicaciones y resultados que ayuden a completarlo o verificarlo.
- **Fragmentos incluidos (`includes/`):** comenzar cada fragmento con un título `###` descriptivo e insertarlo directamente en la guía anfitriona. No envolver el recorrido completo en un admonition colapsable; reservar los admonitions para información complementaria. Excluir los fragmentos de la navegación y validar el resultado desde la página que los incluye.
- **Admonitions:** usar tipos reconocidos por Material (`note`, `info`, `tip`, `warning`, `success`, entre otros). Para un tipo personalizado, definir también su estilo en CSS.
- Estas estructuras son una guía flexible: omitir secciones que no aporten al ejemplo y no inventar información solo para completar una plantilla.

---

## 💻 Nomenclatura Técnica (TwinCAT / IEC 61131-3)

- **Variables y funciones:** Siempre en código en línea `` ` variable ` ``.
    - *Ejemplo:* La variable `i_PulsadorMarcha` activa el temporizador `TemporizadorEspera`.
- **Bloques de código:** Usar identificador `iecst` para código Structured Text.
- **Ejemplos progresivos:** Mantener coherentes los identificadores de variables, estados y bloques entre sus declaraciones, el código y las explicaciones. Si un paso renombra un identificador, actualizar también sus referencias en los pasos posteriores.
- **Rutas de árbol del proyecto:** Usar **negrita** y separadores `>`.
    - *Ejemplo:* **PLC** > **[Proyecto]** > **POUs** > **MAIN**.

---

## 🔤 Abreviaturas Globales

Las abreviaturas compartidas por todo el sitio se definen una sola vez en `snippets/abreviaturas.md`. `pymdownx.snippets` las añade automáticamente a cada documento mediante `auto_append` en `mkdocs.yml`; no hay que repetir las definiciones en las páginas.

- **Sintaxis:** `*[PLC]: Controlador lógico programable.`
- **Al añadir una sigla:** mantener la lista alfabética y usar una definición breve y clara.
- **Al usarla:** escribir la sigla exactamente como aparece en la definición para que se muestre su descripción al pasar el cursor.

---

## 🖼️ Imágenes y Capturas de Pantalla

- **Proporción:** No deformar las imágenes. La clase `.screenshot` conserva su proporción original automáticamente.
- **Texto alternativo:** Incluir siempre un título descriptivo en el `alt` de la imagen.
    - *Sintaxis:* `![Pantalla de enlace de variables](./img/ejemplo.png){ width="500px" }`
- **Archivos SVG:** guardarlos siempre con saltos de línea `LF`. Lo fuerzan `.gitattributes` (`*.svg text eol=lf`) y `.editorconfig`; si un editor externo genera `CRLF`, convertir el archivo antes de hacer commit.

---

## 🚧 Archivos en Desarrollo

- Si una página o sección está incompleta, debe incluirse el snippet correspondiente:
    - *Página completa:* `--8<-- "snippets/avisos.md:documento-en-construccion"`
    - *Paso puntual:* `--8<-- "snippets/avisos.md:seccion-en-construccion"`

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

- **Configuración requerida en `docs/assets/stylesheets/extra.css`:**

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

## Iconos

- **Icono de una página:** declarar `icon:` en el frontmatter del Markdown, por ejemplo `icon: fontawesome/solid/screwdriver-wrench`. En las páginas índice, este icono también se usa en la entrada de navegación asociada.
- **Títulos y conceptos:** usar iconos Font Awesome Solid con la sintaxis `:fontawesome-solid-screwdriver-wrench:`.
- **Marcas y productos:** usar Simple Icons, por ejemplo `:simple-github:` o `:simple-googledrive:`.
- **Acciones e iconos de interfaz:** usar Material Design Icons, por ejemplo `:material-download:` o `:material-mouse-right-click:`.
- Evitar duplicar el icono de una página en el título de `nav` si ya procede de su frontmatter.

---

## ✅ Validación Local

Antes de proponer cambios, activar el entorno virtual del proyecto y compilar la documentación desde la raíz del repositorio:

```powershell
.\.venv\Scripts\Activate.ps1
mkdocs build
```

Si la compilación falla, corregir los errores antes de enviar la contribución. Para revisar los cambios en el navegador, ejecutar `mkdocs serve` en la misma terminal donde se activó `.venv`.

---

## ☑️ Progreso en Listas de Tareas

Las casillas Markdown (`- [ ]` / `- [x]`) son interactivas. `docs/assets/javascripts/tasklist.js` guarda su estado en `localStorage`, asociándolo a la ruta de la página y al texto de la tarea.

- El progreso permanece en el mismo navegador, perfil y origen del sitio; no se sincroniza entre dispositivos ni se comparte mediante Git.
- Si se cambia el texto de una tarea, puede dejar de coincidir con la marca guardada anteriormente. Al reordenar tareas con el mismo texto, se distinguen por su orden de aparición.
- Para validar el comportamiento, marcar una casilla, recargar la página y comprobar que conserva su estado.
- Borrar los datos locales del sitio en el navegador elimina también el progreso guardado.
