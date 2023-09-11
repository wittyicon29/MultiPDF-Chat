import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceInstructEmbeddings
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.llms import GPT4All, HuggingFaceHub
from html_templates import css, bot_template, user_template


def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text


def get_text_chunks(raw_text):
    text_splitter = CharacterTextSplitter(
        separator = "\n",
        chunk_size = 1000,
        chunk_overlap = 200,
        length_function = len
    )
    
    chunks = text_splitter.split_text(raw_text)
    return chunks


def get_vector_store(text_chunks):
    embeddings = HuggingFaceInstructEmbeddings(model_name = "hkunlp/instructor-large")
    vectorstore = FAISS.from_texts(texts = text_chunks, embedding = embeddings)
    return vectorstore


def conversation_chain(vectorstore):
    llm = HuggingFaceHub(repo_id = "google/flan-t5-small", model_kwargs = {"temperature":0.5, "max_length":512})
    memory = ConversationBufferMemory(memory_key = "chat_history", return_message = True)
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm = llm,
        retriever = vectorstore.as_retriever(),
        memory = memory
    )
    return conversation_chain

def handle_user_input(user_input):
    response = st.session_state.conversation({'question' : user_input})
    st.session_state.chat_history = response['chat_history']
    
    for i, message in enumerate(st.session_state.chat_history):
        if i % 2 == 0:
            st.write(user_template.replace("{{MSG}}", message.content), unsafe_allow_html = True)
        else:
            st.write(bot_template.replace("{{MSG}}", message.content), unsafe_allow_html = True)

def main():
    load_dotenv()
    st.set_page_config(page_title = "Chat with Multiple PDFs", page_icon = ":books")
    
    st.write(css, unsafe_allow_html = True)
    
    if "conversation" not in st.session_state:
        st.session_state.conversation = None
        
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None
    
    st.header("Chat with Multiple PDFs :books:")
    user_input = st.text_input("Ask a question about your documents: ")
    if user_input:
        handle_user_input(user_input)
    
    st.write(user_template.replace("{{MSG}}", "Hello Hagrid (Knower of all)"), unsafe_allow_html = True)
    st.write(bot_template.replace("{{MSG}}", "Hello Muggle"), unsafe_allow_html = True)

    
    with st.sidebar:
        st.subheader("Your documents")
        pdf_docs = st.file_uploader("Upload your PDFs here and click on 'Process'", accept_multiple_files = True)
        if st.button("Process"):
            with st.spinner("Processing"):
                
                raw_text = get_pdf_text(pdf_docs)
                st.write(raw_text)
                
                text_chunks = get_text_chunks(raw_text)
                st.write(text_chunks)
                
                vector_store = get_vector_store(text_chunks)
                
                st.session_state.conversation = conversation_chain(vector_store)
                
                
        
        
if __name__ == '__main__':
    main()