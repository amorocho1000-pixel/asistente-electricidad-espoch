import streamlit as st
import unicodedata
import re
from catalogo import C, PROCESOS, FORMATOS_CC, TAREAS_CC, ROLES_CC, METODOLOGIAS, PLANIFICACION_CC_URL, METODOS_URL
from adicional import NORMAS, GIRAS, REQUISITOS_BUS, ESTUDIANTES, RESPUESTAS
from nuevos_formatos import SOLICITUDES, AYUDANTIA, PRACTICAS, GUIAS_LABORATORIO, EXPLICACIONES
from entregables_docentes import ENTREGABLES, RESUMEN, RRA, POL
from documentos_periodo import CRONOGRAMA_TITULACION, PLANIFICACION_2026_PDF

def clean(t):
    return ''.join(x for x in unicodedata.normalize('NFKD', t.lower()) if not unicodedata.combining(x))

def ficha_documento(nombre, url, detalle=''):
    """Presenta documentos enlazados con acceso a descarga y al original.

    La descarga depende de los permisos establecidos por el propietario en Drive.
    """
    st.markdown(f'**{nombre}**')
    if detalle:
        st.caption(detalle)
    m = re.search(r'/(?:document|spreadsheets|presentation|file)/d/([A-Za-z0-9_-]+)', url)
    if m:
        descarga = f'https://drive.google.com/uc?export=download&id={m.group(1)}'
        st.markdown(f'[Descargar]({descarga})　 [Ver original]({url})')
    else:
        st.markdown(f'[Ver original]({url})')

def enlaces(items):
    for nombre,url in items:
        ficha_documento(nombre, url)

st.set_page_config(page_title='Electricidad | Asistente académico',page_icon='⚡',layout='wide')
st.markdown('''<style>
:root{--primary-color:#7c182d} .block-container{max-width:1120px;padding-top:2.0rem}
h1,h2,h3{font-family:Arial,Helvetica,sans-serif;color:#171717;font-weight:700} .stButton>button{border-radius:8px}
.institutional{background:#9a151b;color:white;padding:24px;border-radius:10px}
.institutional h1{color:white;margin:0;font-size:2.1rem}.institutional p{margin:7px 0 0;color:#fff}
</style>''',unsafe_allow_html=True)
st.image('assets/cabecera_institucional.png', use_container_width=True)
st.title('Asistente académico de Electricidad')
st.write('Trámites, formatos y procedimientos de la Carrera de Electricidad')
t1,t2,t3,t4=st.tabs(['Estudiantes','Docentes','Consultas normativas','Privacidad'])
with t1:
 st.header('Servicios estudiantiles')
 categoria=st.selectbox('Seleccione el proceso',['Justificación de inasistencias','Prácticas preprofesionales','Ayudantía de docencia','Titulación','Convalidaciones y homologaciones','Otras solicitudes'])
 if categoria=='Justificación de inasistencias':
  st.subheader('Justificación de inasistencias')
  st.write('Seleccione el modelo adecuado a la duración o naturaleza de la inasistencia. Complete el documento y adjunte los respaldos requeridos por la normativa aplicable; la descarga no equivale a su presentación ni aprobación.')
  st.markdown('#### Según duración de la inasistencia')
  enlaces([(n,u) for n,u in SOLICITUDES if 'Justificacion Inasistencia hasta 5 dias' in n or 'Justificacion Inasistencia 6 a 20 dias' in n])
  st.markdown('#### Inasistencias a actividades académicas específicas')
  enlaces([(n,u) for n,u in SOLICITUDES if 'Justificacion Inasistencia' in n and not any(x in n for x in ['hasta 5 dias','6 a 20 dias'])])
  st.markdown('#### Otras solicitudes relacionadas con ausencias y evaluaciones')
  enlaces([(n,u) for n,u in SOLICITUDES if any(x in n for x in ['Rendir Evaluacion Atrasada','Nueva Fecha Sustentacion','Examen Recuperacion Complexivo'])])
  st.info('Para inasistencias superiores a 20 días no se identificó un formato independiente en el catálogo oficial de solicitudes consultado. No debe confundirse el formato «retiro de matrícula después de 20 días» con una justificación de inasistencia. Antes de presentar el trámite, consulte a Coordinación y la normativa aplicable.')
  st.markdown(f'[Consultar Reglamento de Régimen Académico vigente]({NORMAS["rra"][1]})')
 elif categoria=='Prácticas preprofesionales':
  st.subheader('Prácticas preprofesionales — formatos A–F')
  st.write('Secuencia documental: solicitud (A), planificación (B), evaluación de habilidades blandas (C), autoevaluación (D), informe (E) y consolidado docente (F). La ejecución y reconocimiento de horas requieren validación institucional.')
  enlaces(PRACTICAS)
  st.markdown('#### Solicitudes vinculadas')
  enlaces([(n,u) for n,u in SOLICITUDES if 'Practicas' in n])
  st.markdown('#### Reconocimiento de ayudantías')
  st.write(EXPLICACIONES['ayudantia'])
  st.markdown(f'[Reglamento de Régimen Académico — arts. 228–230]({NORMAS["rra"][1]})')
 elif categoria=='Ayudantía de docencia':
  st.subheader('Ayudantía de docencia — ruta documental')
  st.write(EXPLICACIONES['ayudantia'])
  enlaces(AYUDANTIA)
  st.markdown(f'[Reglamento de Ayudantías — Resolución 427.CP.2025]({NORMAS["ayudantias"][1]})')
 elif categoria=='Titulación':
  st.subheader('Titulación')
  st.markdown('#### Cronograma vigente de titulación PAO8–PAO9 · 2026-2S')
  ficha_documento('Cronograma de Titulación PAO8–PAO9 · 2026-2S (PDF)',CRONOGRAMA_TITULACION)
  enlaces(ESTUDIANTES['Titulación'])
  st.markdown('#### Solicitudes correspondientes al proceso')
  enlaces([(n,u) for n,u in SOLICITUDES if any(k in n for k in ['Titulacion','Sustentacion','Complexivo','Medios_Tecnologicos'])])
 elif categoria=='Convalidaciones y homologaciones':
  st.subheader('Convalidaciones y homologaciones')
  st.write(EXPLICACIONES['convalidacion'])
  enlaces([(n,u) for n,u in SOLICITUDES if 'Homologacion' in n])
  st.markdown(f'[Reglamento de Régimen Académico — Resolución 450.CP.2026]({NORMAS["rra"][1]})')
 else:
  st.subheader('Catálogo de solicitudes estudiantiles')
  enlaces(SOLICITUDES)
