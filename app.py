import json 
import streamlit as st
import requests

st.title("Chat GPT Clone")
st.header("",divider="grey")


def palmApiRequest(user_input):
    url="https://generativelanguage.googleapis.com/v1beta3/models/text-bison-001:generateText?key={API_KEY}"
    payload={"prompt":{"text": user_input}}
    resource=requests.post(url,json=payload)
    print(resource.text)
    return json.loads(resource.text)["candidates"][0]["output"]

if "inputs" not in st.session_state:
    st.session_state.inputs=[]
for i in st.session_state.inputs:
    with st.chat_message(i["role"]):
        st.markdown(i["content"])

user_input=st.chat_input("Ask Anything 🤷‍♂️")

if user_input:
    user_message=st.chat_message("user")
    user_message.markdown(user_input)
    st.session_state.inputs.append({"role":"user","content":user_input})

    ai_message=st.chat_message("assistant")
    with ai_message:
        resource=palmApiRequest(user_input)
        st.markdown(resource)
        st.session_state.inputs.append({"role":"assistant","content":resource})


    