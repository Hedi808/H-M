from fastapi import FastAPI

app = FastAPI(title="CloudMind Test App")


@app.get("/")
def root():
    return {
        "message": "Maram + Hedi = APT",
        "status": "running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }
