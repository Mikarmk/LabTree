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
    if 'chat_history' not in st.session_state:
        st.session_state['chat_history'] = []

    message = st.text_input('Ваше сообщение:', key='chat_input')
    uploaded_file = st.file_uploader('Загрузите файл:', type=['txt', 'pdf', 'docx'])

    if st.button('Отправить'):
        if message:
            st.session_state.chat_history.append((message, 'user'))
            st.session_state.chat_history.append(('Ответ от нейросети', 'ai'))
            st.experimental_rerun()

        if uploaded_file is not None:
            # Обработка загруженного файла
            st.session_state.chat_history.append(('Файл:', 'user'))
            st.session_state.chat_history.append((uploaded_file, 'user'))
            st.experimental_rerun()

    # Display the chat history in a scrollable container
    chat_container = st.container()
    with chat_container:
        if st.session_state.chat_history:
            st.markdown('<div style="height: 300px; overflow-y: scroll;">', unsafe_allow_html=True)
            for i, (msg, role) in enumerate(st.session_state.chat_history):
                if role == 'user':
                    st.markdown(f"**Вы:** {msg}", unsafe_allow_html=True)
                else:
                    st.markdown(f"**Нейросеть:** {msg}", unsafe_allow_html=True)
                if i < len(st.session_state.chat_history) - 1:
                    st.markdown('---')
            st.markdown('</div>', unsafe_allow_html=True)

    # Place the input field below the chat history
    input_container = st.container()
    with input_container:
        st.write('')
        if st.button('Отправить'):
            if message:
                st.session_state.chat_history.append((message, 'user'))
                st.session_state.chat_history.append(('Ответ от нейросети', 'ai'))
                st.experimental_rerun()

        if uploaded_file is not None:
            # Обработка загруженного файла
            st.session_state.chat_history.append(('Файл:', 'user'))
            st.session_state.chat_history.append((uploaded_file, 'user'))
            st.experimental_rerun()

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
    uploaded_file = st.file_uploader('Загрузите файл:', type=['txt', 'pdf', 'docx'])

    if st.button('Найти литературу'):
        st.write('Результаты поиска литературы:')

        if uploaded_file is not None:
            # Обработка загруженного файла
            st.write('Вы загрузили файл:', uploaded_file)

# Display the appropriate tool based on the selected option
if tool == 'Чат с нейросетью':
    chat()
elif tool == 'Загрузка файлов':
    file_upload()
elif tool == 'Поиск литературы':
    literature_search()
else:
    st.write('')
