# Use the official Python image as the base image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy project files into the container
COPY ./get_status.py /app/
COPY ./.env /app/

# Copy the requirements file into the container and install the dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python3", "get_status.py"]