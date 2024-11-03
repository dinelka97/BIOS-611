# Use the official Python image from Docker Hub
FROM python:3.13

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy requirements.txt into the container
COPY requirements.txt ./

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Install additional system packages for NLTK
RUN apt-get update && apt-get install -y \
    build-essential \
    && apt-get clean

# Download NLTK resources (punkt and stopwords)
RUN python -m nltk.downloader punkt stopwords

# Copy the current directory contents into the container
COPY . .

# Run your Python script when the container launches
CMD ["python", "HW5_dinelka.py"]

