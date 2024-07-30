import streamlit as st
import replicate
import os

# Page title
st.set_page_config(page_title="Llama 3.1 🦙 Chatbot 🤖")


# Replicate api key Credentials
with st.sidebar:
    col1, col2 = st.columns(2)
    with col1:
        st.image("img/ollama.png", width=100)
    with col2:
        st.image("img/meta2.png", width=130)
    st.title('Llama 3.1 🦙 Chatbot 🤖')
    replicate_api = st.text_input('Enter Replicate API token:', type='password')
    if not (replicate_api.startswith('r8_') and len(replicate_api) == 40):
        st.warning('Please enter your credentials!', icon='⚠️')
        st.info("You can get your api key from this button bellow 👇", icon='ℹ️')
        st.link_button('Get your replicate api key', url='https://replicate.com/account/api-tokens', use_container_width=True)
    else:
        st.success("You're good to go now, start chatting!", icon='🤝')

    st.subheader('Models and parameters')
    selected_model = st.sidebar.selectbox('Choose a Llama2 model',
                                          ['Llama3.1-405B', 'llama3-70b', 'llama3-8b'], key='selected_model')
    if selected_model == 'Llama3.1-405B':
        llm = 'meta/meta-llama-3.1-405b-instruct'
    elif selected_model == 'llama3-8b':
        llm = 'meta/meta-llama-3-8b'
    else:
        llm = 'meta/meta-llama-3-70b'

    temperature = st.sidebar.slider('temperature', min_value=0.01, max_value=5.0, value=0.1, step=0.01)
    top_p = st.sidebar.slider('top_p', min_value=0.01, max_value=1.0, value=0.9, step=0.01)
    max_length = st.sidebar.slider('max_length', min_value=64, max_value=4096, value=512, step=8)

os.environ['REPLICATE_API_TOKEN'] = replicate_api

# Store LLM generated responses
if "messages" not in st.session_state.keys():
    st.session_state.messages = [
        {"role": "assistant", "content": "Hi there!👋 I'm here to help 💡, What's on your mind 🧠?"}]

# Display or clear chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])


def clear_chat_history():
    st.session_state.messages = [
        {"role": "assistant", "content": "Hi there!👋 I'm here to help 💡, What's on your mind 🧠?"}]

st.sidebar.button('Clear Chat History', on_click=clear_chat_history)
st.sidebar.html("<p>Developed with ❤️ by <a href='https://github.com/amine-sabbahi' target='_blank'>Sabbahi</a></p>")
st.sidebar.image("img/SABBAHI.png", width=250)

# Function for generating Llama3.1 response
def generate_llama3_1_response(prompt_input):
    string_dialogue = "You are a helpful assistant. You do not respond as 'User' or pretend to be 'User'. You only respond once as 'Assistant'."
    for dict_message in st.session_state.messages:
        if dict_message["role"] == "user":
            string_dialogue += "User: " + dict_message["content"] + "\n\n"
        else:
            string_dialogue += "Assistant: " + dict_message["content"] + "\n\n"
    output = replicate.run(llm,
                           input={"prompt": f"{string_dialogue} {prompt_input} Assistant: ",
                                  "temperature": temperature, "top_p": top_p, "max_length": max_length,
                                  "repetition_penalty": 1})
    return output


# User-provided prompt
if prompt := st.chat_input(disabled=not replicate_api):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

# Generate a new response if last message is not from assistant
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = generate_llama3_1_response(prompt)
            placeholder = st.empty()
            full_response = ''
            for item in response:
                full_response += item
                placeholder.markdown(full_response)
            placeholder.markdown(full_response)
    message = {"role": "assistant", "content": full_response}
    st.session_state.messages.append(message)