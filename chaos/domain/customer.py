import os
import joblib 
import pandas as pd 
from chaos.infrastructure import generate, marketing, socio_eco
from chaos.settings.base import MODELS_DIR
import chaos.settings.base as base
from os.path import splitext, basename
import logging
base.enable_logging(log_filename=f'{splitext(basename(__file__))[0]}.log', logging_level=logging.DEBUG)

class Customer:
    MODEL_PATH = os.path.join(MODELS_DIR, "ML-lightgbm.pkl")

    def __init__(self, marketing: dict):
        """
        Parameters
        ----------
        marketing: dict
            marketing data, used as features for prediction. At the moment, only the following keys are used: 'AGE', 'BALANCE'
        """
        self.marketing = pd.DataFrame.from_dict(marketing, orient='index').T

    def get_model(self):
        if not os.path.exists(self.MODEL_PATH):
            training_pipeline_instance = TrainingPipeline(
                dataset=generate.GenerateDataSet(
                    marketing=marketing.Marketing.read(),
                    socio=socio_eco.SocioEco.read()
                    ).create_data())
            training_pipeline_instance.train_model()
        
        model = joblib.load(self.MODEL_PATH)
        return model
        

    def predict_subscription(self) -> float:
        """Returns appetence score [0,1] of the customer predicted by the model
        
        Returns
        -------
        appetence: float
            appetence of the customer to the bank loan (0: not appetent, 1: very appetent)

        Explanation
        -----------
        We construct the features from the caracteristics and the socio economic data.
        At the moment, we use arbitrary features. This should be changed.
        """
        model = self.get_model()
        client_data = generate.GenerateDataSet(
            marketing=self.marketing,
            socio=socio_eco.SocioEco.read()
            ).create_data().head(1)
            
        return model.predict_proba(client_data)[0][1]

