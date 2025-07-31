# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Install system dependencies required by python-magic
RUN apt-get update && apt-get install -y libmagic1 && rm -rf /var/lib/apt/lists/*

# Install gunicorn
RUN pip install gunicorn

# Copy the dependency configuration file
COPY pyproject.toml .

# Install project dependencies
# The '.' installs the project in the current directory, which includes dependencies from pyproject.toml
RUN pip install .

# Copy the rest of the application source code into the container
COPY . .

# Command to run the application using Gunicorn
# Render will set the PORT environment variable.
# Gunicorn will run the app by calling the create_app factory in the 'app' package.
CMD gunicorn --bind 0.0.0.0:$PORT "app:create_app()"

