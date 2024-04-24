import streamlit as st

# Set the page title
st.title('Нейросеть и инструменты')

# Add a logo
if st.sidebar.image('logo.png', width=100):
    st.sidebar.markdown('')

# Add a sidebar for selecting the tool
st.sidebar.header('Выберите инструмент')
tool = st.sidebar.radio('',
                        ['Чат с нейросетью', 'Загрузка файлов', 'Поиск литературы'])

# Define the chat function
def chat():
    message = st.text_input('Ваше сообщение:', key='chat_input')
    if message:
        with st.spinner('Отправка сообщения...'):
            st.session_state.chat_history.append((message, 'user'))
            response = get_response(message)
            st.session_state.chat_history.append((response, 'ai'))

    if 'chat_history' not in st.session_state:
        st.session_state['chat_history'] = []

    chat_history = st.session_state.chat_history

    for i, (msg, role) in enumerate(chat_history):
        if role == 'user':
            st.markdown(f"**Вы:** {msg}", unsafe_allow_html=True)
        else:
            st.markdown(f"**Нейросеть:** {msg}", unsafe_allow_html=True)

        if i < len(chat_history) - 1:
            st.markdown('---')

    if st.button('Отправить'):
        chat()

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

# Style the buttons
def style_button(button_name):
    return f"""
    <style>
    {button_name} {{
        background-color: #0070f3;
        color: white;
        font-size: 16px;
        padding: 10px 20px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        margin-top: 10px;
    }}
    </style>
    """

st.markdown(style_button('.stButton'), unsafe_allow_html=True)

# Display the appropriate tool based on the selected option
if tool == 'Чат с нейросетью':
    chat()
elif tool == 'Загрузка файлов':
    file_upload()
elif tool == 'Поиск литературы':
    literature_search()
else:
    st.write('')
