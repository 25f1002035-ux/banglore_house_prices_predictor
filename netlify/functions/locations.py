import json
from pathlib import Path

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
        # Load columns from the model directory
        columns_path = Path(__file__).parent.parent.parent / 'model' / 'columns.json'
        
        with open(columns_path, 'r') as f:
            data_columns = json.load(f)
            columns = data_columns['data_columns']
        
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
    
    except Exception as e:
        return {
            'statusCode': 400,
            'headers': {'Access-Control-Allow-Origin': '*'},
            'body': json.dumps({'error': str(e)})
        }
