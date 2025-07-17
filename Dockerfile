// File: Dockerfile

# Stage 1: Build C++ and Python bindings
FROM python:3.10-slim AS builder

# Install dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    cmake g++ make libstdc++6 \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy all files
COPY . .

# Install Python dependencies & build bindings
RUN pip install --upgrade pip setuptools wheel
RUN pip install -r python/backend_module/requirements.txt
RUN python setup.py build_ext --inplace bdist_wheel

# Stage 2: Runtime image
FROM python:3.10-slim

# Install runtime dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    libstdc++6 && apt-get clean && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy built wheel and install
COPY --from=builder /app/dist/*.whl .
RUN pip install *.whl

# Copy source files for runtime use (e.g., config, templates)
COPY python/backend_module /app/backend_module

# Expose FastAPI port
EXPOSE 8000

# Command to run FastAPI app
CMD ["uvicorn", "backend_module.main:app", "--host", "0.0.0.0", "--port", "8000"]
