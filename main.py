from fastapi import FastAPI, Request
import jwt
from config import SIGNING_SECRET
import uvicorn

app = FastAPI()


@app.post('/monday')
async def receive_hook(request: Request):
    """
    Receive an action from Monday
    """
    # fetch request body
    res = await request.json()
    # In payload, you can find the "input fields" you selected in the action on monday
    print("Payload")
    print(res)
    # fetch token from authorization headers
    token = request.headers.get("authorization")
    try:
        # decode token with signing secret from monday
        claims = jwt.decode(
            token, 
            SIGNING_SECRET, 
            algorithms="HS256", 
            audience=str(request.url)
        )
        print("Decoded token in first time")
        # if decoded, token is valid
        # claims contains multiple pieces of info including the id of the user that triggered the action
        print(claims)

    except Exception as e:
        print("Failed to decode first time")
        print(e)

    return res

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)