# Bangalore House Prices Predictor - Deployment Guide

## Project Overview
This is a machine learning web application that predicts house prices in Bangalore using a trained Random Forest model. The project consists of:
- **Backend**: Flask API (Python)
- **Frontend**: HTML/CSS/JavaScript
- **Model**: Pre-trained scikit-learn model (pickle file)

## Deployment Files Created
The following files have been added to support deployment:

### 1. **requirements.txt**
Python dependencies needed to run the application:
- Flask 2.3.0
- Flask-Cors 4.0.0
- NumPy 1.24.3
- scikit-learn 1.3.0
- Gunicorn 21.2.0
- python-dotenv 1.0.0

### 2. **Procfile**
For Heroku deployment. Specifies how to run the application using Gunicorn.

### 3. **Dockerfile**
For Docker containerization. Allows running the app in any Docker-compatible environment.

### 4. **.gitignore**
Prevents sensitive files and cache from being committed:
- __pycache__ directories
- Virtual environments
- .env files
- IDE settings
- OS files

---

## Deployment Options

### Option 1: Deploy on Heroku (Recommended for Beginners)

#### Prerequisites:
- Heroku account (free at heroku.com)
- Heroku CLI installed
- Git installed

#### Steps:

1. **Create Heroku Account**
   - Go to https://www.heroku.com
   - Sign up for free account

2. **Install Heroku CLI**
   ```bash
   # On Windows, use installer from https://devcenter.heroku.com/articles/heroku-cli
   # Or via npm:
   npm install -g heroku
   ```

3. **Initialize Git Repository (if not already done)**
   ```bash
   git init
   git add .
   git commit -m "Add deployment files"
   ```

4. **Login to Heroku**
   ```bash
   heroku login
   ```

5. **Create Heroku App**
   ```bash
   heroku create your-app-name
   ```

6. **Deploy to Heroku**
   ```bash
   git push heroku main
   ```

7. **View Logs**
   ```bash
   heroku logs --tail
   ```

8. **Your app is live at**
   ```
   https://your-app-name.herokuapp.com
   ```

**Cost**: Free tier available (limited dyno hours)

---

### Option 2: Deploy on Render.com (Free Alternative)

#### Prerequisites:
- Render account (free at render.com)
- GitHub repository

#### Steps:

1. **Push code to GitHub**
   ```bash
   git add .
   git commit -m "Add deployment files"
   git push origin main
   ```

2. **Go to Render Dashboard**
   - Visit https://render.com
   - Sign up with GitHub account
   - Click "New" → "Web Service"

3. **Connect GitHub Repository**
   - Select your banglore_house_prices_predictor repository
   - Connect

