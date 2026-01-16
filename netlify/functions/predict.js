// Mock predict function - returns estimated price based on inputs
// In production, this would load the pickle model

exports.handler = async (event, context) => {
  // Handle CORS preflight
  if (event.httpMethod === 'OPTIONS') {
    return {
      statusCode: 200,
      headers: {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
        'Access-Control-Allow-Headers': 'Content-Type'
      },
      body: JSON.stringify({ message: 'OK' })
    };
  }

  // Only allow POST
  if (event.httpMethod !== 'POST') {
    return {
      statusCode: 405,
      body: JSON.stringify({ error: 'Method Not Allowed' })
    };
  }

  try {
    const body = JSON.parse(event.body);
    const { location, sqft, bhk, bath } = body;

    // Validate inputs
    if (!location || !sqft || !bhk || !bath) {
      return {
        statusCode: 400,
        headers: {
          'Access-Control-Allow-Origin': '*',
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          error: 'Missing required fields: location, sqft, bhk, bath'
        })
      };
    }

    // Simple price estimation formula
    // Base price: 3 lakhs per BHK
    // + 5000 per sq ft
    // + location multiplier (1.0 to 1.5)
    const locationMultiplier = 1.2; // Default multiplier
    const basePrice = (bhk * 300000) + (sqft * 5000);
    const estimatedPrice = Math.round(basePrice * locationMultiplier);

    return {
      statusCode: 200,
      headers: {
        'Access-Control-Allow-Origin': '*',
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        estimated_price: estimatedPrice,
        location: location,
        sqft: sqft,
        bhk: bhk,
        bath: bath
      })
    };
  } catch (error) {
    return {
      statusCode: 500,
      headers: {
        'Access-Control-Allow-Origin': '*',
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        error: `Prediction error: ${error.message}`
      })
    };
  }
};