with t2:
 st.header('Gestión académica docente')
 modulo=st.radio('Apartado',['Comisiones académicas','Procesos del docente'],horizontal=True)
 if modulo=='Comisiones académicas':
  com=st.selectbox('Comisión',list(C));enlaces([(n,u) for n,u in C[com] if not (com=='Comisión de Carrera' and n=='Acta de Comisión de Carrera')])
  if com=='Comisión de Carrera':
   st.subheader('Evidencias de la planificación por responsable')
   ficha_documento('Planificación académica y de gestión 2026-2S (PDF)', PLANIFICACION_2026_PDF)
   rol=st.selectbox('Responsable',list(ROLES_CC));cod=ROLES_CC[rol]
   found=[t for t in TAREAS_CC if not cod or cod.lower() in t[2].lower()]
   for codigo,titulo,responsable,evidencia,formato in found:
    with st.expander(f'{codigo} — {titulo} | {responsable}'):
     st.write('Evidencia mínima: '+evidencia)
     if formato and formato in FORMATOS_CC:ficha_documento(formato, FORMATOS_CC[formato])
     elif codigo=='A11':st.info('La CEACC elabora el informe y lo remite al Subdecanato para envío a la DEAC con el formato institucional.')
     else:st.caption('Consultar la planificación y los respaldos que correspondan a esta actividad.')
   st.caption('La planificación distingue evidencias programadas de entregas y aprobaciones efectivas.')
 else:
  proc=st.selectbox('Proceso',['Giras de observación y visitas de campo','Estrategias metodológicas innovadoras','Prácticas de laboratorio'])
  if proc.startswith('Giras'):
   st.subheader('Procedimiento institucional de giras de observación')
   for a,b in GIRAS:
    with st.expander(a,expanded=True):st.markdown(b)
   st.subheader('Expediente de transporte institucional')
   for x in REQUISITOS_BUS:st.markdown('• '+x)
   st.subheader('Formatos para planificación, ejecución e informe de giras')
   st.write('Seleccione el documento correspondiente. Los archivos se abren desde el repositorio institucional y pueden descargarse si dispone de los permisos necesarios.')
   enlaces([
    ('Anexo B — Planificación de gira o visita de campo', 'https://docs.google.com/document/d/1r-kd8EnDo4nJshxjLsFeORvanspuuI-c/edit'),
    ('Anexo C — Compromiso estudiantil', 'https://docs.google.com/document/d/1rbowcFpdG8yE4oF9za4FM4_KNoSvQVzY/edit'),
    ('Anexo D — Informe de gira o visita de campo', 'https://docs.google.com/document/d/13OsqLI3_olN-gu2ok4N_WRIRxdm4RGgp/edit'),
    ('Carta de compromiso del docente', 'https://docs.google.com/document/d/1NUKi3shWKVfDsIaeI6P6_ZxjyKDI8qK7/edit'),
    ('Plantilla Quipux — Solicitud de transporte institucional', 'https://docs.google.com/document/d/1jsucwLkcVnrliispbj7m-Y-FYyP6Jhkp/edit'),
   ])
   st.markdown('#### Normativa y documentación de referencia')
   enlaces([
    ('Guía institucional de giras de observación y visitas de campo', NORMAS['giras'][1]),
    ('Guías Académicas Institucionales — codificación, Resolución 337.CP.2026', 'https://drive.google.com/file/d/1REzt4QiJcUtY0Qb8sOhCBXYxBRraqg1S/view'),
    ('Reglamento para el Uso de Vehículos de la ESPOCH — Resolución 666.CP.2024', NORMAS['vehiculos'][1]),
    ('Ver carpeta de formatos de giras', 'https://drive.google.com/drive/folders/1OgIPfOXULX-EDRScjtzr4jYg6dBgbm2x'),
   ])
   st.warning('Los formularios de giras y transporte incluyen información personal, incluso datos de salud en Anexo C. No se recaban en este aplicativo público.')
  else:
   for i,s in enumerate(PROCESOS[proc]['pasos'],1):st.markdown(f'{i}. {s}')
   if proc=='Estrategias metodológicas innovadoras':
    met=st.selectbox('Metodología',list(METODOLOGIAS));loc,desc=METODOLOGIAS[met];st.markdown(desc);st.write('Resolución 064.CP.2025, numeral '+loc)
    st.markdown('#### Formatos institucionales para la estrategia didáctica')
    st.write('Utilice los documentos correspondientes a la cooperación, planificación previa y cierre de la actividad.')
    enlaces([
     ('Carta de invitación — coordinación con la institución o experto participante', 'https://docs.google.com/document/d/1ODbF-KEg58CcHL2BXsXDgKUkytf8xsHR/edit'),
     ('Anexo 1 — Planificación de la estrategia didáctica', 'https://docs.google.com/document/d/1p0iZH79u02dcPcey-nXohtkY0gTPg8jE/edit'),
     ('Anexo 2 — Informe final de ejecución', 'https://docs.google.com/document/d/1TB8IvbmByTCLU3_qn5VlS328NF0ArV8-/edit'),
    ])
    st.markdown('**Fuente normativa:** [Métodos y Estrategias Didácticas — Resolución 064.CP.2025, numerales 6.1–6.6 y anexos]('+METODOS_URL+').')

    st.write('El numeral 6.1 requiere cooperación, planificación académica aprobada por Comisión de Carrera, declaración en sílabo y planificación de asignatura, evidencias de ejecución y evaluación.')
   else:
    st.markdown('#### Formatos de prácticas de laboratorio')
    st.write('Consulte el acta de la Comisión de Carrera sobre la designación de prácticas de laboratorio, la declaración de prácticas formativas y el formato de seguimiento.')
    enlaces([
     ('Documento de Comisión de Carrera — Designación de guías de laboratorio 2026-2S', 'https://drive.google.com/file/d/18BwlIbW-QzrOGxnBCFvpNKfOMZu0EWIJ/view'),
     ('Declaración de prácticas formativas de Electricidad 2026 — documento PDF', 'https://drive.google.com/file/d/1_UhtnMSMfSS7zc8AXL4F_logEPVI5eVW/view'),
     ('Formato de seguimiento de prácticas de laboratorio (Word)', 'https://docs.google.com/document/d/1rr06IWfUa_wDHKhzoieZM0yxmAcnlhZM/edit'),
     ('Formato de informe consolidado de prácticas de laboratorio — Coordinación de Carrera', 'https://docs.google.com/document/d/1eKmTHiExdmHl_UtoC-ryXts_gvKMUyfM/edit'),
    ])
