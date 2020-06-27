import os
import logging

# By default the data is stored in this repository's "data/" folder.
# You can change it in your own settings file.
REPO_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
LOGS_DIR = os.path.join(REPO_DIR, 'logs')
MODELS_DIR = os.path.join(REPO_DIR, 'chaos/domain')

# Logging
def enable_logging(log_filename, logging_level=logging.DEBUG):
    """Set loggings parameters.

    Parameters
    ----------
    log_filename: str
    logging_level: logging.level

    """
    with open(os.path.join(LOGS_DIR, log_filename), 'a') as file:
        file.write('\n')
        file.write('\n')

    LOGGING_FORMAT = '[%(asctime)s][%(levelname)s][%(module)s] - %(message)s'
    LOGGING_DATE_FORMAT = '%Y-%m-%d %H:%M:%S'

    logging.basicConfig(
        format=LOGGING_FORMAT,
        datefmt=LOGGING_DATE_FORMAT,
        level=logging_level,
        filename=os.path.join(LOGS_DIR, log_filename)
    )

ON_KEY = "DATE"

NUM_FEATURES = ["AGE", "BALANCE", "NB_CONTACT", "NB_DAY_LAST_CONTACT", "NB_CONTACT_LAST_CAMPAIGN", "EMPLOYMENT_VARIATION_RATE", "IDX_CONSUMER_PRICE","IDX_CONSUMER_CONFIDENCE", "NB_EMPLOYE"]
CAT_FEATURES = ["JOB_TYPE", "STATUS", "EDUCATION", "HAS_DEFAULT", "HAS_HOUSING_LOAN", "HAS_PERSO_LOAN", "CONTACT", "RESULT_LAST_CAMPAIGN"]
TARGET = "SUBSCRIPTION"



