import json
import os

def handler(event, context):
    """Netlify Function to get available locations"""
    
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
        # Load columns from model directory
        # In Netlify, files are available at the root level during execution
        columns_file = os.path.join(os.path.dirname(__file__), '..', '..', 'model', 'columns.json')
        
        # If that doesn't work, try the absolute path used during build
        if not os.path.exists(columns_file):
            # Try from the build output directory
            columns_file = '/var/task/model/columns.json'
        
        if not os.path.exists(columns_file):
            # Try from current working directory
            columns_file = 'model/columns.json'
        
        with open(columns_file, 'r') as f:
            data_columns = json.load(f)
            columns = data_columns.get('data_columns', [])
        
        if not columns:
            return {
                'statusCode': 500,
                'headers': {'Access-Control-Allow-Origin': '*'},
                'body': json.dumps({'error': 'No columns found in data_columns'})
            }
        
        # Extract locations (all columns except the first 3 which are sqft, bath, bhk)
        locations = sorted([col.title() for col in columns[3:]])
        
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Content-Type': 'application/json'
            },
            'body': json.dumps({
                'locations': locations,
                'count': len(locations)
            })
        }
    
    except FileNotFoundError as e:
        return {
            'statusCode': 404,
            'headers': {'Access-Control-Allow-Origin': '*'},
            'body': json.dumps({'error': f'File not found: {str(e)}'})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {'Access-Control-Allow-Origin': '*'},
            'body': json.dumps({'error': f'Error: {str(e)}'})
        }
