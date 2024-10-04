FROM python:3.11.7

# Environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /chat-app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    libffi-dev \
    libssl-dev \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Copy project files
COPY . /chat-app

# Upgrade pip and install dependencies
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Expose the app port
EXPOSE 8000

# Run the application
CMD ["python", "jatte/manage.py", "runserver", "0.0.0.0:8000"]





# FROM python:3.11.7

# # Environment variables
# ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONUNBUFFERED 1

# # Set work directory
# WORKDIR /chat-app

# RUN apt-get update && apt-get install -y \
#     build-essential \
#     python3-dev \
#     libffi-dev \
#     libssl-dev

# COPY . /chat-app

# RUN pip install --upgrade pip
# RUN pip install -r requirements.txt

# EXPOSE 8000
# CMD ["python", "jatte/manage.py", "runserver", "0.0.0.0:8000"]