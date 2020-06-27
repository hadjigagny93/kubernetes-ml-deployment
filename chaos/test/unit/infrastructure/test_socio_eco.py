import mock 
from chaos.infrastructure.socio_eco import SocioEco
import pandas as pd

@mock.patch("psycopg2.connect")
def test_read(mock_connect):
    mock_con = mock_connect.return_value
    data = SocioEco.read()

    assert isinstance(data, pd.DataFrame)