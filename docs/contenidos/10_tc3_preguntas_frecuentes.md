# Preguntas frecuentes

## Declaración de variables

### ¿Debo declarar en `VAR_INPUT` una variable que quiero conectar a una entrada física del sistema? (equivalentemente para `VAR_OUPUT`)

No necesariamente. Hay que tener clara la distinción entre variables que se declaran en **la zona de entrada o salida** en un POU y las variables de entrada/salida de un **FB**.

- Las primeras son las que **podrán ser vinculadas** con las entradas y salidas físicas del sistema y se declaran de esta forma:
    - `<nombre_variable> AT %I* : <tipo>;` (zona de entrada de la memoria)
    - `<nombre_variable> AT %Q* : <tipo>;` (zona de salida de la memoria).
- Las segundas se declaran en los ámbitos `VAR_INPUT` (entradas) o `VAR_OUTPUT` (salidas) y se refieren a las entradas y salidas *software* del **FB**.

!!! info "Nota"
    Es totalmente compatible declarar variables en la zona de entrada y salida tanto en los ámbitos `VAR_INPUT` como `VAR_OUTPUT`.

!!! tip "Ejemplo de declaraciones válidas"
    ```pascal
    VAR_INPUT
        VariableZonaEntrada AT %I*: BOOL;
        VariableZonaSalida AT %Q*: BOOL;
        VariableZonaMarcas : BOOL;
    END_VAR

    VAR_OUTPUT
        VariableZonaEntrada AT %I*: BOOL;
        VariableZonaSalida AT %Q*: BOOL;
        VariableZonaMarcas : BOOL;
    END_VAR
    ```

### ¿En qué ámbitos debo declarar mis variables: `VAR`, `VAR_INPUT` o `VAR_OUTPUT`?

Si imaginamos un **FB** como una caja negra que realiza una funcionalidad, esta caja negra tiene una serie de entradas que permite introducir información en el **FB** para operar con ella y tiene una serie de salidas para sacar información del **FB** al exterior, además de un conjunto de variables de uso interno.

!!! info "`VAR_INPUT`"
    Deberemos declarar en `VAR_INPUT` todas aquellas variables que queramos que se les pueda dar valor **desde fuera del FB**. Por ejemplo, en un **FB** (`Ejemplo: FB_Ejemplo`) que use una variable de tiempo para regir una transición (`TiempoTransicion`), podemos declarar dicha variable como `VAR_INPUT` y así permitir que se le dé un valor concreto al llamar al FB: `Ejemplo(TiempoTransicion:=T#1s);`.

!!! info "`VAR_OUTPUT`"
    De manera similar, deberemos declarar en `VAR_OUTPUT` todas aquellas variables que queramos que el valor que se le da dentro del **FB** **pueda ser accedido** desde fuera del mismo. Para el `Ejemplo: FB_Ejemplo` anterior, debemos declarar como `VAR_OUTPUT` una variable `VariableSalida` que toma valor dentro del **FB** si queremos que desde fuera se pueda usar: `Variable := Ejemplo.VariableSalida;`.

!!! info "`VAR`"
    El resto de variables que son de uso interno del **FB** deben ser declaradas en `VAR`.

## Visualización

### ¿Cómo se debe especificar las variables asociadas a los elementos de la visualización?

Se deben especificar **con su ruta completa**. Por ejemplo, para una variable `VariableEjemplo` declarada dentro de un **FB** llamado `Estacion` que ha sido instanciado en el programa `MAIN`, deberemos usar `MAIN.Estacion.VariableEjemplo`.

### ¿Qué elementos deben ser diseñados como botones?

Deberán comportarse como botones **todos los elementos** excepto las etiquetas y los rectángulos de introducción y muestra de datos (numéricos o de tiempo):

- Los elementos vinculados a las **salidas** del sistema, para poder actuar sobre la estación al pulsarlos. Deben ser de tipo `TOGGLE` para poder actuar en distintas salidas a la vez.
- Los elementos vinculados a las **entradas** del sistema, que se asocian a los **pulsadores** (serán de tipo `TAP`) y **conmutadores** (serán de tipo `TOGGLE`). Con esto se permite **simular** la pulsación y conmutación de los mismos **cuando no estemos trabajando con la estación**. Esto nos permitirá hacer evolucionar nuestro programa `SFC` cuando sea suficiente.
- Los elementos vinculados a las **entradas** del sistema que se asocian a los **sensores** (tipo `TOGGLE`). Aunque no tiene sentido físico que podamos modificar el valor de un sensor desde un panel de visualización (el sensor refleja el estado de la realidad, no lo podemos modificar de forma artificial), definir estos elementos como botones nos permitirá **hacer evolucionar** nuestro programa `SFC` en simulación sin la estación. En algún momento nuestro programa estará en una etapa esperando a que un sensor se active. Si no tenemos la estación, podremos usar este botón para simular que el sensor se ha activado y así pasar a la siguiente etapa. Esto agiliza enormemente el proceso de depuración.

!!! info "Nota"
    En todos los casos, los botones **también** deberán cambiar de color con el cambio de estado de la variable asociada.

### ¿Qué representa el número que aparece al lado de los indicadores de los bits del código de palé?

Es la **conversión numérica** (decimal) de los bits del código de palé. Los lenguajes de programación de PLC son especialmente sencillos para acceder a las variables a nivel de bit. Para realizar la conversión bastaría con asignar las variables booleanas correspondientes a cada bit a los bits de la variable numérica.

!!! tip "Ejemplo"
    ```pascal
    VAR
        VariableNumerica : UINT;
        VariableBit0 : BOOL := TRUE;
        VariableBit1 : BOOL;
        VariableBit2 : BOOL := TRUE;
    END_VAR

    ----- 
    
    VariableNumerica.0 := VariableBit0; // acceso al bit 0
    VariableNumerica.1 := VariableBit1; // acceso al bit 1
    VariableNumerica.2 := VariableBit2; // acceso al bit 2

    // VariableNumerica toma el valor decimal 5 (101 en binario)
    ```

## Hardware

### ¿Qué son los bits del código de palé?

Mira la descripción de la cinta transportadora en la **descripción funcional** del sistema FMS200.
