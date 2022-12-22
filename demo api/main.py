from fastapi import FastAPI
from fastapi import Body
import uvicorn


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Welcome Subrata"}


@app.get("/posts")
def get_posts():
    return {"data": "Your Post"}


@app.post("/createpost")
# payload : stores the data sent by the user (postman) via POST request
def create_posts(payload: dict = Body(...)):
    print(payload)
    return {
        "new post": f"user : {payload['user']}, title : {payload['title']}, image : {payload['img']} "
    }
