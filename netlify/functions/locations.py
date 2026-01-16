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
        # Load columns from model directory with multiple path fallbacks
        # Primary location is server/artifacts (matching util.py)
        columns_paths = [
            os.path.join(os.path.dirname(__file__), '..', '..', 'server', 'artifacts', 'columns.json'),
            '/var/task/server/artifacts/columns.json',
            'server/artifacts/columns.json',
            os.path.join(os.path.dirname(__file__), '..', '..', 'model', 'columns.json'),
            '/var/task/model/columns.json',
            'model/columns.json'
        ]
        
        columns_file = None
        for path in columns_paths:
            if os.path.exists(path):
                columns_file = path
                break
        
        if not columns_file:
            return {
                'statusCode': 404,
                'headers': {'Access-Control-Allow-Origin': '*'},
                'body': json.dumps({'error': f'Columns file not found. Tried: {columns_paths}'})
            }
        
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
        # Locations are at indices 3 onwards
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
    except json.JSONDecodeError as e:
        return {
            'statusCode': 400,
            'headers': {'Access-Control-Allow-Origin': '*'},
            'body': json.dumps({'error': f'Invalid JSON in columns file: {str(e)}'})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {'Access-Control-Allow-Origin': '*'},
            'body': json.dumps({'error': f'Error loading locations: {str(e)}'})
        }
