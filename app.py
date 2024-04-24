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
    st.markdown('<div style="height: 300px; overflow-y: scroll;">', unsafe_allow_html=True)
    if 'chat_history' not in st.session_state:
        st.session_state['chat_history'] = []

    message = st.text_input('Ваше сообщение:', key='chat_input')
    if st.button('Отправить'):
        if message:
            st.session_state.chat_history.append((message, 'user'))
            st.session_state.chat_history.append(('Ответ от нейросети', 'ai'))
            st.experimental_rerun()

    chat_history = st.session_state.chat_history

    for i, (msg, role) in enumerate(chat_history):
        if role == 'user':
            st.markdown(f"**Вы:** {msg}", unsafe_allow_html=True)
        else:
            st.markdown(f"**Нейросеть:** Ответ от нейросети", unsafe_allow_html=True)

        if i < len(chat_history) - 1:
            st.markdown('---')

    st.markdown('</div>', unsafe_allow_html=True)

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
