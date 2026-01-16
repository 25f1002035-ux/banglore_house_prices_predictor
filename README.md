# Bangalore House Prices Predictor

A machine learning application that predicts house prices in Bangalore based on various features such as location, size, age, and amenities. This project combines a Python-based backend with a modern web frontend for an interactive user experience.

## Features

- **Machine Learning Model**: Trained on extensive Bangalore housing data for accurate price predictions
- **Interactive Web Interface**: User-friendly UI with location-based price estimation
- **REST API**: Backend API for seamless integration with the frontend
- **Multiple Deployment Options**: Support for Vercel, Netlify, and Docker containerization
- **240+ Locations**: Comprehensive coverage of Bangalore localities
- **Real-time Predictions**: Get instant price estimates based on input parameters

## Project Structure

```
banglore_house_prices_predictor/
├── api/                    # API endpoints for predictions
├── client/                 # React/Vue frontend application
├── server/                 # Flask/Node.js backend server
├── model/                  # ML model and training files
├── netlify/functions/      # Netlify serverless functions
├── public/                 # Static assets
├── Dockerfile              # Docker configuration
├── requirements.txt        # Python dependencies
├── vercel.json            # Vercel deployment config
└── README.md              # Project documentation
```

## Tech Stack

### Backend
- **Python**: Machine learning and data processing
- **Flask/Node.js**: REST API server
- **scikit-learn**: ML model training and prediction
- **pandas**: Data manipulation and preprocessing

### Frontend
- **HTML/CSS/JavaScript**: Core web technologies
- **Interactive UI**: Location dropdown with 240+ Bangalore localities
- **Responsive Design**: Works across devices

### Deployment
- **Vercel**: Frontend and API hosting
- **Netlify**: Alternative frontend deployment
- **Docker**: Container-based deployment

## Installation

### Prerequisites
- Python 3.8+
- Node.js 14+ (for frontend)
- Git

### Local Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/25f1002035-ux/banglore_house_prices_predictor.git
   cd banglore_house_prices_predictor
   ```

2. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up the server**
   ```bash
   cd server
   python app.py
   ```

4. **Run the frontend** (in a new terminal)
   ```bash
   cd client
   # Open index.html in a browser or serve via Python
   python -m http.server 8000
   ```

## Usage

1. Open the web application in your browser
2. Select a location from the dropdown (240+ options available)
3. Enter property details:
   - Size (in sqft)
   - Number of bedrooms
   - Age/Year built
   - Other amenities
4. Click "Predict" to get the estimated price
5. View results instantly

## API Endpoints

### Predict Price
```
POST /api/predict
Content-Type: application/json

Request Body:
{
  "location": "Bangalore",
  "size": 1200,
  "bedrooms": 3,
  "year": 2010
}

Response:
{
  "predicted_price": 5500000,
  "confidence": 0.85
}
```

## Deployment

### Vercel Deployment
See `VERCEL_DEPLOYMENT.md` for detailed instructions.

### Netlify Deployment
See `NETLIFY_DEPLOYMENT.md` for detailed instructions.

### Docker Deployment
See `DEPLOYMENT_GUIDE.md` for comprehensive deployment options.

## Model Details

- **Algorithm**: Regression-based ML model (scikit-learn)
- **Features**: Location, size, bedrooms, age, amenities
- **Training Data**: Bangalore housing market data
- **Accuracy**: Model trained for optimal prediction accuracy
- **Preprocessing**: Feature scaling and encoding for locations

## File Structure

- `api/`: Vercel API routes
- `client/`: Frontend HTML with location dropdown and prediction form
- `model/`: Trained ML model files
- `server/`: Backend application
- `netlify/functions/`: Netlify serverless functions
- `public/`: Static files
- `DEPLOYMENT_GUIDE.md`: General deployment instructions
- `VERCEL_DEPLOYMENT.md`: Vercel-specific setup
- `NETLIFY_DEPLOYMENT.md`: Netlify-specific setup
- `Dockerfile`: Docker container configuration
- `requirements.txt`: Python package dependencies

## Performance

- **Deployments**: 36+ active deployments
- **Languages**: Jupyter Notebook (86.1%), HTML (7.1%), JavaScript (3.1%), Python (2.9%)
- **Commits**: 46+ commits in development history

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create a new branch (`git checkout -b feature/improvement`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some feature'`)
5. Push to the branch (`git push origin feature/improvement`)
6. Open a Pull Request

## License

This project is open source and available under the MIT License.

## Contact

For questions or feedback, please reach out through GitHub issues or contact the maintainer.

## Acknowledgments

- Built as part of data science and machine learning practice
- Trained on real Bangalore housing market data
- Deployed successfully across multiple platforms

---

**Last Updated**: January 2026
**Status**: Active Development
