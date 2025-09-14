# # Use an official Python runtime as a parent image
# FROM python:3.9-slim

# # Set the working directory in the container
# WORKDIR /app

# # Copy the requirements file into the container
# COPY requirements.txt .

# # Install any needed packages specified in requirements.txt
# RUN pip install --no-cache-dir -r requirements.txt

# # Copy the data, etl, and database directories into the container
# # This ensures all necessary files for the ETL process are available
# COPY data/ data/
# COPY etl/ etl/
# COPY database/ database/

# ##### Copy main.py from the root of your local project to the /app directory in the container
# COPY main.py . 

# # Create the database directory if it doesn't exist (important for volume mounting)
# RUN mkdir -p database

# # Define the command to run the ETL pipeline
# # This command will be executed when the container starts
# CMD ["python", "main.py"]



# Use official Python image
FROM python:3.9-slim-buster

# Set working directory
WORKDIR /app

# Copy only essential files first for faster builds
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files
COPY . .

# Create database directory (for volume mounting)
RUN mkdir -p database

# Default command to run ETL pipeline
CMD ["python", "main.py"]
