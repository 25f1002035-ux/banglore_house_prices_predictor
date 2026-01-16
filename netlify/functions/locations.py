import json
import os

# Hardcoded locations as fallback - these are extracted from columns.json
# This ensures the API always works on Netlify even if file loading fails
DEFAULT_LOCATIONS = [
    "1st Block Jayanagar",
    "1st Phase JP Nagar",
    "2nd Phase Judicial Layout",
    "Adarsh Palm Retreat",
    "Aero Park",
    "Agaram",
    "Agloor",
    "Agram",
    "Akenhalli",
    "Aksharanagar",
    "Alathur",
    "Aleksandar Road",
    "Allalasandra",
    "Ananthapura",
    "Ananth Nagar",
    "Anbagaram",
    "Anchepalya",
    "Andrahalli",
    "Anjanapura",
    "Antriksh Bhawan",
    "Anugraha",
    "Aparadh Nagar",
    "Apollo",
    "Appughar",
    "Aqualake",
    "Arayanakere",
    "Arcot Road Saidapet",
    "Ardee Village",
    "Arekere",
    "Aris Village"
]

def handler(event, context):
    """Netlify Function to get available locations"""
    try:
        # Start with default locations
        locations = DEFAULT_LOCATIONS.copy()
        
        # Try to load from columns.json in model folder
        columns_path = os.path.join(os.path.dirname(__file__), '..', '..', 'model', 'columns.json')
        
        if os.path.exists(columns_path):
            try:
                with open(columns_path, 'r') as f:
                    data = json.load(f)
                    columns = data.get('data_columns', [])
                    # Extract locations from columns (skip first 3: sqft, bath, bhk)
                    if columns and len(columns) > 3:
                        locations = sorted([col.title() for col in columns[3:]])
            except Exception as e:
                print(f"Error loading columns.json: {e}")
                # Use default locations on error
        
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
                'Content-Type': 'application/json'
            },
            'body': json.dumps({
                'locations': locations,
                'count': len(locations)
            })
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Content-Type': 'application/json'
            },
            'body': json.dumps({
                'error': f'Error loading locations: {str(e)}',
                'locations': DEFAULT_LOCATIONS,
                'count': len(DEFAULT_LOCATIONS)
            })
        }
