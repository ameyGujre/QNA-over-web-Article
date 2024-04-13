import streamlit as st
from utils import get_response
st.title("Article QnA Assistant")
st.caption("This is a QnA Assistant powered by gpt3.5turbo")



if 'OPENAI_API_KEY' not in st.session_state:
    st.session_state['OPENAI_API_KEY'] = ""
    

if st.session_state['OPENAI_API_KEY'] == "":
    
    api_key = st.text_input(label="Enter your OpenAI API Key", type='password')
    if st.button("Submit"):
        st.session_state['OPENAI_API_KEY'] = api_key
        st.rerun()
else:
    prompt = st.chat_input("Enter your query")



    if prompt:
        with st.chat_message("user"):
            st.write(prompt)
        with st.spinner("Processing your query"):
            response = get_response(prompt,api_key=st.session_state['OPENAI_API_KEY'])
            
            with st.chat_message("assistant"):
                st.write(response)