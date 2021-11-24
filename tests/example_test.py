from tests.constants import client

def test_connection():
    assert client.health() == None
