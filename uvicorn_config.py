import uvicorn
if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,       # Remove or set to False in production.
        workers=1,         # Increase this number in production.
        log_level="debug"
    )