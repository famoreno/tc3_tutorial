## 🔀 Estructuras de evolución

### Secuencia básica

- Una secuencia básica se compone de una **sucesión lineal de etapas y transiciones**, donde las primeras se van a ir ejecutando en secuencia conforme las condiciones asociadas a las segundas se vayan cumpliendo.

- Normalmente, al final de la secuencia se producirá un salto hacia atrás (o el inicio) en el programa.

    ![Imagen](../images/01_conceptos/image%2010.png){width=288px}

- Para insertar un salto detrás de una transición, hay que hacer **CD** sobre la transición y seleccionar ***Insert jump after***. Solo hay que indicar el nombre de la etapa a la que queremos saltar.

### Bifurcación

- Tras una etapa podemos realizar una **bifurcación** en distintas ramas en función de distintas condiciones. Esto nos permite dirigir la secuencia por un camino si ocurre un evento y por otros distintos si ocurren otros eventos.

- En el ejemplo de la figura, si la etapa `Init` está activa y se activa `Execute`, el programa evolucionará por la rama de la izquierda llegando a `S0`. Si lo que se activa es `Restore`, el programa evolucionará por la derecha pasando a `Sr` y, una vez se active `Restaurado`, la secuencia pasará a `S0`.

    ![Imagen](../images/01_conceptos/image%2011.png){width=336px}

- Para realizar una bifurcación, hacer **CD** sobre la **transición** donde se quiera hacer la bifurcación (`Execute` en el ejemplo) y seleccionar ***Insert branch right***.

- Nada impide que se pueda hacer una bifurcación con más de dos ramas.

- Es recomendable que las condiciones de la bifurcación sean excluyentes pero nada impide que no lo sean. El programa tomará el camino de la primera transición cuya condición sea verdadera de izquierda a derecha.

- Si ocurriera que varias o todas las condiciones son verdaderas a la vez, el programa evolucionará por la rama de la izquierda. **Aunque esto puede ser útil en algunos casos, esto suele indicar que hay un mal diseño en el programa.**

### Paralelismo

- Si queremos que el programa evolucione por dos secuencias en paralelo (se ejecutan simultáneamente) podemos incluir un paralelismo en el código.

- En el ejemplo de la figura, si la etapa `Init` está activa y se activa `Execute`, el programa evolucionará por ambas ramas a la vez, activando los estados `S0` y `Sr` de manera simultánea (y por tanto, `LuzRoja` y `Restaura`).

    ![Imagen](../images/01_conceptos/image%2012.png){width=480px}

- En la transición con condición `NOT Pulsador OR S0.t>T#5s` se produce un punto de sincronización ya que, para que el programa evolucione a `S1` debe ocurrir que `S0` y `Sr2` estén activas y, además, que la condición `NOT Pulsador OR S0.t>T#5s` sea cierta. Por tanto, podemos decir que el programa *esperará* hasta que termine la rama de la derecha antes de evolucionar.
  
