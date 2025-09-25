import json
from app import app

def test_products():
    tester = app.test_client()
    response = tester.get('/products')
    assert response.status_code == 200
    data = json.loads(response.data.decode('utf-8'))
    assert isinstance(data, list)
    assert "name" in data[0]
