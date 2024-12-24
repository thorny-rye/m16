from fastapi import FastAPI, HTTPException, Body
from pydantic import BaseModel
from typing import List

app = FastAPI()

users = []


class User(BaseModel):
    id: int = None
    username: str
    age: int = None


@app.get('/users')
async def get_query() -> List[User]:
    return users


@app.post('/user/{username}/{age}')
async def post_query(user: User, username: str, age: int):
    new_id = users[-1].id + 1 if users else 1
    new_user = User(id=new_id, username=username, age=age)
    users.append(new_user)
    return new_user


@app.put('/user/{user_id}/{username}/{age}')
async def put_query(user_id: int, username: str, age: int) -> str:
    try:
        edit_id = users[user_id]
        edit_id.username = username
        edit_id.age = age
        return edit_id
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")

@app.delete('/user/{user_id}')
async def delete_query(user_id: int, user: User) -> List[User]:
    try:
        del_user = users[user_id]
        users.pop(del_user)
        return user
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")
