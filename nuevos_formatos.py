"""Catálogos cotejados con 01_FORMATOS_ELECTRICIDAD, 21-10-2026."""
DOC='https://docs.google.com/document/d/{}/edit'
SHEET='https://docs.google.com/spreadsheets/d/{}/edit'
_items=[
('01_Solicitud_Matricula_Especial','1QcqbeHCYhVF0yxuIG6lVur1c25xoYJ6j'),
('02_Solicitud_Reingreso_Carrera','1YhpeXV2tRFHjkUqoYclQgU48EHG3rLth'),
('03_Justificacion_Inasistencia_hasta_5_dias','12yt8bnBihW7s6toPXPBd4AYFVdCpkq49'),
('04_Justificacion_Inasistencia_6_a_20_dias','1R1lrDo-4yyxTl_pfRRh4gbk4lBob7hzy'),
('05_Solicitud_Rendir_Evaluacion_Atrasada','1RRtOTZG6i4NtJeMnbXy-DYsO3hijhwLj'),
('06_Solicitud_Recalificacion_Evaluacion','131-rr5NF5IzzHHdEq4WZ07uHqzn6K4UY'),
('07_Solicitud_Retiro_Matricula_PAO_mas_20_dias','1vWFV6fFC0gl937yz0BlKRoyFUWLTQweT'),
('08_Solicitud_Retiro_Asignaturas','1MT3DEM38e4fb_1mNb0om8CJu6-Cr_FJx'),
('09_Solicitud_Retiro_Matricula_PAO','1zt1b3-CXhWipmBm0nejUaM7rNSs0_sXT'),
('10_Solicitud_Movilidad_Excepcional_Asignatura','1BBNx4fQmEUV8hsfLj9n_6K_6gm0TRUVb'),
('11_Solicitud_Devolucion_Valores','1x07zhNu4c_fbwMTf0nlbYsbf1Yangs4L'),
('12_Solicitud_Evaluacion_Medios_Tecnologicos','1pWDYA6ghwUu6VHvkc9o2sjwX55jYflt-'),
('13_Solicitud_Reingreso_Modulo_Titulacion','14ajDfKqPYIlGNKnfV_XFaizM2aCMDSfP'),
('14_Solicitud_Examen_Recuperacion_Complexivo','1DTLpEasFRl3Z9OjJrvEtOwApcNIQWY9f'),
('15_Solicitud_Recalificacion_Examen_Complexivo','1HS1DM4RmiRFdC1Rs9HXmJCb7sQdE0fC_'),
('16_Solicitud_Nueva_Fecha_Sustentacion','1SlJwpFTclkSumuyXfgHq5NlyrHsRmjNa'),
('17_Justificacion_Inasistencia_Sustentacion','1T9WCs7auefeslwEr2kevMAdbC3dWURsb'),
('18_Solicitud_de_Cambio_Director_Trabajo_Titulacion','1kkbNbDD_GbReXHohM-j0spGuVwz0rfHh'),
('19_Solicitud_Habilitacion_Matricula_Pendiente','1AwlOvbhAIbeXtFLlYKR9Uj0RkyyYpRkg'),
('20_Solicitud_Sustentacion_Individual','1fQX05rVqZla7Idp7PHGymdtzVH83MEZ7'),
('21_Justificacion_Inasistencia_Examen_Complexivo','1LW9hgQmUXJWOqhEn35P0KgSTECRZBjVH'),
('22_Solicitud_Concluir_Proceso_Titulacion','1E7KauWnfzX3vKlu3s7E3aNk1jtDF2oQj'),
('23_Justificacion_Inasistencia_Gira','1P1ck6FfmhjfU39WXAKypXJEVSmv2kTJ0'),
('24_Solicitud_Homologacion_Asignaturas','1Mq6MlMMmScXX9Nv10p4ZA41yXghONeTJ'),
('25_Solicitud_Homologacion_Practicas_Preprofesionales','1j4GYNoTpe4v7KVjkDgnG93pk1waJRtwk'),
('26_Solicitud_Inicio_Practicas_Preprofesionales','1RotmrafYU5lEePmlQxCTNwQXX7KFM5l_'),
('27_Solicitud_Tercera_Matricula','14Vjkam0FKhWvGP5ES8WresonYVIMKwsc'),
('28_Solicitud_Adelanto_Practicas_Preprofesionales','1heRERgpdDWWFXuz2T8beqIrnae-O0D8q')]
SOLICITUDES=[(n.replace('_',' '),DOC.format(i)) for n,i in _items]
AYUDANTIA=[(n,DOC.format(i)) for n,i in [
('01 · Solicitud','1qupYxguRicy8TBGGgNzmBVomlnKy9ZNG'),('02 · Planificación','1cp091MCLVhs_25AtPb5kYC8OYiHItm2C'),('03 · Informe de medio ciclo','1u4a43mxFAJD0kijASRgImkYe0_vdOkr9'),('04 · Informe de fin de ciclo','1gtqd6JmPpCv9dnghL5kUwkyz7zhO5xqr'),('05 · Evaluación','1a6QxjNkWtWoeU9O9XWLVE_d2VIdIfKo0'),('06 · Informe del tutor para certificación','1ajvzo6mICC0Ejz8yclzzbVSVj8CWqgPs'),('07 · Informe mensual','1QtYmlbnSu1K5OD6LR4GvuTvoB4u7VWC7'),('08 · Guía de presentación de documentación','1Th3E2NqefEIiktHx92qWBRZMYkGXqkKt')]]
PRACTICAS=[(n,SHEET.format(i) if ext=='xlsx' else DOC.format(i)) for n,i,ext in [
('Anexo A · Solicitud','1ofDSR8BoxttD9BakdwZW0zvTS28b03nU','docx'),('Anexo B · Planificación','1xhz19fEv_1zFfyuZmqLF-2E7a8H1YUe-','docx'),('Anexo C · Evaluación de habilidades blandas','1I0att3QwpjVMrPbHi3Kt8lDQ0N2zsNb0','docx'),('Anexo D · Autoevaluación','1TS7aL8Ujw-9IJJkNCe8SbQNJ143MRDrz','docx'),('Anexo E · Informe','1ivWGJnUq8y0J-OVOzNOGJU0VEsKHUXVD','docx'),('Anexo F · Consolidado docente','1B9VslVhf1xL11WodO74gDRVolTko1iS6','xlsx')]]
GUIAS_LABORATORIO='https://drive.google.com/file/d/18BwlIbW-QzrOGxnBCFvpNKfOMZu0EWIJ/view'
EXPLICACIONES={
 'ayudantia':'El estudiante solicita su participación mediante el formato 01; la ayudantía requiere designación y planificación de actividades (02), seguimiento documentado (informes de medio ciclo, fin de ciclo y mensual, según corresponda), evaluación (05) e informe del tutor para certificación (06). Revise la guía 08 para armar el expediente. Para solicitar que las horas se acrediten como prácticas preprofesionales, presente ante la unidad responsable la certificación y los respaldos de designación, actividades, horas y evaluación. La acreditación no es automática. Fundamento: Reglamento de Régimen Académico ESPOCH, arts. 228–230, y Reglamento de Ayudantías, Resolución 427.CP.2025. La autoridad emisora y los requisitos exactos de certificación deben cotejarse con el expediente y reglamento antes de tramitar.',
 'convalidacion':'Para inglés, el Reglamento de Régimen Académico (Resolución 450.CP.2026), apartado de homologación de inglés, prevé certificado B1 MCERL o superior de entidad reconocida y validación del original o copia notariada por Comisión de Carrera para Inglés I–IV; el texto remite también a Resolución 605.CP.2025. Para actividades extracurriculares y ayudantías como prácticas preprofesionales, véanse arts. 228–230; se verifica pertinencia, planificación, evaluación y horas acreditables. La homologación debe ser resuelta y registrada por las instancias competentes; no basta completar la solicitud.',
 'laboratorio':'El docente debe comprobar su designación, declarar la práctica en el sílabo y planificación, disponer de la guía legalizada antes de ejecutar, registrar las evidencias de realización y emitir el reporte de seguimiento para Coordinación. Coordinación consolida los informes de toda la Carrera. El documento 2026-2S_DESIGNACION_GUIAS_LABORATORIO permite verificar la asignación correspondiente; no sustituye la legalización de la guía.'}
