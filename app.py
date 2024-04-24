import streamlit as st

# Set the page title
st.title('Нейросеть и инструменты')

# Add a logo
if st.sidebar.image('logo.png', width=100):
    st.sidebar.markdown('')

# Add a sidebar for selecting the tool
st.sidebar.header('Выберите инструмент')
tool = st.sidebar.selectbox('', ['Чат с нейросетью', 'Загрузка файлов', 'Поиск литературы'])

# Define the chat function
def chat():
    message = st.text_input('Ваше сообщение:')
    if st.button('Отправить'):
        st.write('Ответ от нейросети')

# Define the file upload function
def file_upload():
    uploaded_work = st.file_uploader('Загрузите файл своей работы:')
    uploaded_task = st.file_uploader('Загрузите файл технического задания:')

    if st.button('Сгенерировать файл'):
        st.write('Сгенерированный файл:')

# Define the literature search function
def literature_search():
    topic = st.text_input('Введите тему проекта:')
    description = st.text_area('Короткое описание:')

    if st.button('Найти литературу'):
        st.write('Результаты поиска литературы:')

# Display the appropriate tool based on the selected option
if tool == 'Чат с нейросетью':
    chat()
elif tool == 'Загрузка файлов':
    file_upload()
elif tool == 'Поиск литературы':
    literature_search()
else:
    st.write('')
