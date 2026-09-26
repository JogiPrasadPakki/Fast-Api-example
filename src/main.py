import uvicorn


host = "0.0.0.0"
# read port from environment variable
port = os.getenv("PORT", 8002)
app_name = "app.main:app"


if __name__ == "__main__":
    uvicorn.run(app_name, host=host, port=port)
