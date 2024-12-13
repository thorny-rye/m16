from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}


@app.get('/users')
async def get_query() -> dict:
    return users


@app.post('/user/{username}/{age}')
async def post_query(username: Annotated[str, Path(min_length=5, max_length=20,
                                                   description="Input your username", examples=["Marcus"])],
                     age: Annotated[int, Path(ge=18, le=120, description="Input your age", examples=[22])]) -> str:
    user_id = str(int(max(users, key=int)) + 1)
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"User {user_id} is registered"


@app.put('/user/{user_id}/{username}/{age}')
async def put_query(user_id: Annotated[int, Path(ge=1, le=100,description="Specify User ID", examples=[1])],
                    username: Annotated[str, Path(min_length=5, max_length=20,
                                                  description="Input your username", examples=["Marcus"])],
                    age: Annotated[int, Path(ge=18, le=120, description="Input your age", examples=[22])]) -> str:
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"The user {user_id} is updated"


@app.delete('/user/{user_id}')
async def delete_query(user_id: Annotated[int, Path(ge=0, le=100,
                                                    description="Specify User ID which would deleted", examples=[1])]):
    users.pop(str(user_id))
    return f"User {user_id} has been deleted"
