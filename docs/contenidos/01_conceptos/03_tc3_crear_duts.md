## 👫 Creación de DUTs

Además de los tipos de datos simples (`BOOL`, `INT`, etc.) y los bloques funcionales ya existentes (`R_TRIG`) o creados por nosotros (`FB_Coordinador_ST`), en ocasiones podemos necesitar crear tipos de dato que están compuestos por otros tipos de dato. A estos tipos de datos se les denomina **tipos de unidad de datos** (*Data Unit Type*, DUT).

En nuestros proyectos vamos a poder hacer uso de dos de ellos: 

- **Estructuras** (`STRUCT`)
- **Enumeraciones** (`ENUM`).

### Estructuras

Aglutinan en su interior otros tipos de dato y se definen haciendo **CD** sobre la carpeta DUTs y escogiendo `Add → DUT`:

![Imagen](../images/01_conceptos/image%2016.png){width=240px}

Se le da un nombre significativo (se recomienda comenzar con `ST` como, por ejemplo, `ST_PIEZA`), se deja marcado ***Structure*** y se pulsa en ***Open***.

Se abrirá una ventana de texto para definir los componentes del tipo de dato:

```pascal
TYPE ST_PIEZA :
STRUCT
    Blanca: BOOL;
    Baja: BOOL;
    Tamano: INT;
    Tiempo: TIME;
END_STRUCT
END_TYPE
```

Para usarlo, se define una variable de ese tipo y se accede a sus componentes mediante el operador `.` (punto):

```pascal
// Definicion de variables
VAR
    Pieza: ST_PIEZA;
    Baja: BOOL;
END_VAR
--------------------------------
// Implementacion
Pieza.Blanca := TRUE;
Baja := (Pieza.Tamano < 12);
Pieza.Tiempo := T#1s;
```

### Enumeraciones

Una enumeración (`ENUM`) es un tipo de datos definido por el usuario compuesto por una serie de componentes separados por comas, también llamados valores de enumeración, que se utiliza para declarar variables definidas por el usuario.

Se definen haciendo **CD** sobre la carpeta DUTs y escogiendo `Add → DUT`:

![Imagen](../images/01_conceptos/image%2016.png){width=240px}

Se le da un nombre significativo (se recomienda comenzar con `E` como, por ejemplo,  `E_ColorBasic`), se deja marcado ***Enumeration*** y se pulsa en ***Open***.

Se abrirá una ventana de texto para definir los componentes del tipo de dato:

```pascal
{attribute 'qualified_only'}
{attribute 'strict'}
TYPE E_ColorBasic :
(
    eRed, 
    eYellow,
    eGreen,
    eBlue,
    eBlack
) // Basic data type is INT, default initialization is eRed
;
END_TYPE
```

Una variable definida con el tipo `E_ColorBasic` es, en realidad, de tipo `INT` y solo puede tomar los valores definidos en `E_ColorBasic`: `eRed`, `eYellow`, etc.

Cada uno de esos valores tiene un valor `INT` asociado, comenzando por el cero: `eRed = 0`, `eYellow = 1`, etc.

Para usarlo, se define una variable de ese tipo y se le asigna el valor deseado usando el nombre del tipo de dato ***Enumeration***:

```pascal
// Definicion de variables
VAR
    Color: E_ColorBasic;
END_VAR
--------------------------------
// Implementacion
Color := E_ColorBasic.eYellow; // asignacion de valor
IF Color <> E_ColorBasic.eRed THEN // comprobacion de valor
    [...]
END_IF
```
#### Declaración compacta

!!! warning "Importante"
    Este método se utiliza si el tipo **va a ser utilizado solo en un mismo POU**. Si se pretende utilizar el tipo enumerado declarado en más de uno, es más conveniente declararlo como DUT siguiendo el procedimiento anterior.
    
Existe otra manera más compacta de declarar una variable de tipo ***Enumeration***. Para ello, basta con declarar el nombre de la variable y los posibles valores que puede tomar. 

```pascal
VAR
    Estado : (E_Reposo, E_MarchandoDerecha, E_MarchandoIzquierda);
END_VAR
``` 


