import mock 
from chaos.infrastructure.marketing import Marketing
import pandas as pd

@mock.patch("psycopg2.connect")
def test_read(mock_connect):
    mock_con = mock_connect.return_value
    data = Marketing.read()
    assert isinstance(data, pd.DataFrame)