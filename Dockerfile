# GET THE IMAGE SLIM-BUSTER
FROM python:3.10.6-slim-buster

# RUN ITS CONTENT THE FILE TO INSTALL
# UPDATES FROM THE DEBIAN REPOSITORIES
# COPY install-packages.sh .
# RUN chmod +x install-packages.sh
# RUN ./install-packages.sh

# INSTALL APT PACKAGES
RUN apt-get update && apt-get install --no-install-recommends -y \
    # dependencies for building Python packages
    build-essential \
    # psycopg2 dependencies
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# CREATE AND SET WORKING DIRECTORY
# RUN mkdir /app
WORKDIR /app

# FORCE STDIN, STDOUT AND STDERR TO BE TOTALLY UNBUFFERED. ON SYSTEMS WHERE IT MATTERS, ALSO PUT STDIN, STDOUT AND STDERR IN BINARY MODE.
# SET DEFAULT ENVIRONMENT VARIABLES
ENV PYTHONUNBUFFERED 1
# PYTHON FROM COPYING PYC FILES TO THE CONTAINER
ENV PYTHONDONTWRITEBYTECODE 1

# COPY /requirements/requirements.txt /app
COPY /requirements /app

RUN python3 -m pip install --no-cache-dir --upgrade \
    pip \
    setuptools \
    wheel
# RUN python3 -m pip install --no-cache-dir -r requirements.txt
RUN python3 -m pip install --no-cache-dir -r local.txt

# INSTALL REQUIRED SYSTEM DEPENDENCIES
RUN apt-get update && apt-get install --no-install-recommends -y \
    # psycopg2 dependencies
    libpq-dev \
    # Translations dependencies
    gettext \
    # cleaning up unused files
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
    && rm -rf /var/lib/apt/lists/*

# ADD CURRENT DIRECTORY CODE TO WORKING DIRECTORY
COPY . /app
