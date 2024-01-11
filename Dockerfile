FROM python:3.8-slim-buster

# Set the working directory
WORKDIR /app

# Copy the contents of the local directory to the container
COPY . /app

# Install required system packages
RUN apt-get update && \
    apt-get install -y --fix-missing \
    ffmpeg libsm6 libxext6 unzip && \
    apt-get install -y awscli

# Update pip and install Python dependencies
RUN pip install --upgrade pip && \
    pip install psycopg2-binary && \
    pip install -r requirements.txt

# Set the user and group
ARG USER_NAME=jayen
ARG GROUP_NAME=jayen
RUN addgroup --gid 1000 $GROUP_NAME && \
    adduser --disabled-password --gecos '' --uid 1000 --gid 1000 $USER_NAME && \
    chown -R $USER_NAME:$GROUP_NAME /app

# Set the user and group ownership for the application directory
RUN chown -R $USER_NAME:$GROUP_NAME /app

# Switch to the non-root user
USER $USER_NAME

# Command to run the application
CMD ["python3", "app.py"]
