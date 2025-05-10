from fastapi import FastAPI
from fastapi.responses import JSONResponse


def create_app() -> FastAPI:
    app = FastAPI()

    @app.get("/", response_class=JSONResponse)
    async def read_root():
        return {
            "title": "My First API",
            "message": "Hello, Welcome to the API!"
        }

    @app.get("/usuarios", response_class=JSONResponse)
    async def get_usuarios():
        return {
            "usuarios": [
                {"id": 1, "name": "John Doe"},
                {"id": 2, "name": "Jane Smith"},
                {"id": 3, "name": "Alice Johnson"},
                {"id": 4, "name": "Bob Brown"}
            ]
        }

    return app


app = create_app()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
