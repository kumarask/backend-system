FROM python:3.10-slim
WORKDIR /app
COPY . .
RUN pip install .
CMD ["python3", "python/backend_module/backend_service.py"]