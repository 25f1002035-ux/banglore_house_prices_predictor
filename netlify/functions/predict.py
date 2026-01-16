import json
import pickle
import numpy as np
import os

# Load model and columns with multiple path fallbacks
def load_model_and_columns():
    """Load model and columns with fallback paths for Netlify"""
    
    # Try different paths
    model_paths = [
        os.path.join(os.path.dirname(__file__), '..', '..', 'model', 'banglore_home_prices_model.pickle'),
        '/var/task/model/banglore_home_prices_model.pickle',
        'model/banglore_home_prices_model.pickle'
    ]
    
    columns_paths = [
        os.path.join(os.path.dirname(__file__), '..', '..', 'model', 'columns.json'),
        '/var/task/model/columns.json',
        'model/columns.json'
    ]
    
    model_path = None
    columns_path = None
    
    for path in model_paths:
        if os.path.exists(path):
            model_path = path
            break
    
    for path in columns_paths:
        if os.path.exists(path):
            columns_path = path
            break
    
    if not model_path:
        raise FileNotFoundError(f"Model file not found in any of these paths: {model_paths}")
    if not columns_path:
        raise FileNotFoundError(f"Columns file not found in any of these paths: {columns_paths}")
    
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
    
    with open(columns_path, 'r') as f:
        data_columns = json.load(f)
        columns = data_columns.get('data_columns', [])
    
    return model, columns

# Load once at startup
try:
    model, columns = load_model_and_columns()
except Exception as e:
    model = None
    columns = []
    load_error = str(e)

def handler(event, context):
    """Netlify Function to predict house prices"""
    
    # Check if model loaded
    if not model:
        return {
            'statusCode': 500,
            'headers': {'Access-Control-Allow-Origin': '*'},
            'body': json.dumps({'error': f'Model not loaded: {load_error}'})
        }
    
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
        
        location = body.get('location', '').lower()
        sqft = float(body.get('sqft', 0))
        bhk = int(body.get('bhk', 0))
        bath = int(body.get('bath', 0))
        
        if not all([location, sqft, bhk, bath]):
            return {
                'statusCode': 400,
                'headers': {'Access-Control-Allow-Origin': '*'},
                'body': json.dumps({'error': 'Missing required fields: location, sqft, bhk, bath'})
            }
        
        # Create feature vector
        x = np.zeros(len(columns))
        x[0] = sqft
        x[1] = bath
        x[2] = bhk
        
        # Get location index
        location_found = False
        for i, col in enumerate(columns):
            if col.lower() == location:
                x[i] = 1
                location_found = True
                break
        
        if not location_found:
            # Use the first available location as default
            if len(columns) > 3:
                x[3] = 1
        
        # Make prediction
        prediction = model.predict([x])[0]
        
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Content-Type': 'application/json'
            },
            'body': json.dumps({
                'estimated_price': round(float(prediction), 2),
                'location': location,
                'sqft': sqft,
                'bhk': bhk,
                'bath': bath
            })
        }
    
    except json.JSONDecodeError:
        return {
            'statusCode': 400,
            'headers': {'Access-Control-Allow-Origin': '*'},
            'body': json.dumps({'error': 'Invalid JSON in request body'})
        }
    except ValueError as e:
        return {
            'statusCode': 400,
            'headers': {'Access-Control-Allow-Origin': '*'},
            'body': json.dumps({'error': f'Invalid input values: {str(e)}'})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {'Access-Control-Allow-Origin': '*'},
            'body': json.dumps({'error': f'Prediction error: {str(e)}'})
        }
