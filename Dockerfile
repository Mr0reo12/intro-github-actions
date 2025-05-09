# Use a image Python 3.12 
FROM python:3.12-slim

# Here we set the environment 
WORKDIR /app

# Copy archive to the image
COPY . /app

# Install system dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir fastapi uvicorn


# Create a new user
RUN useradd -m appuser

# Change the root user to appuser
USER appuser

# Expose the port the app runs on
EXPOSE 8000

# Command to run the app
CMD [ "uvicorn", "main:app", "--host", "0.0.0", "--port", "8000", "--reload" ]

