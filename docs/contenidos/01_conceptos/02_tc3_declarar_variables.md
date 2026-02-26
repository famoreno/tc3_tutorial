## 🏷️ Declaración de variables

!!! tip "Recomendación"
    Se recomienda utilizar la convención **[CamelCase](https://es.wikipedia.org/wiki/Camel_case)** para declarar las variables.

    Como convención adicional, añadiremos un prefijo `i_` para aquellas variables que se declaren en la zona de entrada y `o_` para las de la zona de salida.

- Independientemente del lenguaje utilizado para implementar el código, las variables se declaran de la misma manera.
- Las variables se declaran en la caja superior de la ventana del bloque funcional creado.
- La sintaxis para la declaración de variables es la siguiente:

```pascal
<NombreVariable> : <tipo> [:=<ValorInicial>]
```

Los tipos de datos más utilizados son los siguientes:

| Tipo de dato        | Descripción |
|---------------------|-------------|
| `BOOL`              | Variable booleana/binaria. Solo puede valer `TRUE` o `FALSE`. |
| `INT`               | Entero con signo de 16 bits (-32768 a 32767). |
| `UINT`              | Entero sin signo de 16 bits (0 a 65535). |
| `FLOAT`             | Número real en coma flotante (32 bits). Permite decimales. |
| `TIME`              | Tipo de dato para representar tiempos o duraciones. |
| `R_TRIG`            | Bloque de función para detectar flanco ascendente (`FALSE` → `TRUE`). |
| `TON`               | Temporizador a la conexión (retardo a la activación). Activa la salida tras un tiempo. |
| `ARRAY[x..y] OF ...`| Conjunto de variables del mismo tipo indexadas entre `x` e `y`. |

!!! question "Ejemplo"
    ```pascal
    // bool
    Pulsador: BOOL;
    LuzAmarilla: BOOL := TRUE;

    // enteros con y sin signo
    Altura: INT;
    Contador: UINT;
    UnidadesSolicitadas: UINT := 10;

    // números reales
    TpoSegundos: FLOAT := 1.2;

    // tiempo
    TiempoEspera: TIME := T#2s;
    TiempoRestante: TIME;

    // bloques funcionales
    Flanco_Pulsador: R_TRIG; // detector de flanco (estándar)
    Temporizador: TON; // temporizador (estándar)
    Coordinador: FB_Coordinador; // bloque funcional definido por el usuario

    // arrays
    Ocupado: ARRAY[0..3] OF BOOL; // array de cuatro elementos de tipo BOOL; acceso con []
    ```

- La sintaxis de los valores posibles es la siguiente:
    - **Variables booleanas:** `TRUE`, `FALSE`.
    - **Variables enteras:** `0`, `1`, etc.
    - **Variables reales:** `0.1`, `2.3`, etc.
    - **Variables de tiempo:** `T#<tiempo>` donde `<tiempo>` debe ser del estilo `<numero><unidad>`, siendo `<unidad>` escogido de `{s, ms}`.

        !!! question "Ejemplo"
            `T#2s` (dos segundos)
            
            `T#500ms` (quinientos milisegundos).
    
    - El acceso a los *arrays* se hace con el índice entre corchetes. 
        
        !!! question "Ejemplo"
            `Ocupado[1] := TRUE;`

- Ejemplos de llamadas a los bloques funcionales estándar:
    
    !!! question "Ejemplo"
        **Detector de flanco:** Se activa su salida `Flanco_Pulsador.Q` cuando la señal `boton` pasa de `FALSE` a `TRUE`.
            ```st
                Flanco_Pulsador(CLK := boton);
            ```
    
    !!! question "Ejemplo"
        **Temporizador:** Se activa cuando la señal `start` pasa a `TRUE` y activa su salida `Temporizador.Q` tras pasar 10s.
        ```st
            Temporizador(IN:=start, PT:=T#10s);
        ```


Las variables en TC3 se declaran dentro de los ámbitos existentes en el POU correspondiente: **locales**, **entrada** y **salida**.

### Variables locales

```pascal
FUNCTIONAL_BLOCK FB_Estacion
VAR
    Contador: UINT;
END_VAR
```

Las variables declaradas aquí se pueden utilizar dentro del POU pero **no** pueden tomar valores de fuera del POU ni se pueden acceder desde fuera del POU.

### Variables de entrada

```pascal
FUNCTIONAL_BLOCK FB_Estacion
VAR_INPUT
    TiempoEntrada: TIME;
    TiempoSalida: TIME := T#2s;
END_VAR
```

Las variables declaradas aquí **deben** ser especificadas al llamar al **FB** (a no ser que se les de un valor por defecto).

!!! warning "Importante"
    No especificarlas en la llamada produce un error de compilación.

### Variables de salida

```pascal
FUNCTIONAL_BLOCK FB_Estacion
VAR_OUTPUT
    LuzAmarilla: BOOL;
    LuzVerde: BOOL;
END_VAR
```

Las variables declaradas aquí pueden ser accedidas desde fuera del **FB** (por ejemplo, desde otro **FB** que llama a este, o desde el programa `MAIN`).

```pascal
PROGRAM MAIN
VAR
    Estacion: FB_Estacion
    LuzAmarillaEstacion: BOOL;
END_VAR
------------------
LuzAmarillaEstacion := Estacion.LuzAmarilla; // esto es válido
```

!!! warning "Importante"
    Querer acceder a una variable de un **FB** que no ha sido declarada como salida produce un error de compilación.

### Variables de entrada y salida

```pascal
FUNCTIONAL_BLOCK FB_Estacion
VAR_IN_OUT
    Contador: UINT;
END_VAR
```

Este ámbito no aparece por defecto al crear un **FB** pero puede ser añadido simplemente escribiendo la sección `VAR_IN_OUT ... END_VAR`.

Las variables declaradas aquí deben tomar un valor como entrada al **FB** y su valor final tras cada ciclo puede ser accedido desde fuera del **FB**.

Combina las condiciones de los ámbitos de entrada y salida.

- En un programa (ej. `MAIN`) sólo disponemos del ámbito `VAR`.
- En un **FB**, además del ámbito `VAR`, disponemos de los ámbitos `VAR_INPUT` y `VAR_OUTPUT`.

---

### Variables vinculadas a la E/S

Recuerda que la memoria del PLC está estructurada en tres secciones: la **imagen de entrada**, la **imagen de salida** y la **zona de marcas**.

#### Zona de marcas

Aquí se guardarán aquellas variables que son internas al programa y no van a ser vinculadas con terminales de entrada y salida.

Las variables declaradas con la siguiente sintaxis se guardan en la zona de marcas:

```pascal
VAR
    Pulsador: BOOL;
    Contador: UINT;
    Lampara: BOOL;
END_VAR
```

#### Imagen de entrada

Aquí se guardarán las variables que queremos vincular a las **entradas físicas** del sistema.

Su sintaxis añade `AT %I*` antes de la definición del tipo:

```pascal
VAR
    i_Pulsador AT %I*: BOOL;
END_VAR
```

!!! warning "Importante"
    En nuestro trabajo usaremos la convención de añadir un prefijo `i_` delante de estas variables.

#### Imagen de salida

Aquí se guardarán las variables que queremos vincular a las **salidas físicas** del sistema.

Su sintaxis añade `AT %Q*` antes de la definición del tipo:

```pascal
VAR
    o_Lampara AT %Q*: BOOL;
END_VAR
```

!!! warning "Importante"
    En nuestro trabajo usaremos la convención de añadir un prefijo `o_` delante de estas variables.

!!! warning "Importante"
    Declarar una variable en la imagen de entrada o salida es **independiente** de que sean entradas o salidas del bloque funcional.
    
    Estas declaraciones son completamente correctas.

    ```pascal
    VAR_INPUT
        Pulsador AT %I*: BOOL;
        LamparaAmarilla AT %Q*: BOOL;
        TiempoEspera: TIME;
    END_VAR

    VAR
        LamparaMarcha AT %Q*: BOOL;
    END_VAR

    VAR_OUTPUT
        PresenciaPale AT %I*: BOOL;
    END_VAR
    ```

