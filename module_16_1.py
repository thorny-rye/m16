from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def welcome() -> str:
    return 'Главная страница'


@app.get('/user/admin')
async def admin() -> str:
    return "Вы вошли как администратор"


@app.get('/user/{user_id}')
async def user_id(user_id):
    return f'Вы вошли как пользователь № {user_id}'

@app.get('/user')
async def user_info(username, age):
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"
