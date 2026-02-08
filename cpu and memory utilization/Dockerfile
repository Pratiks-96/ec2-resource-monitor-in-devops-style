# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy script
COPY ec2_monitor.py .

# Install dependencies
RUN pip install --no-cache-dir psutil

# Run script
CMD ["python", "ec2_monitor.py"]
