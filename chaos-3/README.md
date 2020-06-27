# Project 3 : Bénédicte, El Hadji, Juan 

The current project is aim to deploy a Machine Learning Model into production environments, using some cloud technologies such as Docker and Kubernetes.

## User Guide - API Reference 
The solution includes an application for external users. This application take some potential client features, and returns the subscription forecast through an API rest.

### Score
The flask API provides you with a subscription forecast for a potential client.

```
POST /score
```

#### Parameters
**DATE** *"YYYY-MM-DD"*: Last day of contact.

---
**AGE** *int*: Age (in years).

---
**JOB_TYPE** *string*: Type of job.

---
**STATUS** *string*: Civil status.

---
**EDUCATION** *string*: Education level.

---
**HAS_DEFAULT** *string*: The client has previously default or not.

---
**BALANCE** *float*: Current account balance.

---
**HAS_HOUSING_LOAN** *string*: The client holds a real state loan.

---
**HAS_PERSO_LOAN** *string*: The client holds a personal loan.

---
**CONTACT** *string*: Communication channel.

---
**DURATION_CONTACT** *float*: Last contact duration in seconds.

---
**NB_CONTACT** *integer*: Number of contacts with the client during current campaign.

---
**NB_DAY_LAST_CONTACT** *integer*: Number of days since the last contact with the client for previous campaign (999: the client has not been previously reached).

---
**NB_CONTACT_LAST_CAMPAIGN** *integer*: Number of contacts with the client for previous campaigns.

---
**RESULT_LAST_CAMPAIGN** *string*: Result from the previous Marketing Campaign.

---
**EMPLOYMENT_VARIATION_RATE** *float*: Monthly Employment Variation Rate.

---
**IDX_CONSUMER_PRICE** *float*: Monthly Consumer Price Index.

---
**IDX_CONSUMER_CONFIDENCE** *float*: Monthly Consumer Confidence Index.

---
**NB_EMPLOYEE** *float*: Quarterly Number of Employees.

---
#### Returns
**SUBSCRIPTION** *% Yes/No*: Returns the subscription probability and whether the client will subscribe or not.

---
In order to test the API the following information is required:
* IP Address: run in terminal and copy the corresponding **EXTERNAL-IP** to *chaos-3-loadbalancer-master*
```
kubectl get services
```
* Port: 5000

* Input: .json file with client information collected by marketing

* Output: Subscription probability and Yes/No

You can run the following command in the terminal to test the API, using a random client information:

```
POST /customers

curl http://<host>:5000/score --request POST --data '{"marketing":{"DATE": "2008-05-05",
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
 "RESULT_LAST_CAMPAIGN": "nan"}}' --header "Content-Type: application/json"
```

## Developer Guide

Before to start this project, please check if you have installed Docker, Kubernetes, Google Cloud SDK..

### 0. Clone this repository
```
$ git clone https://gitlab.com/yotta-academy/cohort-2020/projects/ml-prod-projects/chaos-3.git
$ cd chaos-3
```
### 1. Setup your virtual environment and activate it
To setup your virtual environnement, you have to use Pyenv with python 3.8.1.
```
$ git clone https://github.com/yyuu/pyenv-virtualenv.git ~/.pyenv/plugins/pyenv-virtualenv
$ pyenv install 3.8.1
$ pyenv virtualenv <python_version> <environment_name>
```
Put this code on file .bashrc to have your environment activate when you are in the folder chaos-3
```
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```
or on terminal
```
$ pyenv activate <environment_name>
$ pip install -e ./
```

Now python3.8.1 and your environment virtual are installed !

### 2. Run for installing dependencies
```
$ pip install -r requirements.txt

```
### 3. Running Test

To test your application, you must launch the three commands. If you are setting up the environment for the first time, you will receive the credentials by email (a key.json file for the link between the python application and cloud SQL, and a config.yml file with database credentials).

#### 3.1 Open connection to the database on GCP
First, you must download https://cloud.google.com/sql/docs/postgres/sql-proxy

```
$ ./cloud_sql_proxy -instances=yotta-ml3:europe-west1:uranus=tcp:5432
```

#### 3.2  Open server API with a command python

```
$ python chaos/application/server.py
```

#### 3.3  Test API in local
```
$ curl http://<host>:5000/score --request POST --data '{"marketing":{"DATE": "2008-05-05",
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
 "RESULT_LAST_CAMPAIGN": "nan"}}' --header "Content-Type: application/json"
```


### 4. Coverage 
You can test coverage, as proposed in <https://pypi.org/project/pytest-cov/>
```
pip install pytest-cov

```
```
pytest --cov=chaos chaos/test/unit

```

## Architecture 
```
.
├── chaos
│   │
│   ├── application
│   │   ├── server.py
│   │   └── train_model_for_appetence.py
│   │
│   ├── domain
│   │   ├── ML-lightgbm.pkl
│   │   └── customer.py
│   │
│   ├── infrastructure
│   │   ├── config
│   │   │   └── config.py
│   │   ├── connexion.py
│   │   ├── generate.py
│   │   ├── marketing.py
│   │   └── socio_eco.py
│   │
│   ├── settings
│   │   ├── __init__.py
│   │   └── base.py
│   │
│   └── test
│       ├── functional
│       │      └── test_server.py
│       │
│       └── unit
│           ├── application
│           │   ├── test_server.py
│           │   └── test_train_model_for_appetence.py
│           │
│           ├── domain
│           │   └── test_customer.py
│           │
│           └── infrastructure
│               ├── test_connexion.py
│               ├── test_generate.py
│               ├── test_marketing.py
│               └── test_socio_eco.py
│   
├── deployment
│   ├── chaos-deployment-develop.yml
│   ├── chaos-deployment-master.yml
│   ├── chaos-deployment-staging.yml
│   ├── loadbalancer-develop.yml
│   ├── loadbalancer-master.yml
│   └── loadbalancer-staging.yml
├── doc
│   └── Projet 3 - Enoncé.pdf
├── logs
│   └── .gitignore
├── notebook
│   └── prod.ipynb
├── Dockerfile
├── README.md
├── requirements.txt
└── setup.py
```
