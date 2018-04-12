# FileClassifier Models & REST API - Classification Test

Helping train AIVA.

## Getting Started

REST API deploy on AWS infrastrcture: https://rb2pqd7dte.execute-api.us-east-2.amazonaws.com/dev

This repository holds the classification model elements used to build the document classifier. Additionally, it describes the details of the application infrastructure.

### Libraries Used

The following libraries/dependecies have been used for development

```
Libraries-Python 3: Flask [API creation], zappa [AWS Lambda - continuous deployment], sklearn [classification model]

Systems : AWS S3, AWS Lambda, AWS API Gateway, AWS EC2

Classification Model: Logistic Regression ; Accuracy - 86%
```

### Details

1. Lambda_Function_Handler
```
Contains the 'fileclassify.py' file which serves as the container of the primary lambda function handler. This has been packaged aling with the dependencies and deployed on AWS.
```
2. Python Notebook - Classification
```
Includes the logical flow of the approach followed for building the classification model. Contains the model impementation, metrics, and confusion martrix. Also, contains the 'pckl'(pickle) files which correspond to the saved model to be used for prediction, and the vocabulary reference for the count vectorizer utilized for building the model.
```
3. Test Data
```
Includes the 'test_data.csv' which corresponds to the 10% split of the provided data to be used for testing (x,y test). The content column data can be pasted in the web application input to test the prediction outcome.
```

