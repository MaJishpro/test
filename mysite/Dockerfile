# Dockerfile
FROM python:3.9
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /body
COPY requirements.txt /body/
RUN pip install --upgrade pip && pip install -r requirements.txt
COPY / /body/
CMD ["sh", "run.sh"]