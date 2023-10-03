FROM python:3.11.1

WORKDIR /myapp

COPY . .

RUN pip install -r requirements.txt

RUN chmod +x start_worker.sh

RUN chmod +x migrate_and_run.sh
