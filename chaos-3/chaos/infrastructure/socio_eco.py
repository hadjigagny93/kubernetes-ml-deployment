import pandas as pd

from chaos.infrastructure.connexion import Connexion




class SocioEco:
    TABLE = "socio_eco"

    @classmethod
    def read(cls) -> pd.DataFrame:
        engine = Connexion().connect()
        """Returns socio eco data"""
        query = f"SELECT * FROM {cls.TABLE}"
        data = pd.read_sql(query, engine)
        return data