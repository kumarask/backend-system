import uvicorn
from backend_module.app import app

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
