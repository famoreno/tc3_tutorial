## ⤵️ Lenguaje SFC

### Reglas sintácticas

- Los nombres de las etapas en SFC (*Sequential Function Chart*) no pueden empezar por un número. Tampoco pueden tener espacios, puntos u otros caracteres especiales como eñes, interrogaciones, etc. Sí permite guiones bajos.
- **No puede haber dos etapas consecutivas ni dos transiciones consecutivas**. Hay que tener especial atención a esto cuando se produzcan bifurcaciones o saltos.

### Añadir etapa / transición
- Hacer **CD** sobre la **etapa** donde queramos introducir una nueva y seleccionar ***Add step-transition*** o ***Add step-transition after***, dependiendo de si queremos añadirla antes o después, respectivamente, de la etapa seleccionada.

!!! warning "Importante"
    Comprobar que no quedan dos etapas o dos transiciones consecutivas. En caso contrario, borrar aquello que no sirva (**CI** sobre él y pulsar *Supr*).

### Asociar acciones a etapas
#### Acción continua
Las acciones continuas se ejecutan de manera continuada mientras el sistema está en la etapa asociada. Esto nos va a permitir:

- **Activar una señal booleana** durante todo el tiempo que la etapa esté activa. 
- **Ejecutar una acción más compleja** asociada al **FB** de manera continua mientras la etapa esté activa.

El procedimiento para su creación es el siguiente:

- Hacer **CD** sobre la **etapa** a la que queramos asociar una acción no memorizada (o continua) y seleccionar ***Insert action association*** o ***Insert action association after***, dependiendo de si queremos insertarla antes o después de las ya existentes (si las hay).
- En la caja de la acción aparece en primer lugar el **modificador** (por defecto `N`, que significa **"No memorizada"**) y en segundo lugar el hueco donde debemos poner la acción a realizar.

##### Señal booleana
Si queremos activar una señal booleana, bastará con escribir su nombre en la caja de acción.
      
![Imagen](../images/01_conceptos/image%205.png){width=288px}

Existen varios tipos de modificadores de acciones:

| Código | Tipo | Descripción |
|--------|------|-------------|
| `N`    | **No memorizada (continua)** | **Se ejecuta/activa mientras la etapa esté activa.** |
| `R0`   | Reinicio | La acción se desactiva. |
| `S0`   | Activación | Se ejecuta cuando se activa la etapa y continúa activa aunque la etapa se desactive. |
| `L`    | Limitada | Se ejecuta cuando se activa la etapa y se desactiva cuando la etapa se desactiva o se alcanza el tiempo especificado. |
| `D`    | Retrasada | Se ejecuta un tiempo después de que se active la etapa y se desactiva cuando la etapa se desactiva. |
| `P`    | Pulsada | Se ejecuta dos veces: cuando se activa la etapa y una vez más en el ciclo siguiente. |
| `SD`   | Activación con retardo | Se activa aunque la etapa ya no esté activa. |
| `DS`   | Retardo de activación | Se activa solo si la etapa permanece activa. |
| `SL`   | Activación limitada | Activación con duración limitada. |

!!! warning "Importante"
    Usaremos, por defecto, las **acciones no memorizadas**, aunque se pueden usar las otras si tiene sentido para el proyecto.

##### Acción compleja

Si, por el contrario, lo que queremos asociar a esta etapa es una **acción compleja**, tendremos que realizar el siguiente procedimiento:

- Añadir una acción haciendo **CD** sobre el FB donde queremos usar la acción y seleccionar `Add > Action...`

    ![Imagen](../images/01_conceptos/add_action.png){width=400px}

- Especificar el nombre de la acción que queramos y seleccionar el lenguaje en el que la vamos a implementar.
    
    ![Imagen](../images/01_conceptos/select_lang_action.png){width=250px}

    !!! tip "Sugerencia"
        En nuestro trabajo tomaremos la convención de añadir el prefijo `a_` a las acciones que creemos de este modo.

- Escribir el código de la acción, como por ejemplo:

    ```st
    BLK();
    o_LamparaMarcha := (S0.x AND BLK.Q) OR NOT S0.x;
    ```

