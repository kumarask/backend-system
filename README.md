# Backend System – C++ Multithreaded Queue with Python Bindings & Prometheus Metrics

A multithreaded backend system written in C++ with Python bindings using `pybind11`, exposing producer/consumer backends with retry logic, lifecycle hooks, Prometheus metrics, FastAPI control API, and full Docker/K8s support.

---

## 📁 Project Structure

```
backend-system/
├── base/                         # C++ base classes (Queue, Producer, Consumer)
├── bindings/                     # pybind11 bindings
├── metrics/                      # Prometheus HTTP metrics server
├── python/backend_module/        # Python FastAPI + custom wrappers
├── grafana/                      # Dashboards and alert rules
├── helm/backend-chart/           # Helm chart for Kubernetes
├── .github/workflows/            # GitHub Actions CI/CD
├── systemd/, supervisord/        # Production service configs
├── Dockerfile, setup.py, .env
├── README.md, LICENSE
```

---

## ⚙️ Requirements

- Linux / WSL / macOS
- CMake, GCC/G++, Make
- Python 3.10+
- [pybind11](https://github.com/pybind/pybind11)
- Prometheus, Grafana (optional)
- Docker, Helm, Kubernetes (optional)

---

## 🧪 Local Build (C++ + Python)

```bash
# Install dependencies
sudo apt install cmake g++ python3-dev python3-pip
pip install pybind11 fastapi uvicorn prometheus_client

# Build C++ backend
cd base/
mkdir build && cd build
cmake ..
make

# Build Python bindings
cd ../../bindings/
mkdir build && cd build
cmake ..
make

# Test Python module
cd ../../python/
python3 -m backend_module.backend_service
```

---

## 🐳 Docker Build & Run

```bash
# Build Docker image
docker build -t backend-system .

# Run container
docker run -d -p 8000:8000 -p 9091:9091 backend-system
```

---

## ☁️ Kubernetes Deployment (with Helm)

```bash
cd helm/backend-chart/
helm install backend-release .

# To uninstall:
# helm uninstall backend-release
```

---

## 📈 Prometheus + Grafana Integration

- Prometheus scrape endpoint: `http://localhost:9091/metrics`
- Grafana JSON dashboard available under `grafana/`
- Use `grafana/alert_rules.yml` with Alertmanager

---

## 🖥️ Systemd or Supervisord

For production services:

```bash
# systemd
sudo cp systemd/backend.service /etc/systemd/system/
sudo systemctl enable --now backend

# OR supervisord
sudo cp supervisord/backend.conf /etc/supervisor/conf.d/
sudo supervisorctl reread
sudo supervisorctl update
```

---

## 📞 API Endpoints (FastAPI)

| Method | Endpoint          | Description         |
|--------|-------------------|---------------------|
| GET    | `/status`         | Health check        |
| POST   | `/start`          | Start backend       |
| POST   | `/stop`           | Stop backend        |
| POST   | `/enqueue`        | Add item to queue   |
| GET    | `/metrics`        | Prometheus metrics  |

---

🛠 Example Helm Install
```bash
helm install backend ./helm/backend-chart
```
---

## 📜 License

MIT License

---

## 🙋 Contact

Developed by: **Kumara Krishnappa**  
GitHub: [github.com/kumarask](https://github.com/kumarask)
