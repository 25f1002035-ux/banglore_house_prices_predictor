from flask import Flask, request, jsonify
import util  # util.get_location_names() will auto-load

app = Flask(__name__)

@app.route('/')
def home():
    locations = util.get_location_names()
    sample = locations[:10]
    return f"""
    <h1>🏠 Bangalore Home Price Prediction</h1>
    <p>📍 <b>{len(locations)}</b> locations loaded</p>
    <h3>Sample (first 10):</h3>
    <ul>{''.join(f'<li>{loc}</li>' for loc in sample)}</ul>
    <p><a href="/get_location_names">Full JSON List</a></p>
    """


@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    total_sqft=float(request.form['total_sqft'])
    location=request.form['location']
    bhk=int(request.form['bhk'])
    bath=int(request.form['bath'])
    response=jsonify({
        'estimated_price':util.predict_price(location,total_sqft,bhk,bath)
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

@app.route('/get_location_names')
def get_location_names():
    response = jsonify({'locations': util.get_location_names()})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == "__main__":
    print("Starting Python Flask Server for home price prediction")
    util.load_saved_artifacts()
    print("🌐 Visit http://127.0.0.1:5000/")
    app.run(debug=True, host='127.0.0.1', port=5000)
