// Hardcoded locations for Bangalore
const DEFAULT_LOCATIONS = [
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
];

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

  try {
    return {
      statusCode: 200,
      headers: {
        'Access-Control-Allow-Origin': '*',
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        locations: DEFAULT_LOCATIONS,
        count: DEFAULT_LOCATIONS.length
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
        error: `Error loading locations: ${error.message}`,
        locations: DEFAULT_LOCATIONS,
        count: DEFAULT_LOCATIONS.length
      })
    };
  }
};
