FROM python:3.12-slim-bookworm as builder
WORKDIR /app
COPY ./requirements.txt .
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

FROM python:3.12-slim-bookworm
WORKDIR /app
COPY --from=builder /usr/local /usr/local
COPY ./src /app
CMD ["opentelemetry-instrument", "python", "main.py"]