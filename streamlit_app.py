import streamlit as st
from ai import ask_ai

# Show title and description.
st.title("Demo Maffra Agentic System Chatbot")
st.write(" A finalidade desta demo é demonstrar a capacidade do bot de responder perguntas baseadas no documentos presentes na Vector Database")
#    uploaded_file = st.file_uploader(
 #       "Upload a document (.txt or .md)", type=("txt", "md")
  #  )
@st.fragment()
def ask_ai_func():
    st.subheader('Perguntas')
    user_question = st.text_input("Faça uma pergunta sobre algum documento presente na VDB, 'Fale sobre o CV.doc' ")
    if st.button("Enviar"):
        with st.spinner():
            result = ask_ai(user_question)
            st.write(result)

if __name__ == "__main__":
    ask_ai_func()