with t3:
 st.header('Consultas sobre reglamentos y procedimientos')
 st.markdown('### Biblioteca normativa y documentos oficiales')
 st.write('Consulte los reglamentos, estatutos, guías y resoluciones de la Carrera de Electricidad, o acceda al servicio documental del Decanato de Desarrollo Académico (DDA). La posibilidad de abrir o descargar cada documento depende de los permisos del repositorio.')
 col_base,col_dda=st.columns(2)
 with col_base:
  st.link_button('📚 Base normativa de Electricidad', 'https://drive.google.com/drive/folders/1c04_3XkerZ5IMfQ9HadDTyKjeSFLXNW1', use_container_width=True)
 with col_dda:
  st.link_button('🏛️ Consulta documental DDA', 'https://script.google.com/macros/s/AKfycbyIZK3CGZgQR6C7-_YLH2nOi278nYLTlweBOMuPBzpYzarPD92jHnbcF3nmhqSeejMd/exec', use_container_width=True)
 st.divider()
 with st.expander('Entregables docentes · evaluación y cierre académico 2026-2S', expanded=False):
  st.markdown('### Obligaciones documentales por responsabilidad')
  st.markdown('Los destinos se diferencian entre **Otros Docencia**, instrumentos académicos, registros del sistema institucional y **Coordinación de Carrera**.')
  for nombre,ambito,destino,norma,fuente,formato in ENTREGABLES:
   with st.expander(nombre):
    st.markdown('**Aplica a:** '+ambito)
    st.markdown('**Destino:** '+destino)
    st.markdown(f'**Sustento:** [{norma}]({fuente})')
    if nombre=='Obligaciones de resultados de sostenibilidad':
     st.markdown('**Numeral 9:** la asignatura institucional de Sostenibilidad Ambiental debe integrar actividades prácticas acordes con el campo de formación de cada carrera, atendiendo al marco jurídico, la seguridad, la salud y los contextos culturales.')
     st.markdown('**Numeral 9.1:** se promoverán acciones individuales o conjuntas en la carrera, facultad o institución, orientadas a desarrollar competencias y sostenibilidad con buenas prácticas.')
     st.markdown('**Numeral 9.2:** cuando las actividades estén vinculadas a proyectos de investigación o vinculación aprobados por Consejo Politécnico, el personal académico debe reportar avances y resultados al DDA cada dos períodos académicos, acreditando expresamente la participación estudiantil.')
    if formato:ficha_documento('Plantilla o documento relacionado',formato)
  st.caption('Las evidencias deben reflejar actividades efectivamente realizadas, no entregas presuntas.')
 st.divider()
 st.markdown('### Realizar una consulta normativa')
 st.write('Puede escribir preguntas sobre matrículas, inglés, convalidaciones, giras, transporte, distributivos, estrategias o entregables docentes.')
 question=st.chat_input('Escriba su consulta académica sin datos personales')
 if question:
  st.chat_message('user').write(question)
  q=clean(question); scored=[]
  for keys,answer,key in RESPUESTAS:
   score=sum(len(k.split())+1 for k in keys if clean(k) in q)
   if score:scored.append((score,answer,key))
  if any(x in q for x in ['entregable docente','entregables docente','otros docencia','subir al repositorio','evidencias docente','cierre academico','final del periodo','fin del periodo','rubricas docente','team teaching']):
   with st.chat_message('assistant'):
    st.markdown(RESUMEN)
    st.markdown(f'**Fuentes:** [RRA, artículo 26]({RRA}) · [Políticas Académicas 2026-2S, numerales 5, 6, 11, 12 y 13]({POL})')
    st.caption('Para revisar las obligaciones una por una, abra el apartado «Entregables docentes» situado arriba.')
  elif scored:
   _,answer,key=max(scored,key=lambda t:t[0]);title,url=NORMAS[key]
   with st.chat_message('assistant'):
    st.write(answer);st.markdown(f'**Fuente:** [{title}]({url})')
    if key=='vehiculos':
     st.write('**Requisitos habilitantes comprobados:**')
     for x in REQUISITOS_BUS:st.markdown('• '+x)
  else:
   with st.chat_message('assistant'):st.warning('No dispongo aún de un apartado normativo cotejado para responder con seguridad esta pregunta. Puede consultar el catálogo de normas o formular una pregunta más específica. No atribuiré artículos inexistentes.')
 st.caption('Motor local de respuestas fundamentadas; no utiliza IA generativa ni lee automáticamente toda la normativa. No se almacenan preguntas en una base de datos propia.')
