# FULL CODE

```python
import os
import requests
import PyPDF2
from io import BytesIO
from pdf2image import convert_from_bytes

import pdb

def download_arxiv_pdf(url, filename):
    response = requests.get(url)
    
    with open(filename, 'wb') as f:
        f.write(response.content)

def pdf_to_text(pdf_path):
    with open(pdf_path, 'rb') as f:
        reader = PyPDF2.PdfReader(f)
        text = ""

        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text += page.extract_text()

    return text

arxiv_pdf_url = "https://arxiv.org/pdf/2103.00020v1.pdf"  
filename = os.path.join(os.getcwd(), 'content', 'CLIP.pdf')  
download_arxiv_pdf(arxiv_pdf_url, filename)
pdf_text = pdf_to_text(filename)

arxiv_pdf_url = "https://arxiv.org/pdf/2106.09685.pdf"  
filename = os.path.join(os.getcwd(), 'content', 'LORA.pdf')  
download_arxiv_pdf(arxiv_pdf_url, filename)
pdf_text = pdf_to_text(filename)

############################################
import pinecone, openai
# from get_arxiv import *

os.environ["OPENAI_API_KEY"] = 

pinecone.init(api_key="", environment="northamerica-northeast1-gcp")

#####
from langchain.document_loaders import PyPDFLoader

folder_path = os.path.join(os.getcwd(), 'content')

documents = []
for filename in os.listdir(folder_path):
    if filename.endswith('.pdf'):
        # Do something with the PDF file
        file_path = os.path.join(folder_path, filename)
        loader = PyPDFLoader(file_path)
        pdf_pages = loader.load()  #takes a while
        documents.extend(pdf_pages)  # just add on, no separating pages by each pdf

# documents: each page Document() is a member of the list

#################
from langchain.text_splitter import RecursiveCharacterTextSplitter

def split_docs(documents,chunk_size=1000,chunk_overlap=20):
  text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
  docs = text_splitter.split_documents(documents)
  return docs

docs = split_docs(documents)
# print(len(docs))  # number of chunks, each size 1000

# #################
from langchain.embeddings.openai import OpenAIEmbeddings

embeddings = OpenAIEmbeddings(model_name="ada")

# query_result = embeddings.embed_query("Hello world")  # vector of 1024

# #################
from langchain.vectorstores import Pinecone

index_name = "demo"
index = Pinecone.from_documents(docs, embeddings, index_name=index_name) #upload embds
# index = pinecone.Index("demo")
  #  'Index' object has no attribute 'similarity_search'

def get_similiar_docs(query,k=10,score=False):
  if score:
    similar_docs = index.similarity_search_with_score(query,k=k)
  else:
    similar_docs = index.similarity_search(query,k=k)
  return similar_docs

#################
# from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI

model_name = "gpt-3.5-turbo"
# model_name = "text-davinci-003"
# model_name = "gpt-4"
# llm = OpenAI(model_name=model_name)
llm = ChatOpenAI(model_name=model_name)

from langchain.chains.question_answering import load_qa_chain
chain = load_qa_chain(llm, chain_type="stuff")

def get_answer(query):
  similar_docs = get_similiar_docs(query)
  answer =  chain.run(input_documents=similar_docs, question=query)
  return  answer

# query = "What are the most important results of this paper?"
# query = "Summarize"
# query = "Compare LORA to CLIP"
query = "What is LORA and what is CLIP?"
# get_answer(query)

# it does recognize LORA and CLIP, but k=2 doesn't allow it to retrieve LORA. Try to expand the k. k=10 also doesn't work though
# however, if k is too large: openai.error.InvalidRequestError: This model's maximum context length is 4097 tokens. However, your messages resulted in 4494 tokens. Please reduce the length of the messages.

###########
# find what embeddings are retrieved upon query
similar_docs = index.similarity_search(query, k=2)
for result in similar_docs:
    print(result.page_content)

##################################
pdb.set_trace()
```