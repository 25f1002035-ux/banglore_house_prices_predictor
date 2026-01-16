FROM python:3.9-slim

WORKDIR /app

# Copy requirements
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose port
EXPOSE 5000

# Set environment variables
ENV FLASK_APP=server/server.py
ENV PYTHONUNBUFFERED=1

# Run gunicorn server
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "--chdir", "server", "server:app"]
