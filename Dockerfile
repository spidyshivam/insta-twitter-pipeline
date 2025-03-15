# Use official Python image
FROM python:3.13

# Set the working directory inside the container
WORKDIR /app

# Copy the project files to the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install -r requirements.txt

# Expose the application port (adjust based on FastAPI/Flask)
EXPOSE 8000

# Set environment variables ( Using .env file )

# Run the application (modify command based on your framework)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
