from fastapi import FastAPI

app = FastAPI(title="soil-ai - ai-service")

@app.get("/health")
async def health():
    return {"status":"ok"}

@app.post("/clean")
async def clean(payload: dict):
    # placeholder: implement CSV cleaning pipeline later
    return {"received": True, "payload_shape": len(payload)}