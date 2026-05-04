# 🛒 Carro básico

!!! info "Nota"
    Esta práctica **NO** es entregable.

En esta segunda práctica, trataremos de replicar el comportamiento del **carro básico señalizado** con algunos de los sensores y actuadores de la estación que se nos haya asignado. Para ello, buscaremos **en la descripción funcional** de nuestra estación algún actuador **biestable con sensores final de carrera** en ambos extremos. En caso de no encontrar ninguno, escogeremos un actuador **monoestable** y **modificaremos** levemente el GRAFCET del carro básico señalizado para que la vuelta del carro se realice con la desactivación de la señal que produce la ida.

## Ejemplo de apoyo

Utilice el ejemplo del [**carro básico**](../contenidos/03_tc3_carro_basico.md) como apoyo para entender la estructura del proyecto.

## Entregables

Ninguno.

## Funcionalidades

!!! warning "Atención"
    📃 Versión descargable [aquí](../../pdfs/Checklist_Func_Basico.pdf){target="_blank"}.

El proyecto desarrollado debe tener las siguientes funcionalidades:

??? info "Requeridas"
    1. Secuencia de producción normal.
    1. Visualización funcional.
    1. Modo manual (mandos directos) y automático.
    1. Modo de procesamiento por lotes (tarea).
    1. Gestión de la tarea (maniobras solicitadas, pendientes y realizadas).
    1. Parametrización de todas las variables (tiempos y cantidades).

## Componentes

- `MAIN`: programa principal (`ST`)
    - `FB_Carro`: lógica de control (`SFC`)
- `VISU_Carro`: interfaz gráfica

## Itinerario

!!! warning "Atención"
    La lista es *clickable* pero **NO** guarda el estado; si actualizas o entras/sales de la página se perderán las marcas.

    📃 Versión descargable [aquí](../../pdfs/Checklist_Itinerario_Carro_Basico.pdf){target="_blank"}.

- [ ] Crear una solución con el nombre apropiado (`XXX_TC3_GYY`, `XXX` = iniciales de la asignatura, `YY` = número del grupo).
- [ ] Crear el proyecto PLC (`Carro_Basico_PLC`).
- [ ] Crear el bloque funcional `FB_Carro` (`SFC`).
- [ ] Declarar las variables pertinentes en el **FB** según la tabla de entrada y salida de la estación.
- [ ] Declarar e invocar la instancia `Carro` de `FB_Carro` en el programa `MAIN`.
- [ ] Compilar.
- [ ] Buscar el controlador remoto.
- [ ] Configurar entrada/salida (dispositivos y terminales).
- [ ] Vincular variables.
- [ ] Activar la configuración.
- [ ] Transferir el proyecto (`Login`) y ponerlo en funcionamiento (`Start`).
- [ ] Monitorizar una variable de entrada (pulsador de marcha).
- [ ] Forzar una variable de salida (lámpara de alarma).
- [ ] Crear una visualización (`VISU_Estacion`) que permita monitorizar todas las entradas y activar todas las salidas
- [ ] Probar una a una todas las entradas y salidas desde la visualización.
- [ ] Implementar en `FB_Carro` la secuencia de pasos del GRAFCET del carro básico señalizado (en `SFC`).
- [ ] Compilar y poner el programa en ejecución para comprobar el correcto funcionamiento del sistema.
