import boto3
from flask import request
from flask import json
from flask import Flask
from sklearn.feature_extraction.text import CountVectorizer
import pickle
import zlib
import base64

#set the S3 bucket name and machine learning model names (which reside on S3)
BUCKET_NAME = 'hw-model-bucket'
MODEL_FILE_NAME = 'LRmodel.pckl'
MODEL_FILE_NAME_2 = 'vocal.pckl'

#define flask app
app = Flask(__name__)
S3 = boto3.client('s3',region_name='us-east-2') #connect to S3 bucket

#define utility dictionary to map identified encoded classes to labels
file_category_mapping = {0: 'DELETION OF INTEREST', 1: 'RETURNED CHECK', 2: 'BILL', 3: 'POLICY CHANGE', 4: 'CANCELLATION NOTICE',
						 5: 'DECLARATION', 6: 'CHANGE ENDORSEMENT', 7: 'NON-RENEWAL NOTICE', 8: 'BINDER', 9: 'REINSTATEMENT NOTICE',
						 10: 'EXPIRATION NOTICE', 11: 'INTENT TO CANCEL NOTICE', 12: 'APPLICATION', 13: 'BILL BINDER'}

#define flask app path
@app.route('/', methods=['GET'])

#lambda function handler
def index():    
    # Parse request for model input 
    data2 = request.args.get('words')
    print(data2)
    data1 = zlib.decompress(base64.b64decode(data2)) #decompress data before applying model
	
    # Load model
    model = load_model(MODEL_FILE_NAME)
    vocab  =load_model(MODEL_FILE_NAME_2)
    count_vect = CountVectorizer(vocabulary=vocab)
    data = count_vect.transform([data1])
    print('prin ended------------------')	
		
	# Make prediction 
    prediction = model.predict(data).tolist()
	
	# Respond with prediction result
    result = {'prediction': file_category_mapping[int(prediction[0])]}    
   
    return json.dumps(result)
	
def load_model(key):    
    # Load model from S3 bucket
    response = S3.get_object(Bucket=BUCKET_NAME, Key=key)
    
	# Load pickle model
    model_str = response['Body'].read()     
    model = pickle.loads(model_str)
    
    return model	

if __name__ == '__main__':
    # listen on all IPs 
    app.run(host='0.0.0.0')