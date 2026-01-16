import json
import pickle
import numpy as np
import os
from pathlib import Path

# Load model and columns
model_path = Path(__file__).parent.parent.parent / 'model' / 'banglore_home_prices_model.pickle'
columns_path = Path(__file__).parent.parent.parent / 'model' / 'columns.json'

with open(model_path, 'rb') as f:
    model = pickle.load(f)

with open(columns_path, 'r') as f:
    data_columns = json.load(f)
    columns = data_columns['data_columns']

def handler(event, context):
    """Netlify Function to predict house prices"""
    
    # Handle CORS preflight
    if event['httpMethod'] == 'OPTIONS':
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
                'Access-Control-Allow-Headers': 'Content-Type'
            },
            'body': json.dumps({'message': 'OK'})
        }
    
    try:
        body = json.loads(event['body'])
        
        location = body.get('location')
        sqft = float(body.get('sqft'))
        bhk = int(body.get('bhk'))
        bath = int(body.get('bath'))
        
        # Create feature vector
        x = np.zeros(len(columns))
        x[0] = sqft
        x[1] = bath
        x[2] = bhk
        
        # Get location index
        try:
            location_idx = columns.index(location.lower())
            x[location_idx] = 1
        except (ValueError, AttributeError):
            x[-1] = 1  # Default location
        
        # Make prediction
        prediction = model.predict([x])[0]
        
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Content-Type': 'application/json'
            },
            'body': json.dumps({
                'estimated_price': round(prediction, 2),
                'location': location,
                'sqft': sqft,
                'bhk': bhk,
                'bath': bath
            })
        }
    
    except Exception as e:
        return {
            'statusCode': 400,
            'headers': {'Access-Control-Allow-Origin': '*'},
            'body': json.dumps({'error': str(e)})
        }
