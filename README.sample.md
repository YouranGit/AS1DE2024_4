<img src="./images/Flag_of_California.svg.png" alt="Logo of the project" align="right" width="150" height="100"> 

# Design and Implementation of MLOps for an ML Application: California Housing Prices &middot; [![Build Status](https://img.shields.io/travis/npm/npm/latest.svg?style=flat-square)](https://travis-ci.org/npm/npm) [![npm](https://img.shields.io/npm/v/npm.svg?style=flat-square)](https://www.npmjs.com/package/npm) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com) [![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square)](https://github.com/your/your-project/blob/master/LICENSE)
> This project provides an API for predicting California housing prices based on various features of the dataset included. The repository includes a Jupyter notebook for initial analysis and model training, cloud build configurations, and a Dockerized API for making predictions.

---

## Features
- **Machine Learning Model**: Utilizes the California housing dataset to train a predictive model.
- **Dockerized API**: The `prediction-api` directory contains code to deploy the model as an API.
- **Cloud Build Configurations**: JSON files for setting up automated builds.

---
## Installing / Getting started

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/California_Housing_Predictor.git
   cd California_Housing_Predictor

   
Acces the API at http://localhost:5000.

## Developing

### Built With
- **Python 3.8+**: Core language used for data analysis, model building, and API creation.
- **Flask**: Used to create the API in `app.py`.
- **Docker**: Containerizes the API for easy deployment.
- **Google Cloud Build**: Configurations included for automated deployment in the cloud.

### Prerequisites
- **Python 3.8 or higher**
- **Docker** (for building and deploying the API)
- **Jupyter Notebook** (optional, for local development and testing of the notebook)
- **Google Cloud Account** (for cloud deployment if using Cloud Build)


### Setting up Dev

Here's a brief intro about what a developer must do in order to start developing
the project further:

1. **Clone the repository**
  ```bash
  git clone https://github.com/yourusername/California_Housing_Predictor.git
  cd California_Housing_Predictor
```

2. **Setup virtual environment**
   ```bash
   python3 -m venv env
   source env/bin/activate

3. **Install dependencies**
   ```bash
   pip install -r prediction-api/requirements.txt

4. **Run API locally**
   ```bash
   docker build -t california_housing_predictor .
   docker run -p 5000:5000 california_housing_predictor

First step is for cloning the repository. The second step sets up a virtual environment for Python where the program can run in. The third step consists of installing the required libraries/dependencies to run the API.  These are:

- **setuptools**
- **flask**
- **pandas**
- **keras**
- **tensorflow**
- **numpy**
- **h5py**
- **six**
- **joblib**
- **scikit-learn**
- **google-cloud-storage**



The final step runs the API in the virtual environment.


### Building

```shell
docker build -t california_housing_predictor ./prediction-api
```

The code above builds the Docker image to package the API:

### Deploying / Publishing

```shell
docker run -p 5000:5000 california_housing_predictor
```

Access the API at http://localhost:5000.

**Google Cloud Deployment** (optional):
Configure and deploy with Cloud Build:
The JSON configurations (cloud_build_app_mlp_automated.json, etc.) contain the steps for Google Cloud.
Ensure your Google Cloud project is set up and has necessary permissions.

```shell
gcloud builds submit --config cloud_build_ml_app.json
```

## Versioning

This project uses Semantic Versioning. Versions are tagged as vMAJOR.MINOR.PATCH, reflecting new features, changes, and fixes respectively.


## Configuration

Configurations for deployment are stored in the cloud_build_app_mlp_automated.json and other cloud build JSON files. API settings can be modified in app.py.

## Tests

Tests can be added to validate the model and API. To run tests, add test cases within tests/ (if this directory does not exist, create it) and use pytest:

Install testing dependencies (add pytest to requirements.txt):

```shell
pip install pytest
```

```shell
pytest tests/
```

## Style guide

This project follows PEP 8 style guidelines for Python code. Ensure code is formatted using a linter, such as flake8:

```shell
pip install flake8
```

```shell
flake8 prediction-api/
```

The code above installs flake8 and runs it.

## API Reference

Endpoint: /predict
Method: POST
Description: Predicts housing prices based on provided feature values.
Payload:

```shell
{
    "feature1": value1,
    "feature2": value2,
    ...
}
```
Response:
Returns a JSON object with predicted price:

```shell
{
    "prediction": 123456
}

```
Usage example:

```shell
curl -X POST -H "Content-Type: application/json" -d '{"feature1": value1, "feature2": value2}' http://localhost:5000/predict
```

## Database

The dataset is a modified version of the California Housing Data used in the paper Pace, R. Kelley, and Ronald Barry. "Sparse spatial autoregressions." Statistics & Probability Letters 33.3 (1997): 291-297..

The data contains information from the 1990 California census. So although it may not help you with predicting current housing prices like the Zillow Zestimate dataset, it does provide an accessible introductory dataset for teaching people about the basics of machine learning.

The data pertains to the houses found in a given California district and some summary stats about them based on the 1990 census data. The columns are as follows, their names are pretty self-explanatory:

- 1) Median House Value: Median house value for households within a block (measured in US Dollars) [$]
- 2) Median Income: Median income for households within a block of houses (measured in tens of thousands of US Dollars) [10k$]
- 3) Median Age: Median age of a house within a block; a lower number is a newer building [years]
- 4) Total Rooms: Total number of rooms within a block
- 5) Total Bedrooms: Total number of bedrooms within a block
- 6) Population: Total number of people residing within a block
- 7) Households: Total number of households, a group of people residing within a home unit, for a block
- 8) Latitude: A measure of how far north a house is; a higher value is farther north [°]
- 9) Longitude: A measure of how far west a house is; a higher value is farther west [°]
- 10) Distance to coast: Distance to the nearest coast point [m]
- 11) Distance to Los Angeles: Distance to the centre of Los Angeles [m]
- 12) Distance to San Diego: Distance to the centre of San Diego [m]
- 13) Distance to San Jose: Distance to the centre of San Jose [m]
- 14) Distance to San Francisco: Distance to the centre of San Francisco [m]

Source: https://www.kaggle.com/datasets/fedesoriano/california-housing-prices-data-extra-features.

## Licensing

This project is licensed under the MIT License.
