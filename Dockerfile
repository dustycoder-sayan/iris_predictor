# Use an official Python runtime as a parent image/base image
FROM python:bullseye

# Set current working directory of the container to /app
WORKDIR /app

# Copy the requirements.txt to the container
COPY requirements.txt .

# Install dependencies
pip install --no-cache-dir -r requirements.txt

# Copy Code
COPY . .

# Expose Port 8080
EXPOSE 8080
 
# Run the application
CMD ["python", "backend/iris.py"]