- Asociarlo a una etapa en la caja de acción contínua.

    ![Imagen](../images/01_conceptos/action_step.png){width=350px}

- A partir de este momento, el código de la acción se ejecutará de **manera continua** (en cada ciclo básico del PLC) mientras la etapa asociada esté activa.

#### Acción de entrada o salida
También podemos crear acciones con activación **a la entrada** o **a la salida** de una etapa. Estas acciones se implementan en cualquiera de los lenguajes de la norma y permiten realizar acciones que se ejecutan **solo una vez** durante la etapa, en lugar de hacerse de manera continua.

##### **A la entrada**
- Las acciones con activación a la **entrada** se ejecutan solo una vez **inmediatamente después** de entrar en la etapa donde se asocian. **Posteriormente** se comprueba si la condición de transición para pasar a la siguiente etapa es cierta o no.
- Normalmente usaremos estas acciones para inicializar variables memorizadas, actualizar contadores, etc.
- Para crear una de este tipo, hacer **CD** sobre la etapa donde la queremos asociar y seleccionar ***Add entry action***.
- Aparece un popup donde se nos pregunta por el nombre que le queremos poner y el lenguaje a utilizar. Se recomienda dejar el nombre por defecto (`S0_entry` en la figura) ya que nos indica en qué etapa está y de qué tipo es.
 
    ![Imagen](../images/01_conceptos/image%206.png){width=384px}

- En nuestros proyectos, **estas acciones siempre serán implementadas en `ST`**, pero podrían ser codificadas en cualquier otro lenguaje de la norma.
- Una vez creada, se representa en el programa `SFC` como un cuadrado con una **E** en la esquina inferior izquierda de la etapa.
 
    ![Imagen](../images/01_conceptos/image%207.png){width=288px}

##### **A la salida**
- Las acciones con activación **a la salida** se ejecutan solo una vez inmediatamente antes de pasar a la siguiente etapa. Esto implica que **antes** de que se ejecute esta acción, la condición de transición para pasar a la siguiente etapa **debe ser cierta**.
- Normalmente usaremos estas acciones para inicializar variables memorizadas, actualizar contadores, etc.
- Para crear una de este tipo, hacer **CD** sobre la etapa donde la queremos asociar y seleccionar ***Add exit action***.
- Aparece un *popup* donde se nos pregunta por el nombre que le queremos poner y el lenguaje a utilizar. Se recomienda dejar el nombre por defecto (`S0_exit` en la figura) ya que nos indica en qué etapa está y de qué tipo es.

    ![Imagen](../images/01_conceptos/image%208.png){width=384px}

    !!! warning "Importante" 
        En nuestros proyectos, **estas acciones siempre serán en `ST`**, pero podrían ser implementadas en cualquier otro lenguaje de la norma.

- Una vez creada, se representa en el programa `SFC` como un cuadrado con una **X** en la esquina inferior derecha de la etapa.         
    ![Imagen](../images/01_conceptos/image%209.png){width=288px}

!!! warning "Importante" 
    Nada impide que una etapa tenga asociadas **una o varias acciones no memorizadas**, una con activación a la entrada y otra con activación a la salida.


#### Acción principal

Existe un cuarto tipo de acciones que podemos utilizar: las **acciones principales**. Estas acciones también se asocian a una etapa y se ejecutan de manera continua durante todo el tiempo que la etapa esté activa.

El procedimiento de creación de estas acciones es el mismo que el indicado [aquí](../01_conceptos/#accion-compleja) pero, en lugar de introducir el nombre de la acción en la caja de acción, lo introduciremos en el campo `Main Action` dentro de las propiedades de la etapa.

![Imagen](../images/01_conceptos/main_action_property.png){width=288px}

Una vez asociada a la etapa, aparece representada en el diagrama SFC con un triángulo oscuro en la esquina superior derecha de la misma.

![Imagen](../images/01_conceptos/main_action_step.png){width=140px}

!!! warning "Importante" 
    Conceptualmente no hay diferencia sustancial con las acciones complejas utilizadas en las cajas de acción, pero tomaremos la convención de utilizar este tipo de acciones cuando **las variables involucradas no estén relacionadas con las E/S *hardware* de nuestro sistema** y las **acciones en la caja de acción** en caso contrario.

