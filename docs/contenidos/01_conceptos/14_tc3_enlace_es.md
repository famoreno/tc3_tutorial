## 🔗 Vinculación de variables y E/S

!!! tip "Recomendación"
    Hay un video de ejemplo en el Campus Virtual en `Automatización > Videos > TC3` con nombre `9_Runtime_Target_*.mkv`.

Una vez se han revisados y renombrados los terminales/canales de E/S del controlador, procedemos a vincularlos con las variables de nuestro programa.

El procedimiento es el siguiente (siguiendo con el ejemplo anterior de pulsador/lámpara):

- **DC** sobre el canal nombrado como `o_LamparaMarcha` (`DB > Change Link...`):
    - Seleccionar la variable que queremos vincular `MAIN.o_Lampara` en la instancia `PLCTask Input` y pulsar `OK`.
        - Observar cómo cambian los iconos del canal `o_LamparaMarcha` y de la variable `MAIN.o_Lampara` en la instancia (aparece una flecha sobre el icono en ambos casos, indicando que hay una vinculación).
- **DC** sobre la variable `MAIN.i_Pulsador` en la instancia `PLCTask Input` (`DB > Change Link...`)
    - Seleccionar en I/O el canal correspondiente a i_Pulsador
        - De la misma manera, cambian los iconos del canal `o_LamparaMarcha` y de la variable `MAIN.o_Lampara` en la instancia.

    !!! info "Info"
        Esta operación se puede hacer desde la instancia hacia la entrada/salida o al revés.
