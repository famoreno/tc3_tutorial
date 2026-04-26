# Descripción general - Prácticas
A lo largo del curso, el alumnado deberá desarrollar, **en grupo**, una serie de prácticas para alcanzar el conocimiento suficiente como para poder realizar un **proyecto de automatización sencillo** (pero completo) de un sistema automático de producción real.

El itinerario de prácticas incluye una serie de prácticas iniciales **que no se tienen que entregar** para adquirir y afianzar los conocimientos básicos sobre el *software* de desarrollo TwinCAT 3 y el funcionamiento esencial de los lenguajes de implementación de programas PLC que usaremos durante el curso: `ST` y `SFC`. 

Tras estas prácticas iniciales, los grupos deberán realizar un **proyecto de automatización** para una de las estaciones del sistema FMS-200 ubicadas en el laboratorio (aula Beckhoff). Para ello, deberán comprender los ejemplos proporcionados en el curso y **trasladar este conocimiento** al desarrollo de su proyecto.

## Itinerario de prácticas
Las prácticas propuestas están basadas en los ejemplos proporcionados y explicados en esta misma guía, estando cada una de ellas relacionada con uno de los ejemplos. Así, la hoja de ruta prevista para las prácticas es la siguiente :

1. <span class="fondo-gris">**No entregable**</span> ⌚ **1-2 sesiones**. Replicar el ejemplo **Demo**. [➡️](../contenidos/05_tc3_practicas/05_tc3_demo.md)
2. <span class="fondo-gris">**No entregable**</span> ⌚ **2-4 sesiones**. Adaptar el ejemplo **Carro básico (señalizado)** explicado en clase a los elementos de la estación del sistema FMS-200 asignada al grupo. [➡️](../contenidos/05_tc3_practicas/05_tc3_carro_basico.md)
3. <span class="fondo-verde">**Entregable**</span> ⌚ **Resto del curso**. Desarrollar el proyecto de automatización, abordándolo con distintos niveles de complejidad creciente:
      - <span class="fondo-rojo">**Mínimo**</span> **Monolítico**. Toda la funcionalidad en un solo bloque funcional [➡️](../contenidos/05_tc3_practicas/05_tc3_proyecto_mono.md)
      - **Estructurado**. La funcionalidad está dividida en distintos bloques funcionales.
      - **Estructurado + GEMMA**. Se incorpora la guía GEMMA para la gestión de los distintos modos de funcionamiento de un sistema automático de producción.

El símbolo ⌚ indica el tiempo estimado para su realización.

Para abordar un nivel de complejidad, es **obligatorio** haber completado satisfactoriamente el anterior. Al final del curso, los grupos deberán entregar el proyecto con el **nivel más alto que se haya implementado completamente**.

!!! warning "Importante"
    **Completar un nivel no es suficiente para obtener una buena calificación**, sino que la calidad de la solución también influye en la misma. De esta forma, por ejemplo, obtendrá una mejor calificación una implementación monolítica correcta y de alta calidad (con una implementación clara, eficiente, con una buena visualización, con distintas opciones, etc.), que una implementación estructurada caótica, con exceso o defecto de bloques funcionales, con variables no utilizadas y un código ilegible, **aunque funcione**.

## Proyectos de automatización
Antes de abordar el proyecto, los grupos deberán leer del documento `fms200_descripcion_funcional.pdf` que se proporciona en el campus virtual donde se muestra:

- Una visión general del sistema completo.
- Una explicación particular para cada estación disponible en el laboratorio.
- Las tablas de entrada/salida de las mismas.

Los grupos también deberán consultar los **vídeos** de las estaciones que se proporcionan en el campus virtual para tener una mejor visión del funcionamiento de las mismas.

!!! warning "Importante"
    Las visualizaciones mostradas en los vídeos están algo desfasadas y, en los proyectos, deben ser adaptadas para parecerse, en la medida de lo posible, a las visualizaciones incluidas en los ejemplos. Así, los nombres de los elementos que aparecen deberán ser sustituidos por las versiones más recientes que aparecen en la tabla de entrada/salida. Otras variables, como por ejemplo `PV`, deberán ser también sustituidas por sus versiones más explícitas: `Solicitadas`.

Finalmente, se recomienda a los grupos que **tengan visibles siempre los ejemplos** explicados en clase para tenerlos como referencia a la hora de desarrollar sus proyectos.

## Particularidades de las estaciones
Además de la información proporcionada en el documento de descripción funcional, podemos incidir en las siguientes particularidades de cada estación.

### FMS-201
- Esta estación dispone de un sensor específico para la **detección de falta material**, el cual no debe formar parte de las condiciones iniciales del sistema, sino que se utilizará dentro de la producción para detectar la falta de bases y solicitar al operador que introduzca nuevas.

### FMS-202
- En la visualización debe haber una zona donde se pueda **seleccionar** el tipo de rodamiento que se quiere transferir a la base: 
    - Como mínimo debe haber un botón que permita seleccionar uno u otro tipo (alto o bajo).
    - Opcionalmente, se puede implementar para que se puedan transferir cualquier tipo o ninguno.
- El actuador giratorio de entrada de la estación tiene **tres estados estables**, lo que nos permitirá colocarlo en cualquier posición de su recorrido, no solo en su inicio y final. 

### FMS-205
- En la visualización debe haber una zona donde se pueda **seleccionar** el tipo de tapa que se quiere transferir a la base. 
    - Como mínimo debe haber un conjunto de botones que permitan seleccionar las características de la tapa deseada (alta/baja, clara/oscura, metal/nylon), teniendo en cuenta que la combinación **oscura + metal** no es posible, por ejemplo.
    - Alternativamente se pueden implementar seis botones para los seis tipos distintos de tapa. En este caso se puede optar por permitir seleccionar solo un tipo de tapa o permitir seleccionar libremente un conjunto de combinaciones como válidas.
- Esta estación debe mantener en memoria la **información** de las tapas situadas en su disco giratorio. Como recomendación, defina *arrays* y estructuras para gestionar esta información.
- **Mientras el volteador de tapas no esté operativo**, la gestión de la detección de tapa invertida debe solucionarse simplemente mediante el aviso al operador de la situación y la espera a que el mismo lo solucione.

### FMS-206
- Esta estación debe colocar **siempre cuatro tornillos** sobre la base.
- Al implementar el procesamiento por lotes (o tareas) se deberán considerar **dos bucles anidados**: uno para los tornillos y otro para las piezas completas.

### FMS-208
- La gestión del movimiento de los ejes supone la mayor dificultad de esta estación. Revise cuidadosamente la información al respecto que aparece en la **descripción funcional** de la estación.
- Inicialmente, la **inicialización** de los ejes puede realizarse manualmente sobre la visualización. Posteriormente, una vez se haya implementado la secuencia de recogida y suelta de la base, es recomendable automatizar esta inicialización e incorporarla a la secuencia principal.
- Opcionalmente, se pueden incorporar **mejoras** al sistema como el mantenimiento de una memoria del almacén donde se guarden las posiciones que están ocupadas.