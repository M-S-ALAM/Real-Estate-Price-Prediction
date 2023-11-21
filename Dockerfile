# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt /app/

RUN pip install --upgrade pip
# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Copy the entire current directory into the container at /app
COPY . /app

# Expose port 8501 for Streamlit
EXPOSE 8501

# Run your Streamlit app
CMD ["streamlit", "run", "app.py"]




