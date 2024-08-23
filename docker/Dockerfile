# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8888 available to the world outside this container
EXPOSE 8888
ENV SCAN_PORT=8888
# Run the application using gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8888", "app.scanner:app"]
