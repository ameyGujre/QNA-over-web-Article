##Creating utility functions for creating embeddings and retrival 
from langchain_community.document_loaders.web_base import WebBaseLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from langchain import hub
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

import os


# OPENAI_API_KEY = os.getenv("openai_api_key")


# ##instantiating embedding model
# embeddings = OpenAIEmbeddings(api_key=OPENAI_API_KEY, model="text-embedding-ada-002")

# ##Instantiating chatopenai model
# llm = ChatOpenAI(api_key=OPENAI_API_KEY, model="gpt-3.5-turbo",temperature=0)



def create_embeddings(page_url, api_key):
    
    embeddings = OpenAIEmbeddings(api_key=api_key, model="text-embedding-ada-002")
    
    try:
        loader = WebBaseLoader(page_url)
        documents = loader.load()
        
        text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
        docs = text_splitter.split_documents(documents=documents)
        
        db_new = FAISS.from_documents(docs, embeddings)
        
        try:
            db_old = FAISS.load_local(folder_path="embeddings/",index_name="index", embeddings=embeddings,allow_dangerous_deserialization=True)
            db_old.merge_from(db_new)
        except:
            
            db_new.save_local(folder_path="embeddings/",index_name="index")
        print(page_url)
        
        return True
    except Exception as E:
        
        return E
    
    
def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)


def get_response(query, api_key):
    
    embeddings = OpenAIEmbeddings(api_key=api_key, model="text-embedding-ada-002")
    
    llm = ChatOpenAI(api_key=api_key, model="gpt-3.5-turbo",temperature=0)
    
    db = FAISS.load_local(folder_path="embeddings/", embeddings=embeddings,allow_dangerous_deserialization=True)
    retriever = db.as_retriever(search_kwargs={'k': 3})
    
    prompt = hub.pull("rlm/rag-prompt")
    
    rag_chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
    )
    
    response = rag_chain.invoke(query)
    return response
if __name__=="__main__":
    
    # create_embeddings(page_url="https://pubmed.ncbi.nlm.nih.gov/29939616/")
    print(get_response(query="What is the gold standard for measurement of insulin resistance?"))