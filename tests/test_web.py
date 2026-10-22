from web import app

def test_index():
    response = app.test_client().get('/')
    assert response.status_code == 200
    assert b'calculator-form' in response.data

def test_health():
    response = app.test_client().get('/health')
    assert response.status_code == 200
    assert response.json == {'status': 'ok'}
