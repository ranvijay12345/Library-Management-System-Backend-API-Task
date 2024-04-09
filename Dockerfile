# Use the official Python image as base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the FastAPI app files to the working directory
COPY . .

EXPOSE 5000
# Command to run the FastAPI application
CMD ["uvicorn", "index:app", "--host", "0.0.0.0", "--port", "5000"]
