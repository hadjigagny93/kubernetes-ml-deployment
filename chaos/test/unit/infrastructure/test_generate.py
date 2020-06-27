
from chaos.infrastructure.generate import GenerateDataSet
from chaos.infrastructure.socio_eco import SocioEco
from chaos.infrastructure.marketing import Marketing
import pandas as pd
import mock


@mock.patch("psycopg2.connect")
def test_create_data(mock_connect):
    mock_con = mock_connect.return_value
    marketing_dataset = Marketing.read()
    socio_dataset = SocioEco.read()
    generate = GenerateDataSet(marketing=marketing_dataset, socio=socio_dataset)
    assert isinstance(generate, GenerateDataSet) == True
