# Setup
## Libraries
import openai
import os
from dotenv import load_dotenv, find_dotenv
from IPython.display import display, Markdown
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import PyPDFLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import DocArrayInMemorySearch


## Variables
_ = load_dotenv(find_dotenv()) # read local .env file
openai.api_key = os.environ['OPENAI_API_KEY']

file = 'data/pdfs/ISLRv2_website.pdf'


# Load file
loader = PyPDFLoader(file)
document = loader.load()


# Split
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1500, chunk_overlap=150)
splits = text_splitter.split_documents(document)


# Convert into embeddings and store
embeddings = OpenAIEmbeddings()

db = DocArrayInMemorySearch.from_documents(
    splits, 
    embeddings
)


# Query 
query = input("Your query, e.g. 'Explain bias-variance tradeoff for a linear regression model.'")
similar_pages = db.similarity_search(query, limit=10)
retriever = db.as_retriever()
llm = ChatOpenAI(temperature = 0.0)
qpages = "".join([similar_pages[i].page_content for i in range(len(similar_pages))])
response = llm.call_as_llm(f"{qpages} Question: {query}") 
display(Markdown(response))

