## MultiPDF-Chat
This is a Python application that allows you to have a conversation with multiple PDF documents. You can ask questions about your documents, and the application will provide you with answers based on the content of the PDFs. You can ask questions about the PDFs using natural language, and the application will provide relevant responses based on the content of the documents. This app utilizes a language model to generate accurate answers to your queries. Please note that the app will only respond to questions related to the loaded PDFs.

## Features

- **PDF Text Extraction**: The application extracts text from multiple PDF documents.

- **Text Chunking**: The extracted text is divided into manageable chunks for processing.

- **Semantic Search**: It performs semantic search on the text chunks using deep learning embeddings.

- **Conversational AI**: You can have a conversation with the AI using natural language.

## How does it works 
![PDF-LangChain](https://github.com/wittyicon29/MultiPDF-Chat/assets/99320225/d51c9823-b443-418f-8e50-da1318c27213)

The application uses the following components:

- **PDF Text Extraction**:  It extracts text from the uploaded PDFs using PyPDF2.
- **Text Chunking**:  The extracted text is divided into chunks for efficient processing.
- **Semantic Search**: It leverages Hugging Face Transformers to create embeddings of text chunks and uses FAISS for semantic search.
- **Conversational AI**: Conversations are handled using Streamlit and Hugging Face's conversational models.

## Configuration 

You can configure the behavior of the application by modifying the code in main.py. You can change the PDF text extraction method, text chunking parameters, and conversational AI model.

## Installation

To run this application, you'll need Python and the required libraries installed. You can install the necessary dependencies using `pip`:

```bash
pip install -r requirements.txt
```
Then from the app.py run the following command in the terminal using `streamlit`:

```bash
streamlit run app.py
```

PS. In the .env file you can change the environment variable API TOKEN

## Usage

1. **Upload PDFs**: Upload your PDF documents using the file uploader.

2. **Ask Questions**: Type your questions in the input box and click "Ask."

3. **Get Answers**: The application will provide answers based on the content of the PDFs.


## Liscense
The MultiPDF App is released under the MIT License.

## Acknowledgment
Reference - [Ask Multiple PDFs](https://github.com/alejandro-ao/ask-multiple-pdfs/tree/main)
