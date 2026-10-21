# Revisión preliminar y plan de implementación — 20-10-2026

## Fuentes verificadas
- Política ESPOCH para el tratamiento de datos personales en sistemas informáticos, artículos 1–13: https://drive.google.com/file/d/19QAvXRGx3ULXPa2k1ZEX4NavQEdqSSg9/view. Su vigencia y acto aprobatorio deberán ratificarse con DTIC.
- Marco normativo SPDP: LOPDP (2021), Reglamento General (2023): https://www.spdp.gob.ec/marco-normativo/
- Resoluciones SPDP 2025–2026, incluida norma sobre IA emitida en febrero de 2026: https://www.spdp.gob.ec/resoluciones/
- Guía de privacidad desde diseño: https://www.spdp.gob.ec/docs/guias/2025-2/guia-de-proteccion-de-datos-personales-desde-el-diseno-y-por-defecto/

## Estado del chatbot anterior
**No acreditado / no verificable**. La URL conocida `https://asistente-electricidad-espoch.andresmorocho.chatgpt.site/` no se pudo recuperar mediante el mecanismo de inspección disponible. No se verificaron código, tráfico, logs, formularios, cesiones, avisos ni mecanismos de autenticación. No se puede afirmar cumplimiento ni infracción.

## Lista de control necesaria antes de poner datos personales en servicio
- [ ] Confirmar vigencia de política institucional, resolución, responsable, gestor/DPD y aprobación DTIC.
- [ ] Documentar finalidades, datos, base legítima y minimización por cada formulario.
- [ ] Determinar proveedores, encargados, subencargados, ubicaciones y transferencias internacionales.
- [ ] Establecer aviso de privacidad, derechos del titular y canal institucional.
- [ ] Definir plazos y procedimientos de conservación, eliminación, incidentes y copias de seguridad.
- [ ] Validar TLS, autenticación, perfiles, auditoría, segregación, análisis de vulnerabilidades.
- [ ] Analizar riesgos y procedencia de evaluación de impacto, antes de tratamientos de riesgo.
- [ ] Establecer control de respuestas, citas y revisiones de fuentes; pruebas de funcionalidad.
- [ ] Revisar permisos y derechos de autor de documentos del catálogo.

## Fases
0. Gobernanza, inventario, dictamen de riesgos y autorización para piloto.
1. Prototipo local mínimo (incluido en este paquete).
2. Incorporar catálogo académico *público* revisado y validado, con versiones de fuentes y citas.
3. Construir formularios y herramientas de docentes/estudiantes con almacenamiento mínimo, previa aprobación.
4. Añadir IA y sistema privado separado, solo con contratos, controles, análisis y autorizaciones pertinentes.
5. Publicación HTTPS, revisión DTIC, pruebas de seguridad y plan de mantenimiento.

**Advertencia:** ausencia de base de datos de chat propia no equivale a anonimato: servidores de terceros pueden registrar IP, sesiones o metadatos. En el prototipo los enlaces a documentos en Drive requieren confirmar si son públicos antes de distribuirlos.
