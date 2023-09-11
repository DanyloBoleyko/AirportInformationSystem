import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        'back.app:app',
        host="0.0.0.0",
        reload=True,
        port=5000
    )
