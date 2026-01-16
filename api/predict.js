export default function handler(req, res) {
    if (req.method === 'OPTIONS') {
          res.setHeader('Access-Control-Allow-Origin', '*');
          res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
          res.setHeader('Access-Control-Allow-Headers', 'Content-Type');
          return res.status(200).json({ message: 'OK' });
        }
    if (req.method !== 'POST') {
          return res.status(405).json({ error: 'Method not allowed' });
        }
    try {
          const { location, sqft, bhk, bath } = req.body;
          if (!location || !sqft || !bhk || !bath) {
                  return res.status(400).json({ error: 'Missing required fields' });
                }
          const sqftNum = parseFloat(sqft);
          const bhkNum = parseInt(bhk);
          const bathNum = parseInt(bath);
          let basePrice = (bhkNum * 300000) + (sqftNum * 5000);
          let multiplier = 1.2;
          const estimatedPrice = Math.round(basePrice * multiplier / 100000) / 10;
          return res.status(200).json({
                  estimated_price: estimatedPrice,
                  location: location,
                  sqft: sqftNum,
                  bhk: bhkNum,
                  bath: bathNum
                });
        } catch (error) {
          return res.status(500).json({ error: error.message });
        }
  }
