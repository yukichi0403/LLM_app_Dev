import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.schema import AIMessage, HumanMessage, SystemMessage


llm = ChatOpenAI(temperature=0)
st.set_page_config(
    page_title="My Great ChatGPT",
    page_icon="🤗",
)
st.header("My Great ChatGPT")

if "messages" not in st.session_state:
    st.session_state["messages"] = [SystemMessage(content="You are a helpful assistant.")]

if user_input := st.chat_input("聞きたいことを入力してね！"):
    st.session_state.messages.append(HumanMessage(content=user_input))
    with st.spinner("ChatGPT is typing..."):
        response = llm.invoke(st.session_state.messages)
        st.session_state.messages.append(AIMessage(content=response.content))


messages = st.session_state.get("messages",[])
for message in messages:
    if isinstance(message, AIMessage):
        with st.chat_message("assistant"):
            st.markdown(message.content)
    elif isinstance(message, HumanMessage):
        with st.chat_message("user"):
            st.markdown(message.content)
    else:
        st.write(f"System message: {message.content}")
# print(st.session_state.messages)