
import os
import sys
import pinecone
from langchain.llms import Replicate
from langchain.vectorstores import Pinecone
from langchain.text_splitter import CharacterTextSplitter
from langchain.document_loaders import PyPDFLoader
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.chains import ConversationalRetrievalChain
from langchain.chains import RetrievalQA

# Replicate API token
os.environ['REPLICATE_API_TOKEN'] = "r8_d6SWhMJ3MgKb9SDvB37yqocz3F8T9Mn1PJtvD"

# Initialize Pinecone
pinecone.init(api_key='430f691b-720a-4e41-a078-366aca7e442a', environment='YOUR_ENVIRONMENT')

# Load and preprocess the PDF document
loader = PyPDFLoader('./WT_Employee_Referral_Policy_V3.pdf')
documents = loader.load()

# Split the documents into smaller chunks for processing
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
texts = text_splitter.split_documents(documents)
# print("---", texts)
# Use HuggingFace embeddings for transforming text into numerical vectors
embeddings = HuggingFaceEmbeddings()

# Set up the Pinecone vector database
index_name = "rameshshelke"
index = pinecone.Index(index_name)
print("index---",index.__dict__)
"""
vectordb = Pinecone.from_documents(texts, embeddings, index_name=index_name)

print("vector db----",vectordb)
# Initialize Replicate Llama2 Model
llm = Replicate(
    model="a16z-infra/llama13b-v2-chat:df7690f1994d94e96ad9d568eac121aecf50684a0b0963b25a41cc40061269e5",
    input={"temperature": 0.75, "max_length": 3000}
)
"""
# # Set up the Conversational Retrieval Chain
# qa_chain = ConversationalRetrievalChain.from_llm(
#     llm,
#     vectordb.as_retriever(search_kwargs={'k': 2}),
#     return_source_documents=True
# )

# Load vector database that was persisted earlier and check collection count in it
from langchain.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI

persist_directory = 'docs/chroma/'
embedding = OpenAIEmbeddings()
vectordb = Chroma(persist_directory=persist_directory, embedding_function=embedding)
print(vectordb._collection.count())

llm = ChatOpenAI(model_name="llm_name", temperature=0)
# Create a QA Chain
qa_chain = RetrievalQA.from_chain_type(
    llm,
    retriever=vectordb.as_retriever()
)
