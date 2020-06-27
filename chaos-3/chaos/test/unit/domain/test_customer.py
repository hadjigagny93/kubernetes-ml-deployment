import warnings
from chaos.domain.customer import Customer
from sklearn.pipeline import Pipeline 
from chaos.infrastructure.marketing import Marketing
import pandas as pd
import mock 
from chaos.infrastructure.generate import GenerateDataSet





dataframe = pd.DataFrame.from_dict({'AGE': {0: 58},
 'JOB_TYPE': {0: 'Manager'},
 'STATUS': {0: 'Marié'},
 'EDUCATION': {0: 'Tertiaire'},
 'HAS_DEFAULT': {0: 'No'},
 'BALANCE': {0: 2143},
 'HAS_HOUSING_LOAN': {0: 'Yes'},
 'HAS_PERSO_LOAN': {0: 'No'},
 'CONTACT': {0: 'nan'},
 'NB_CONTACT': {0: 1},
 'NB_DAY_LAST_CONTACT': {0: -1},
 'NB_CONTACT_LAST_CAMPAIGN': {0: 0},
 'RESULT_LAST_CAMPAIGN': {0: 'nan'},
 'SUBSCRIPTION': {0: 'No'},
 'EMPLOYMENT_VARIATION_RATE': {0: 1.1},
 'IDX_CONSUMER_PRICE': {0: 93.994},
 'IDX_CONSUMER_CONFIDENCE': {0: -36.4},
 'NB_EMPLOYE': {0: 5191.0}})

#@mock.patch.object(GenerateDataSet, "create_data")    
@mock.patch("psycopg2.connect")
def test_predict_subscription(mock_connect):

    warnings.filterwarnings("ignore")
    mock_con = mock_connect.return_value
    customer_instance = Customer(
        marketing={
            "DATE": "2008-05-05",
            "AGE": 58,
            "JOB_TYPE": "Manager",
            "STATUS": "Marié",
            "EDUCATION": "Tertiaire",
            "HAS_DEFAULT": "No",
            "BALANCE": 2143,
            "HAS_HOUSING_LOAN": "Yes",
            "HAS_PERSO_LOAN": "No",
            "CONTACT": "nan",
            "DURATION_CONTACT": 261,
            "NB_CONTACT": 1,
            "NB_DAY_LAST_CONTACT": -1,
            "NB_CONTACT_LAST_CAMPAIGN": 0,
            "RESULT_LAST_CAMPAIGN": "nan"})

    with mock.patch.object(GenerateDataSet, "create_data") as mock_foo:
        mock_foo.return_value = dataframe
        assert isinstance(customer_instance.predict_subscription(), float) == True
