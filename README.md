# Asistente Académico de Electricidad — actualización V1.0

## Cambios
- Justificaciones de inasistencia organizadas por duración y por evento académico, mediante enlaces a los modelos institucionales existentes.
- No se crea un formulario ficticio para inasistencias superiores a veinte días: este modelo no se encontró en la carpeta FORMATO_SOLICITUDES_ESTUDIANTES.
- Cronograma PAO8–PAO9 2026-2S incorporado en Titulación y Comisión de Titulación.
- Planificación 2026-2S.pdf accesible en Comisión de Carrera.
- Se mantienen las imágenes originales, las consultas y los demás módulos.

## Instalar sobre versión existente
1. Detener el proceso anterior con Ctrl+C.
2. Descomprimir todos los archivos y la carpeta assets en C:\Electricidad\asistente_electricidad_python.
3. Conservar la carpeta .venv.
4. En CMD ejecutar:

```cmd
cd /d C:\Electricidad\asistente_electricidad_python
.venv\Scripts\python.exe -m streamlit run app.py
```

Los enlaces a documentos se abren en el repositorio institucional, conforme a sus permisos. No se transmiten solicitudes ni se almacenan datos personales en este módulo.