with t4:
 st.header('Privacidad y protección de datos personales')
 st.write('Conozca sus derechos y las disposiciones que regulan la recopilación, utilización, conservación y protección de datos personales en Ecuador y en la ESPOCH.')
 st.subheader('Política institucional de la ESPOCH')
 st.markdown('**Políticas para el tratamiento de datos personales en los sistemas informáticos de la Escuela Superior Politécnica de Chimborazo**')
 st.write('La política institucional establece, entre otros aspectos, los principios de tratamiento (artículo 4), las responsabilidades (artículo 6), la confidencialidad (artículo 7) y la información que debe proporcionarse antes de recopilar datos (artículo 11).')
 ficha_documento('Política de datos personales de la ESPOCH', 'https://drive.google.com/file/d/19QAvXRGx3ULXPa2k1ZEX4NavQEdqSSg9/view')
 st.subheader('Legislación ecuatoriana')
 st.markdown('**Ley Orgánica de Protección de Datos Personales (LOPDP)**')
 st.write('Publicada en el Quinto Suplemento del Registro Oficial N.º 459, de 26 de mayo de 2021. Reconoce principios, derechos y obligaciones relativos al tratamiento de datos personales.')
 st.link_button('Leer Ley Orgánica de Protección de Datos Personales', 'https://www.asambleanacional.gob.ec/es/multimedios-legislativos/63464-ley-organica-de-proteccion-de-datos', use_container_width=True)
 st.markdown('**Reglamento General de la LOPDP**')
 st.write('Expedido mediante Decreto Ejecutivo N.º 904 y publicado en el Suplemento del Registro Oficial N.º 435 de 13 de noviembre de 2023.')
 st.link_button('Leer Reglamento General de Protección de Datos', 'https://www.registroficial.gob.ec/tercer-suplemento-al-registro-oficial-no-435/', use_container_width=True)
 st.subheader('Normativa y orientación de la autoridad de control')
 st.write('La Superintendencia de Protección de Datos Personales publica el marco normativo y resoluciones complementarias; se recomienda revisar sus actualizaciones.')
 col1,col2=st.columns(2)
 with col1:
  st.link_button('Marco normativo — SPDP', 'https://www.spdp.gob.ec/marco-normativo/', use_container_width=True)
 with col2:
  st.link_button('Resoluciones — SPDP', 'https://www.spdp.gob.ec/resoluciones/', use_container_width=True)
 st.divider()
 st.markdown('**Privacidad en este asistente**')
 st.write('Este asistente está diseñado para consultas informativas y acceso a formatos. No introduzca cédulas, calificaciones, datos de salud, contraseñas ni información personal de otras personas en las consultas. El uso de un proveedor de alojamiento puede involucrar registros técnicos; antes de una publicación institucional deben verificarse los tratamientos y sus avisos correspondientes.')
 st.caption('Los enlaces permiten leer los documentos en sus sitios de origen; la posibilidad de descarga está sujeta a los permisos de cada sitio.')

# Pie institucional: imágenes originales conservadas sin modificación.
st.divider()
footer_left, footer_center, footer_right = st.columns([1, 2, 1])
with footer_left:
    st.image('assets/logo_carrera.png', width=140)
with footer_right:
    st.image('assets/logo_facultad.png', width=155)
