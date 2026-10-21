from knowledge import answer
def test_personal_data_blocked():
 assert 'No consulto' in answer('calificación de estudiante')[0]
def test_citations():
 assert answer('protección de datos')[1]
