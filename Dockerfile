FROM python:3.11.1

WORKDIR /myapp

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY start_worker.sh ./
RUN chmod +x start_worker.sh

COPY . .
