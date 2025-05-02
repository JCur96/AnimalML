FROM nvidia/cuda:12.2.0-devel-ubuntu22.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    python3.10 python3.10-venv python3.10-distutils python3-pip \
    curl git && \
    ln -sf python3.10 /usr/bin/python3 && \
    ln -sf pip3 /usr/bin/pip && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip && pip install -r requirements.txt
RUN pip install megadetector
COPY animalml animalml

ENV FLASK_APP=animalml.app
ENV FLASK_ENV=development
ENV PYTHONPATH=/app

CMD ["flask", "run", "--host=0.0.0.0", "--port=8000"]
