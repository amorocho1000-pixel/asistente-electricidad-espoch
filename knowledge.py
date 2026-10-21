import unicodedata
POL='https://drive.google.com/file/d/19QAvXRGx3ULXPa2k1ZEX4NavQEdqSSg9/view'
SPDP='https://www.spdp.gob.ec/marco-normativo/'
RES='https://www.spdp.gob.ec/resoluciones/'
SOURCES=[('Política de datos ESPOCH (Drive)',POL),('Normas nacionales SPDP',SPDP),('Resoluciones SPDP',RES)]
def answer(question):
 q=''.join(c for c in unicodedata.normalize('NFKD',question.lower()) if not unicodedata.combining(c))
 if any(w in q for w in ('cedula','calificacion','expediente','historial academico','nota de','matricula de')):
  return 'No consulto ni proporciono información personal o académica individual. Utilice canales institucionales autorizados.',[]
 if any(w in q for w in ('privacidad','proteccion de datos','datos personales','consentimiento')):
  return 'La política ESPOCH establece principios y obligaciones en sus artículos 4, 6, 7 y 11. Consulte también la Ley Orgánica de Protección de Datos Personales, su Reglamento y normas SPDP.',SOURCES
 if any(w in q for w in ('inteligencia artificial','chatbot','modelo de ia')):
  return 'Esta versión utiliza respuestas predefinidas, sin IA generativa. Una futura conexión con IA requiere analizar finalidad, seguridad, transferencias y normativa SPDP de 2026.',[('Resoluciones SPDP',RES)]
 return 'Todavía no dispongo de una fuente pública validada para esa consulta. No inventaré procedimientos, horarios ni fechas.',[]
