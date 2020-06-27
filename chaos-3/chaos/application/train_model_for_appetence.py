# PURPOSE: dump the (stupid) model predicting the appetence score of a customer as a pickle file. If run, the model will train and will be saves in chaos/domain/model.pkl
# EXPLANATION: this file should not be used. It's just the source code of the pickle model for your information

import warnings
warnings.filterwarnings("ignore")


import numpy as np

from sklearn.compose import ColumnTransformer
from sklearn.datasets import fetch_openml
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder

from sklearn.model_selection import train_test_split, GridSearchCV
import joblib

from chaos.settings.base import NUM_FEATURES, CAT_FEATURES, TARGET, MODELS_DIR
import os
import pickle

import numpy as np
from sklearn.ensemble import RandomForestClassifier

import chaos
import chaos.settings.base as base
from os.path import splitext, basename
import logging
base.enable_logging(log_filename=f'{splitext(basename(__file__))[0]}.log', logging_level=logging.DEBUG)

from chaos.infrastructure import generate, marketing, socio_eco

class TrainingPipeline:
    logging.info('--------------------')
    logging.info('Training Pipeline ...')
    def __init__(self, dataset=None):
        self.dataset = dataset
    
    def modify_dataframe_object_type(self):
        self.dataset[CAT_FEATURES] = self.dataset[CAT_FEATURES].astype('category')
        return True
    
    @staticmethod
    def _build_pipeline():
        categorical_features = CAT_FEATURES
        categorical_transformer = Pipeline(steps=[
            ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),
            ('onehot', OneHotEncoder(handle_unknown='ignore'))])

        numeric_features = NUM_FEATURES
        numeric_transformer = Pipeline(steps=[
            ('imputer', SimpleImputer(strategy='median')),
             ('scaler', StandardScaler())])
             
        preprocessor = ColumnTransformer(
            transformers=[
                ('num', numeric_transformer, numeric_features),
                ('cat', categorical_transformer, categorical_features)])
                
        clf = Pipeline(steps=[
            ('preprocessor', preprocessor),
            ('classifier', RandomForestClassifier())])

        return clf

    @staticmethod
    def save_model(model=None):
        logging.info('--------------------')
        logging.info("Save model ...")
        path_to_model = os.path.join(
            MODELS_DIR,
            "{}-{}.pkl".format("ML", "lightgbm"))
        joblib.dump(model, path_to_model)

    def train_model(self):
        _ = self.modify_dataframe_object_type()
        features, target = self.dataset.drop(TARGET, axis=1), self.dataset[TARGET]
        model = self._build_pipeline()
        logging.info('... Preprocessing')
        model.fit(features, target)
        logging.info('... Model Fitting')
        logging.info('... Training Pipeline Done ')
        logging.info('--------------------')
        # load the model in the pickle file
        self.save_model(model)
        logging.info('... Saved Model Done ')
        logging.info('--------------------')






