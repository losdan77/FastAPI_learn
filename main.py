#uvicorn main:app --reload
from fastapi import FastAPI

app = FastAPI(title='Tranding App')

fake_users = [{'id': 1, 'role': 'admin', 'name': 'los'},
              {'id': 2, 'role': 'user', 'name': 'bob'}]

fake_trades = [{'id': 1, 'user_id': 2, 'currancy': 'BTC', 'side': 'buy', 'price': 123},
               {'id': 2, 'user_id': 2, 'currancy': 'BTC', 'side': 'sell', 'price': 125}]


@app.get('/')
def hello():
    return 'hi wirld'


@app.get('/users/{user_id}')
def users(user_id: int):
    return [user for user in fake_users if user['id'] == user_id]


@app.get('/trades')
def get_trades(limit: int = 10, offset: int = 0):
    return fake_trades[offset:][:limit]


@app.post('/users/{user_id}')
def change_user_name(user_id: int, new_name: str):
    current_user = list(filter(lambda user: user['id'] == user_id, fake_users))[0]
    current_user['name'] = new_name
    return {'status': 200, 'data': current_user}
