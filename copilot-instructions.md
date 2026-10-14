# Instrucciones de Copilot para tc3_tutorial

- Antes de editar documentación, consulta [CONTRIBUTING.md](CONTRIBUTING.md); es la fuente normativa para estilo, estructura, imágenes, iconos y validación.
- Trata `docs/` como fuente del sitio. No edites `site/`: MkDocs lo genera al compilar.
- Mantén la navegación de `docs/index.md` coherente con `nav` en `mkdocs.yml`; respeta la organización de contenidos definida en CONTRIBUTING.md.
- Al editar `docs/contenidos/ejemplos/carro-basico/includes/`, valida el resultado desde `step-by-step.md`, que incluye esos fragmentos; `mkdocs.yml` los excluye como páginas independientes. `mkdocs build` valida el renderizado, pero no compila el código ST con TwinCAT.
- Para validar cambios de documentación, activa el entorno virtual y compila desde la raíz:

	```powershell
	.\.venv\Scripts\Activate.ps1
	mkdocs build
	```

- Si necesitas revisar el resultado en el navegador, ejecuta `mkdocs serve` con el entorno activado. Si no puedes ejecutar comandos, indica claramente que la compilación quedó sin verificar.
