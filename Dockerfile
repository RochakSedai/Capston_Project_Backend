FROM python:3.12

WORKDIR /app

COPY pyproject.toml README.md poetry.lock* /app/

RUN pip install --no-cache-dir poetry watchdog && \
    poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi --no-root

COPY . /app/
#CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

CMD ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port $PORT"]