## :fontawesome-solid-code-branch: Parte Común

### Identificador

Un identificador es la cadena de caracteres (letras, números y guiones bajos) que se utiliza para dar un nombre único a variables, constantes, funciones, bloques funcionales o programas dentro del código.
Para que un identificador sea válido según la norma, debe cumplir con las siguientes reglas sintácticas:

- Comienzo: Debe empezar siempre por una letra o por un carácter de subrayado (_). Nunca puede empezar con un número.
- Composición: Solo puede contener letras (A-Z, a-z), números (0-9) y guiones bajos (_). No se permiten espacios ni caracteres especiales (como signos de interrogación o guiones medios).
- Mayúsculas y minúsculas: El estándar IEC 61131-3 no distingue entre mayúsculas y minúsculas (case-insensitive). Por lo tanto, MiContador, micontador y MICONTADOR se consideran el mismo identificador.
- Restricciones: No puede coincidir con ninguna palabra reservada del lenguaje (como IF, THEN, VAR, INT, etc.).

### Declarar una Variable

Para crear una variable escribir su declaración siguiendo la siguiente sintaxis:

```iecst
Identificador [AT %Localización]: Type [:= ValorInicial];
```

1. **Identificador** (obligatorio). Es el nombre único de la variable dentro de su ámbito (scope).
2. **Localización** (opcional). La localización o **Ubicación Directa** establece la zona y la posición de memoria en la que se situará la variable.
    - Modificador de localización `AT`.
    - Dirección.

        ```iecst
        %[Área] [Tamaño] [Dirección]
        ```

        - `%`: prefijo de ubicación.
        - Área: `I` para entradas, `Q` para salidas y `M` para memoria interna (o de marcas).
        - Dirección:
            - Absoluta:

                ```iecst
                [Area][Tamaño][Dirección]
                ```

                - Tamaño [X/B/W/D/L]: prefijo que indica el tamaño de la variable (Bit/Byte/Palabra/Doble/Larga).
                - Dirección [palabra.bit]: posición de la variable en el área de memoria.

                ??? info "Ejemplo"
                    ```iecst
                    Pulsador AT %IX0.0: BOOL;
                    ```

            - Inespecificada: utilizando el carácter comodín `*`

                ??? info "Ejemplo"
                    ```iecst
                    Pulsador AT %*: BOOL;
                    ```

3. **Separador de tipo:** (obligatorio). Separa el nombre de la variable de su tipo.
4. **Tipo de dato**: Especifica principalmente el tamaño y el rango de la variable. Puede ser un tipo elemental (BOOL, INT, REAL, TIME,...), complejo (STRUCT, ENUM, ARRAY,...) o de usuario.
5. **Valor inicial**: Especifica el valor de la variable al iniciar el runtime. Si no se especifica tomará el valor predeterminado para ese tipo de variable.
6. **Delimitador ;** (obligatorio). Terminador de instrucción.

### Variables localizadas y mapeo dinámico

Las **variables localizadas**, son aquellas a las que se le asigna explícitamente una dirección de memoria.

- Situar las instancias de estas variables en las correspondientes imágenes de E/S (*Process Image*) mediante el uso del modificador `AT`, las convierte en **variables de entrada y salida**.
- Si no se hiciera, el compilador situaría estas variables en el **espacio de memoria interna** (marcas) y no se generarían las correspondientes instancias de E/S, por lo que no podrían vincularse (*mapping*) a canales físicos de E/S del controlador.
- El símbolo `%` es el prefijo de ubicación directa.
- Las letras `I` y `Q` indican el área de memoria (entrada/salida).
- El símbolo `*` es un comodín que indica que estas variables tienen un **mapeo dinámico**, lo que implica que será el compilador el encargado de asignarle una dirección (`palabra.bit`) concreta.

### Ámbito de una Variable

El bloque de declaración determina el ámbito y el alcance de la variable especificando quién y cómo puede acceder a la variable o parámetro.

1. `VAR ... END_VAR`: variables locales, internas al POU. Únicamente accesibles dentro del POU en el que se declaran.
2. `VAR_INPUT ... END_VAR`: parámetros de entrada. Pueden ser escritos desde el exterior.
3. `VAR_OUTPUT ... END_VAR`: parámetros de salida. Pueden ser leídos desde el exterior.
4. `VAR_IN_OUT ... END_VAR`: parámetros de entrada/salida por referencia. Punteros a variables externas que pueden leerse y escribirse dentro del POU.
5. `VAR_GLOBAL ... END_VAR`: variables globales (GVL). Accesibles desde cualquier POU del proyecto.
6. `VAR_STAT ... END_VAR`: variables estáticas. Variables locales que conservan su valor entre ciclos de ejecución.
7. `VAR_PERSISTENT ... END_VAR`: variables persistentes. Variables que conservan su valor incluso tras la pérdida de alimentación.