4. **Configure Build and Deploy Settings**
   - **Name**: your-app-name
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn -w 4 -b 0.0.0.0:5000 --chdir server server:app`
   - **Instance Type**: Free (for testing)

5. **Deploy**
   - Click "Create Web Service"
   - Render will automatically deploy

6. **Your app is live at**
   ```
   https://your-app-name.onrender.com
   ```

**Cost**: Free tier with limitations, then pay-as-you-go

---

### Option 3: Deploy with Docker (Advanced)

#### Prerequisites:
- Docker installed
- Docker Hub account (optional, for hosting images)

#### Steps:

1. **Build Docker Image**
   ```bash
   docker build -t bangalore-house-prices .
   ```

2. **Run Docker Container Locally**
   ```bash
   docker run -p 5000:5000 bangalore-house-prices
   ```

3. **Access Application**
   ```
   http://localhost:5000
   ```

4. **Push to Docker Hub (Optional)**
   ```bash
   docker tag bangalore-house-prices your-username/bangalore-house-prices
   docker push your-username/bangalore-house-prices
   ```

5. **Deploy to Cloud Services**
   - AWS ECS
   - Google Cloud Run
   - Azure Container Instances
   - DigitalOcean

---

### Option 4: Deploy on Railway.app

#### Steps:

1. **Go to Railway.app**
   - Visit https://railway.app
   - Sign up with GitHub

2. **Create New Project**
   - Click "New Project"
   - Select "Deploy from GitHub"

3. **Select Repository**
   - Choose banglore_house_prices_predictor
   - Click "Deploy"

4. **Railway Auto-Detects Python**
   - Automatically finds requirements.txt
   - Installs dependencies
   - Starts the application

5. **Your app is live**
   - Check the Railway dashboard for your live URL

**Cost**: Free tier with usage limits

---

### Option 5: Deploy on AWS EC2 (Production)

#### Steps:

1. **Create EC2 Instance**
   - Ubuntu 20.04 LTS
   - t2.micro (free tier eligible)

2. **Connect to Instance**
   ```bash
   ssh -i your-key.pem ubuntu@your-instance-ip
   ```

3. **Install Dependencies**
   ```bash
   sudo apt update
   sudo apt install python3-pip python3-venv git
   ```

4. **Clone Repository**
   ```bash
   git clone https://github.com/25f1002035-ux/banglore_house_prices_predictor.git
   cd banglore_house_prices_predictor
   ```

5. **Create Virtual Environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

6. **Run Application**
   ```bash
   cd server
   gunicorn -w 4 -b 0.0.0.0:5000 server:app
   ```

7. **Set Up Reverse Proxy (Nginx)**
   - Install Nginx
   - Configure to forward requests to Gunicorn
   - Add SSL certificate (Let's Encrypt)

**Cost**: Variable (free tier for 12 months)

---

## Local Development Setup

### Prerequisites:
- Python 3.9+
- pip
- Git

### Steps:

1. **Clone Repository**
   ```bash
   git clone https://github.com/25f1002035-ux/banglore_house_prices_predictor.git
   cd banglore_house_prices_predictor
   ```

2. **Create Virtual Environment**
   ```bash
   python -m venv venv
   # Windows:
   venv\Scripts\activate
   # macOS/Linux:
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Application**
   ```bash
   cd server
   python server.py
   ```

5. **Access Application**
   ```
   http://localhost:5000
   ```

---

## Environment Variables

Create a `.env` file in the root directory:

```
FLASK_ENV=production
FLASK_DEBUG=0
PORT=5000
```

---

## Troubleshooting

### Issue: Module not found errors
**Solution**: Ensure all dependencies in requirements.txt are installed
```bash
pip install -r requirements.txt --upgrade
```

### Issue: Model file not found
**Solution**: Verify banglore_home_prices_model.pickle exists in the model directory

### Issue: Port 5000 already in use
**Solution**: Change PORT environment variable or kill the process using port 5000

### Issue: Static files not loading
**Solution**: Ensure client folder contains app.html, app.css, and app.js

---

## Performance Optimization

1. **Enable Caching**: Add caching headers for static assets
2. **Use CDN**: Serve static files from a CDN
3. **Database Connection Pooling**: If using a database
4. **Load Balancing**: Use multiple Gunicorn workers (already configured as 4)
5. **Monitoring**: Set up error tracking with Sentry

---

## Next Steps

1. Choose your deployment platform
2. Follow the step-by-step guide for that platform
3. Test the deployment
4. Monitor logs and errors
5. Set up automated deployments (GitHub Actions)

---

## Resources

- [Heroku Documentation](https://devcenter.heroku.com/)
- [Render Documentation](https://render.com/docs)
- [Docker Documentation](https://docs.docker.com/)
- [Flask Deployment](https://flask.palletsprojects.com/en/2.3.x/deploying/)
- [Gunicorn Documentation](https://gunicorn.org/)

---

## Support

For issues or questions:
1. Check the troubleshooting section
2. Review logs using platform-specific commands
3. Check Stack Overflow for similar issues
4. Reach out to platform support

---

**Last Updated**: January 2026
**Deployment Ready**: ✓
