import fastapi
import uvicorn  # server that runs the api

# app or api, instance of the fastapi
api = fastapi.FastAPI()


@api.get("/")
def index():
    body = "<html>"\
        "<body style = 'padding:10px>'"\
        "<h1>Welcome to the API</h1>"\
        "<div>"\
        "Try this : <a href='/api/calculate?x=3&y=6&z=3'>/api/calculate?x=3&y=6&z=3</a>"\
        "</div>"\
        "</body>"\
        "</html>"

    return fastapi.responses.HTMLResponse(content=body)


# connects the function to the api and how to access it


@api.get("/api/calculate")
def calculate(x: int, y: int, z: int = 0):
    if z == 0:
        return fastapi.responses.JSONResponse(
            content={"error": "Zero Error : can't divide by zero."},
            status_code=400
        )

    if z is not None:
        value = (x+y)/z

    return {
        "x": x,
        "y": y,
        "z": z,
        "value": value,
    }


# server that runs the api
uvicorn.run(api, host="127.0.0.1", port=8000)
