from flask import Flask, Request, render_template
from engine import engine
from models import User
from sqlalchemy import select
from sqlalchemy.orm import Session

app = Flask(__name__) # Создаем приложение. __name__ - название файла

session = Session(engine) # Cессия для работы с бд

def get_data_from_user() -> list[User]:
    stmt: list[User] = session.query(User).all() # Запрос всех данных из таблицы с пользователями
    # stmt это список с классом пользователя внутри
    # [<models.User object at 0x000001F931FAACD0>, <models.User object at 0x000001F931FAAD50>....]
    return stmt # Возвращаем данные

@app.route("/") # Опредедение маршрута для приложения
def main() -> Request:
    users: list[User] = get_data_from_user() # Вызов функции, получение списка с пользователями
    return render_template('data_page.html', users=users) 

if __name__ == '__main__':
    # Запуск приложения
    app.run(debug=True)

# Чтобы запустить:
# 1: .\.venv\Scripts\activate
# 2: python main.py