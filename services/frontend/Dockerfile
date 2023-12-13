FROM python:3.12-slim-bookworm as builder
WORKDIR /app
COPY ./requirements.txt .
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

FROM python:3.12-slim-bookworm
WORKDIR /app
COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY ./src /app
CMD ["python", "main.py"]