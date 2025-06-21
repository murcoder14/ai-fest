from langchain_community.document_loaders import WebBaseLoader, PyPDFLoader

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_milvus import Milvus
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_text_splitters import RecursiveCharacterTextSplitter

# New Content Generation
def make_llm():
    return ChatOpenAI(model="gpt-4o",temperature=0)

def chat_using_simple_questions():
    prompt_template = PromptTemplate.from_template("Tell me how to curb weeds in my {topic}")
    model = make_llm()
    output_parser = StrOutputParser()
    chain = prompt_template | model | output_parser
    print(chain.invoke({"topic":"lawn"}))

# Reads a PDF document and allows the user to ask questions about the content inside it
def chat_about_pdf_document():
    loader = PyPDFLoader("data/course_catalog.pdf")
    query = "If I have completed Linear Algebra Honors and Multivariable Calculus courses at Choate Rosemary Hall, what other Math courses am I eligible to take?"
    embed_it(loader, query)

# Reads a Web Page and allows the user to ask questions about it
def chat_about_web_page_data():
    # Create a WebBaseLoader instance to load the content from a web page
    #loader = WebBaseLoader("https://www.bushheritage.org.au/species/wombats")  # This could be any web page
    #query = "How far do wombats travel to eat?"  # Replace this with any other question about the page's content
    loader = WebBaseLoader("https://www.choate.edu/ai/gen")  # This could be any web page
    query = "What AI tools are formally approved by Choate Rosemary Hall?"  # Replace this with any other question about the page's content as shown below
    #query = "Who owns the ownership of Generative AI outputs at Choate?"
    #query = "Name any 2 members of the Generative AI Steering Committee at Choate"
    embed_it(loader, query)

def embed_it(loader, query):
    # Load documents from web sources using the loader
    documents = loader.load()
    # Initialize a RecursiveCharacterTextSplitter for splitting text into chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=200)
    # Split the documents into chunks using the text_splitter
    docs = text_splitter.split_documents(documents)
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
    # Vectorstore with document embeddings
    vectorstore = Milvus.from_documents(
        documents=docs,
        embedding=embeddings,
        connection_args={
            "uri": "http://localhost:19530",
        },
        drop_old=True,  # Drop the old Milvus collection if it exists
    )
    # vectorstore.similarity_search(query, k=1)
    call_llm(query, vectorstore)


def call_llm(query, vectorstore):
    # Define the prompt template for generating AI responses
    prompt_template = """
    Human: You are an AI assistant, that provides answers to questions by using fact based and statistical information when possible.
    Use the following pieces of information to provide a concise answer to the question enclosed in <question> tags.
    If you don't know the answer, just say that you don't know, don't try to make up an answer.
    <context>
    {context}
    </context>

    <question>
    {question}
    </question>

    The response should be specific and use statistics or numbers when possible.

    Assistant:"""
    # Create a PromptTemplate instance with the defined template and input variables
    prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
    # Convert the vector store to a retriever
    retriever = vectorstore.as_retriever()
    # Define the RAG (Retrieval-Augmented Generation) chain for AI response generation
    rag_chain = (
            {"context": retriever | format_docs, "question": RunnablePassthrough()}
            | prompt
            | make_llm()
            | StrOutputParser()
    )
    # Invoke the RAG chain with a specific question and retrieve the response
    res = rag_chain.invoke(query)
    print(res)


# Define a function to format the retrieved documents
def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)