import fastapi
import uvicorn  # server that runs the api

# app or api, instance of the fastapi
api = fastapi.FastAPI()


# connects the function to the api and how to access it
@api.get("/api/calculate")
def calculate():           # api endpoint
    value = 2+2
    return {
        "value": value
    }


# server that runs the api
uvicorn.run(api, host="127.0.0.1", port=8000)





