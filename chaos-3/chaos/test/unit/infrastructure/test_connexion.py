
from chaos.infrastructure.connexion import Connexion as conn 
import psycopg2
import mock


def test_get_credentials():
    database_connexion_instance = conn()
    assert isinstance(database_connexion_instance.get_credentials(), dict) == True

def test_get_credentials_1():
    database_connexion_instance = conn()
    assert set(list(database_connexion_instance.get_credentials().keys())) == {"username","password", "hostname", "database", "port"}
