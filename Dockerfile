# Use the jupyter/pyspark-notebook as the base image
FROM jupyter/pyspark-notebook:latest

# Add any additional configurations or dependencies if needed
# For example:
# USER root
# RUN apt-get update && apt-get install -y your-package-name


COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

# Switch back to the default jovyan user
USER $NB_UID