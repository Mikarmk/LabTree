import streamlit as st
import sqlite3

# Создание базы данных
def create_database():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  username TEXT,
                  password TEXT)''')

    conn.commit()
    conn.close()

create_database()

# Функция для добавления пользователя в базу данных
def add_user(username, password):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()

    c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))

    conn.commit()
    conn.close()

# Функция для проверки аутентификации пользователя
def check_credentials(username, password):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()

    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    result = c.fetchone()

    conn.close()

    if result:
        return True
    else:
        return False

# Функция для отображения формы входа
def login():
    username = st.text_input('Имя пользователя')
    password = st.text_input('Пароль', type='password')

    if st.button('Войти'):
        if check_credentials(username, password):
            st.success('Успешный вход!')
            # Перенаправление на основную платформу
        else:
            st.error('Неверное имя пользователя или пароль.')

# Функция для отображения формы регистрации
def registration():
    new_username = st.text_input('Новое имя пользователя')
    new_password = st.text_input('Новый пароль', type='password')

    if st.button('Зарегистрироваться'):
        add_user(new_username, new_password)
        st.success('Регистрация прошла успешно!')

# Функция для отображения основной платформы
def main_platform():
    # Добавьте здесь функционал основной платформы (чат с нейросетью, загрузка файлов, поиск литературы)
    pass

# Проверка аутентификации пользователя
if 'username' not in st.session_state:
    # Отображение формы входа или регистрации
    login()
    registration()
else:
    # Если пользователь аутентифицирован, отображаем основную платформу
    main_platform()
