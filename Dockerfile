FROM python:3.8-slim
    
# Set the working directory to /app
WORKDIR /app

COPY . /app

RUN apt-get update && \
    apt-get install -y build-essential

RUN pip install --trusted-host pypi.python.org -r requirements.txt
RUN find . -name "*.pyx" -exec cythonize -i {} \;

EXPOSE 80

ENV NAME World
